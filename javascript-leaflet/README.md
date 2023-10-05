# USGS Earthquake Data Visualization

## Background

The United States Geological Survey (USGS) is responsible for providing scientific data about natural hazards, the health of our ecosystems and environment, and the impacts of climate and land-use change. They collect a massive amount of earthquake data from all over the world each day but need a meaningful way to visualize and display this data. In this project, you will develop a tool to visualize USGS earthquake data, making it more accessible to the public and government organizations.

## Prerequisites

Before you begin, make sure you have the following:

- [Leaflet](https://leafletjs.com/): An open-source JavaScript library for interactive maps.
- [GeoJSON](https://geojson.org/): A format for encoding a variety of geographic data structures.

## Installation

1. Create a new repository for this project called `leaflet-challenge`. Do not add this Challenge to an existing repository.

2. Clone the new repository to your computer.

3. Inside your local git repository, create two directories: `Leaflet-Part-1` and `Leaflet-Part-2`. These will correspond to the two parts of the challenge.

4. Ensure you have all the necessary HTML and JavaScript files in each directory.

5. Push your changes to GitHub.

## Usage

### Part 1: Create the Earthquake Visualization

Your first task is to visualize an earthquake dataset using Leaflet. Here are the steps:

1. Get your dataset by visiting the [USGS GeoJSON Feed](https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php) page and choosing a dataset to visualize.

2. Use the URL of the chosen JSON dataset to pull in the earthquake data for visualization.

3. Using Leaflet, create an interactive map that plots all the earthquakes from your dataset based on their longitude and latitude.

4. Customize the data markers to reflect the magnitude of the earthquake by their size and the depth of the earthquake by color. Earthquakes with higher magnitudes should appear larger, and earthquakes with greater depth should appear darker in color.

5. Include popups that provide additional information about each earthquake when its associated marker is clicked.

6. Create a legend that provides context for the map data.

Your final visualization should resemble the sample map provided in the challenge instructions.

### Part 2: Gather and Plot More Data (Optional)

This part of the challenge is optional and does not earn extra points. It involves gathering and plotting additional data using Leaflet. You can choose to work on this part if you want to enhance your visualization further.

## Acknowledgments

- [USGS Earthquake Data](https://earthquake.usgs.gov/)
- [Leaflet Documentation](https://leafletjs.com/)
- [GeoJSON Specification](https://geojson.org/)
