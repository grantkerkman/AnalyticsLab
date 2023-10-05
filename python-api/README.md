# Weather Analysis with API Integration

## Background

Data's true power lies in its ability to definitively answer questions. In this project, we aim to answer a fundamental question: "What is the weather like as we approach the equator?" While the answer might seem obvious at first glance, we will use Python requests, APIs, and JSON traversals to provide concrete evidence and insights.

## Instructions

This project is divided into two main parts: WeatherPy and VacationPy.

### Part 1: WeatherPy

In WeatherPy, we create a Python script to visualize the weather of over 500 cities at varying distances from the equator. To achieve this, we utilize the following tools:
- [citipy Python library](https://pypi.org/project/citipy/)
- [OpenWeatherMap API](https://openweathermap.org/api)
- Python's data visualization libraries

**Tasks in WeatherPy include:**
- Retrieving weather data from cities using the OpenWeatherMap API.
- Creating scatter plots to illustrate key relationships:
  - Latitude vs. Temperature
  - Latitude vs. Humidity
  - Latitude vs. Cloudiness
  - Latitude vs. Wind Speed
- Calculating linear regressions for each relationship and separating the plots into Northern and Southern Hemispheres.

We aim to not only visualize but also provide meaningful insights into the relationships between latitude and various weather parameters.

### Part 2: VacationPy

In VacationPy, we leverage our weather data skills to plan future vacations. Using Jupyter notebooks, the `geoViews` Python library, and the Geoapify API, we create map visualizations to identify ideal travel destinations.

**Key tasks in VacationPy include:**
1. Creating a map displaying cities with point sizes representing humidity levels.
2. Filtering cities based on preferred weather conditions (e.g., ideal temperature, low wind speed, and clear skies).
3. Creating a new DataFrame to store hotel information.
4. Using the Geoapify API to find nearby hotels for each city.
5. Adding hotel names and country details to the map's hover messages.

## Dependencies

Before running the code, make sure you have the following dependencies installed:

- [`matplotlib.pyplot`](https://matplotlib.org/stable/contents.html) for data visualization
- [`pandas`](https://pandas.pydata.org/docs/) for data manipulation
- [`numpy`](https://numpy.org/doc/stable/) for numerical operations
- [`requests`](https://docs.python-requests.org/en/latest/) for making API requests
- [`hvplot.pandas`](https://hvplot.holoviz.org/user_guide/Plotting.html) for interactive plotting
- Other libraries such as `time` and [`scipy.stats`](https://docs.scipy.org/doc/scipy/reference/stats.html) for various calculations

You can install these dependencies using pip, but make sure to refer to the documentation links for detailed information on each library.

---

*Note: This README provides an overview of the Weather Analysis with API Integration project. For detailed code implementation and analysis, please refer to the Jupyter Notebooks provided for WeatherPy and VacationPy.*
