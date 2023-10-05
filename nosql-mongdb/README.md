# UK Food Standards Agency Data Analysis

## Overview

The UK Food Standards Agency evaluates various food establishments across the United Kingdom and assigns them a food hygiene rating. This project aims to analyze the food hygiene ratings data to assist the food magazine, "Eat Safe, Love," in identifying locations for future articles. The analysis is divided into three parts: setting up the database, updating the database, and performing exploratory analysis.

## Part 1: Database and Jupyter Notebook Set Up

### Database Setup

1. Import the data provided in the `establishments.json` file into a MongoDB database named `uk_food` and a collection named `establishments`. The data import command used in the Terminal should be documented in a markdown cell within the Jupyter Notebook.

2. Import the required Python libraries: PyMongo and Pretty Print (pprint).

3. Create an instance of the Mongo Client.

4. Confirm the database and collection setup:
   - List the databases to ensure `uk_food` is listed.
   - List the collections to ensure `establishments` is present.
   - Use `find_one` and `pprint` to display one document from the `establishments` collection.

### Part 2: Update the Database

1. Add a new restaurant, "Penang Flavours," to the database as per the provided information.

2. Find the BusinessTypeID for "Restaurant/Cafe/Canteen" and return the BusinessTypeID and BusinessType fields.

3. Update the new restaurant's BusinessTypeID based on the previous step's result.

4. Remove establishments within the "Dover" Local Authority from the database.

5. Convert number values stored as strings to numeric values:
   - Use `update_many` to convert latitude and longitude to decimal numbers.
   - Use `update_many` to convert RatingValue to integer numbers.

## Part 3: Exploratory Analysis

### Data Exploration

1. Answer specific questions to assist "Eat Safe, Love" magazine:
   - Find establishments with a hygiene score equal to 20.
   - Identify establishments in London with a RatingValue greater than or equal to 4 (use regex for London's Local Authority name).
   - Determine the top 5 establishments with a RatingValue of 5, sorted by the lowest hygiene score, nearest to "Penang Flavours" restaurant (within 0.01 degrees of latitude and longitude).
   - Count establishments in each Local Authority area with a hygiene score of 0, sorted from highest to lowest, and display the top ten local authority areas.
   
2. For each question:
   - Use `count_documents` to show the number of documents in the result.
   - Display the first document in the results using `pprint`.
   - Convert the result to a Pandas DataFrame, print the number of rows, and display the first 10 rows.

## Dependencies

Make sure to install the required Python libraries:
- [PyMongo](https://pymongo.readthedocs.io/en/stable/)
- [Pretty Print (pprint)](https://docs.python.org/3/library/pprint.html)

## Contributing

Contributions to this project are welcome. If you have any suggestions, improvements, or bug reports, please feel free to open issues or submit pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
