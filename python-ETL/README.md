# Used Cars ETL Project

## Overview

This project involves the extraction, transformation, and loading (ETL) of a dataset containing information about used car sales from Craigslist. The dataset was sourced from Kaggle, and the aim is to prepare and load the data into a MongoDB database. Below are the details of each ETL process.

## Dependencies

Before running this project, ensure you have the following dependencies installed:

- [Pandas](https://pandas.pydata.org/docs/): Used for data manipulation and transformation.
- [PyMongo](https://pymongo.readthedocs.io/en/stable/): Used to interact with MongoDB.
- [Datetime](https://docs.python.org/3/library/datetime.html): Used for datetime-related operations.

## Extract

The dataset was sourced from Kaggle, and the original dataset was provided in the form of a large CSV file, approximately 1.5 GB in size. Python's Pandas library was used to read and manipulate the data.

## Transform

The data transformation process involved several steps to clean and prepare the dataset for loading into MongoDB:

1. Initial Data Inspection:
   - The `.info()` method was used to get an overview of the dataset's size, shape, data types, and potential data quality issues.

2. Removing Unnecessary Columns:
   - A list of columns that were not needed for analysis was identified and removed using the `.drop()` method.
   - The 'county' column, which contained no data, was removed before dropping missing data to prevent data loss.

3. Handling Missing Values:
   - The `.dropna()` method was applied in-place to remove rows with missing or incomplete data.

4. Data Type Conversion:
   - The 'year' column was converted from floating-point to integer data type.
   - The 'cylinders' column was cleaned by removing the word 'cylinder' from its values using `.replace()` and a list comprehension.

5. Date and Time Conversion:
   - The 'datetime' column needed conversion from ISO 8601 format to a simpler date format, as the time information was not needed.
   - The `.split()` method was used to separate the date and time, with only the date being retained.
   - The cleaned 'cylinders' and 'datetime' columns were inserted back into the dataframe.
   - The `.to_datetime()` method was applied to the 'datetime' column to convert the values.

6. Verification:
   - The `.info()` method was called again to verify that all transformations were successful, and the data was ready for loading.

## Load

The final transformed data, stored in the dataframe 'raw_df,' was loaded into a MongoDB database using the following steps:

1. Data Preparation:
   - The data from the 'raw_df' dataframe was converted to a list of dictionaries using `to_dict(orient='records')`.

2. MongoDB Connection:
   - A connection to the MongoDB server was established using the PyMongo library, and a specific collection within the 'forsale_db' database named 'vehicles' was chosen for data insertion.

3. Data Insertion:
   - The `insert_many()` method was used to insert the data into the MongoDB collection, ensuring that the data was well-formatted for readability.


