# Clever Data Engineer Trial Project

## Goal of the Project:

At Clever, we are turning data into personalized and localized content so our readers can make well-informed decisions about any step of their real estate journey.

Please fork this repository and let us know when you've completed the project with a link to your fork.

Using the data set decribed below, and the Airflow-based data pipeline docker configuration, perform basic analysis for the chosen in `company_profiles_google_maps.csv`. There are basic errors on the DAG that you will need to fix for the pipeline to work properly. 

## Expectations
To perform this project you will need to:
* Perform transforms on the raw data and load them into a PostgreSQL database
* Be able to join datasets together in way for an analyst to be able to rank by a certain set of criteria (you can determine this criteria)
* Be able to filter the data by city or state so analysis can be performed by locality
* Given a locality, create a ranked list according to the criteria you’ve chosen

**Bonus:**
* Interesting additional analysis based on the underlying data
* An example could be Review Sentiment, common themes among ratings, complaints, etc.

## Dataset
Moving company data set (files can be found at 'dags/scripts/data_examples' folder)
* fmcsa_companies.csv
* fmcsa_company_snapshot.csv
* fmcsa_complaints.csv
* fmcsa_safer_data.csv
* company_profiles_google_maps.csv
* customer_reviews_google.csv


## Getting started
To get started with Airflow check the [getting started](docs/getting_started.md) documentation.


---


## Solution

### Introduction
In this project, I developed an end-to-end data pipeline using Airflow to extract, clean, and load moving company data into a PostgreSQL database.

An analysis was conducted in a Jupyter notebook. In this step, I joined relevant datasets, filtered the data by city, and ranked the companies based on customer ratings. As a bonus, I provided an overview of company performance and performed a text analysis to identify common keywords in customer reviews, which helped highlight recurring themes in customer feedback.

Through this solution, I demonstrated proficiency in building automated data pipelines, performing data transformation, and extracting meaningful insights from raw data.

### Pipeline Configuration
The solution fixes the existing errors in the Airflow DAG, ensuring that the pipeline runs smoothly to process the datasets. The pipeline includes the following steps:

1. **Data Extraction**: The provided CSV files are read using an Airflow DAG, which orchestrates the data flow from raw files to the PostgreSQL database.
2. **Data Cleaning (DataFrameCleaner Class)**: A custom `DataFrameCleaner` class was developed to handle data cleansing tasks.
3. **Data Loading**: The cleaned data is then loaded into the PostgreSQL database, making it ready for further analysis.

### Criteria for Ranking
The analysis was performed in a Jupyter notebook after the data was loaded into PostgreSQL. The key steps included:
- **Joining Datasets**: Selected datasets were joined, combining information such as reviews, company profiles, and other key data points.
- **Filtering by City**: The data was filtered by city to enable localized analysis.
- **Ranking by Rating**: The companies were ranked according to their average Google Review Rating, providing a clear view of customer satisfaction.

### Bonus Analysis
In addition to the ranking, further analysis was conducted in the Jupyter notebook:
- **Company Overview**: A comprehensive overview of the companies was created, summarizing average ratings, and reviews counts.
- **Frequent Keywords in Reviews**: A text analysis was performed to identify the most common keywords in customer reviews, highlighting recurring themes or issues mentioned by customers.

These insights provide a deeper understanding of the companies' performance and customer sentiment, allowing for more informed decision-making.
