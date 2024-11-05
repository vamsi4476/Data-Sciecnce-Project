# Tech Layoffs Analysis (2019-2023)

## Project Overview
This project investigates the trends and causes behind significant layoffs within the global technology sector from 2019 to 2023. By leveraging machine learning models and Hadoop MapReduce, the analysis explores the primary factors driving workforce reductions, such as economic downturns, over-hiring, and strategic shifts within tech companies.

## Motivation
The tech industry faced substantial layoffs during this period, influenced by economic pressures, the COVID-19 pandemic, and rapid digital transformation. This project aims to dissect these factors and uncover valuable insights into the dynamics behind tech layoffs, helping stakeholders understand patterns and anticipate future trends.

## Dataset
- **Source**: [Layoffs.fyi](https://layoffs.fyi/) and [Kaggle Layoffs 2022 Dataset](https://www.kaggle.com/datasets/swaptr/layoffs-2022/data)
- **Contents**: Details on layoffs across companies, including fields like `company`, `location`, `industry`, `total_laid_off`, `percentage_laid_off`, `date`, `stage`, `country`, and `funds_raised`.

## Project Structure
- **main.py**: Contains the `CSVMapperReducer` class, which performs data cleaning and transformation using Hadoop MapReduce. It outputs a clean, processed CSV file ready for analysis.
- **layoffs.csv**: Original dataset used for analysis.
- **techlayoffs_project_report.docx**: Final report detailing methodology, results, and conclusions.
- **output.csv**: Processed output file, saved locally and on HDFS.

## Approach
1. **Data Preprocessing**: Handle missing values, normalize data types, and ensure data consistency.
2. **Exploratory Data Analysis (EDA)**: Identify trends, outliers, and key factors contributing to layoffs across different industries and locations.
3. **Hypothesis Testing & Statistical Analysis**: Use advanced statistical methods to investigate economic indicators, COVID-19 impact, and other factors.
4. **Machine Learning Models**:
   - Decision Tree Classifier
   - Random Forest Classifier
   - Bagging Classifier
   - **Performance**: Bagging achieved the highest accuracy (~94%).

5. **Sentiment Analysis**: Evaluate public sentiment on layoffs from news articles and press releases.
6. **Time-Series Analysis**: Examine trends over time to understand patterns of layoffs in various industries and regions.

## Results Summary
- **Key Insights**:
  - Layoffs spiked in 2020, dropped in 2021, and rose sharply again in 2022.
  - The U.S. and India saw the most significant impacts, with Consumer and Food industries hit hardest in 2022.
  - The Travel industry showed resilience with fewer layoffs in 2022 compared to 2020.
- **Model Accuracy**:
  - Decision Tree: 92.98%
  - Bagging: 94.58%
  - Random Forest: 80.70%

## How to Run the Project
1. **Prerequisites**:
   - Install Hadoop for MapReduce ([Hadoop Installation Guide](https://www.youtube.com/watch?v=H999fIuymqc))
   - Install required Python libraries: `numpy`, `pandas`, `mrjob`, and `sklearn`
   - Set up a local or virtual environment with Python 3.7 or later.

2. **Run the Mapper and Reducer**:
   - Ensure Hadoop is running and configured correctly.
   - Run the `main.py` script:
     ```bash
     python main.py
     ```
   - The script will process the dataset using MapReduce and output the cleaned data to `output.csv` locally and in HDFS at `/Datascience/output/output.csv`.

3. **Model Training and Evaluation**:
   - Load `output.csv` into a Jupyter Notebook or Python script.
   - Use the `sklearn` library to train and test the Decision Tree, Random Forest, and Bagging classifiers as demonstrated in `main.py`.

## File Descriptions
- `main.py`: Main script containing the MapReduce job for data processing.
- `layoffs.csv`: Original dataset containing layoff information.
- `output.csv`: Processed and cleaned dataset.
- `techlayoffs_project_report.docx`: Detailed report of project methodology, analysis, and findings.

## Technologies Used
- **Programming Languages**: Python (NumPy, Pandas, scikit-learn)
- **Big Data**: Hadoop MapReduce
- **Machine Learning Models**: Decision Tree, Random Forest, Bagging Classifier
- **Data Visualization**: Seaborn, Matplotlib
- **Sentiment Analysis**: Natural Language Processing (NLP) with `TextBlob`

## Future Work
- **Extend Sentiment Analysis**: Use more robust NLP models to capture sentiment trends more accurately.
- **Explore Other ML Models**: Try additional classification algorithms like Gradient Boosting or XGBoost for potential accuracy improvements.
- **Enhance Time-Series Analysis**: Implement ARIMA or other models for predicting future layoff trends.

## Authors
- **Principal Investigator**: Vamsi Krishna Gunda

## References
- [Layoffs.fyi](https://layoffs.fyi/) - Original Dataset.
- [Kaggle Dataset](https://www.kaggle.com/datasets/swaptr/layoffs-2022/data)
- [TechCrunch Article on 2023 Layoffs](https://techcrunch.com/2023/09/19/tech-industry-layoffs-2023/)

---

Feel free to contribute to this project by opening an issue or creating a pull request.
