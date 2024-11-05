import numpy as np
from mrjob.job import MRJob
import csv
from io import StringIO
import pandas as pd
import json
import os
import logging
from IPython.display import display


class CSVMapperReducer(MRJob):

    def mapper(self, _, line):
        # Parse the CSV line
        rows = next(csv.reader(StringIO(line)))

        # # Convert the row to a DataFrame
        df = pd.DataFrame([rows])
        df.columns = ['company', 'location', 'industry', 'total_laid_off', 'percentage_laid_off', 'date', 'stage', 'country', 'funds_raised']

        # Perform data cleaning operations using pandas
        df[['total_laid_off', 'percentage_laid_off', 'funds_raised']] = df[['total_laid_off', 'percentage_laid_off', 'funds_raised']].apply(pd.to_numeric, errors='coerce')

        # Replace all empty values and strip leading/trailing whitespaces
        # df = df.applymap(lambda x: np.nan if pd.isna(x) or str(x).strip() == '' else x)

        df = df.replace('', np.nan)

        # # Convert the cleaned data to a JSON-compatible representation
        json_data = df.to_dict(orient='records')[0]
        yield None, json.dumps(json_data)

    def reducer(self, _, values):
        # Create a list to store the final data
        final_data = []

        # Iterate over each JSON-compatible data emitted by the mapper
        for json_data in values:
            # Convert the JSON-compatible data back to a DataFrame
            df = pd.DataFrame.from_dict([json.loads(json_data)])

            # Append the modified DataFrame to the final data list
            final_data.append(df)

        # Concatenate all DataFrames into one final DataFrame
        result_df = pd.concat(final_data, ignore_index=True)

        result_df['total_laid_off'].fillna(result_df['total_laid_off'].mean(), inplace=True)
        result_df['percentage_laid_off'].fillna(result_df['percentage_laid_off'].mean(), inplace=True)
        result_df['funds_raised'].fillna(result_df['funds_raised'].mean(), inplace=True)

        result_df['company'].fillna(result_df['company'].mode()[0], inplace=True)
        result_df['location'].fillna(result_df['location'].mode()[0], inplace=True)
        result_df['stage'].fillna(result_df['stage'].mode()[0], inplace=True)

        # Writing the data
        # # Output the final DataFrame to a local CSV file
        local_output_path = '/Users/kasivarmahasthi/Desktop/MS/DatascienceProject/output.csv'
        final_pd = pd.DataFrame(result_df)
        final_pd.to_csv(local_output_path, index=False)

        # Specify the desired HDFS path
        hdfs_output_path = '/Datascience/output/output.csv'

        # Upload the local CSV file to HDFS
        os.system(f'hadoop fs -put {local_output_path} {hdfs_output_path}')


if __name__ == '__main__':
    input_path = "/Users/kasivarmahasthi/Desktop/MS/DatascienceProject/layoffs.csv"
    CSVMapperReducer.run()
