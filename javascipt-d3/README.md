# belly-button-challenge



# Belly Button Biodiversity Dashboard

## Background

In this assignment, you will build an interactive dashboard to explore the Belly Button Biodiversity dataset, which catalogs the microbes that colonize human navels. The dataset reveals that a small handful of microbial species (also called operational taxonomic units, or OTUs, in the study) were present in more than 70% of people, while the rest were relatively rare.

Website can be viewed [here](https://grantkerkman.github.io/belly-button-challenge/).

## Prerequisites

Before you begin, make sure you have the following:

- [D3.js](https://d3js.org/) library for creating data-driven documents.

## Installation

1. Create a new repository for this project called `belly-button-challenge`. Do not add this Challenge to an existing repository.

2. Clone the new repository to your computer.

3. Inside your local git repository, copy the files from the `StarterCode` folder contained within the Module 14 Challenge zip file. This includes `index.html`, `samples.json`, and the `static` folder.

4. Push the above changes to GitHub.

## Usage

### D3 Library

[D3.js](https://d3js.org/) is a JavaScript library for creating interactive data visualizations in the browser. In this project, D3 is used to:

- Read in the `samples.json` dataset from a provided URL.
- Create horizontal bar charts to display the top 10 OTUs found in an individual.
- Create a bubble chart to display each sample.
- Update all the plots when a new sample is selected.

### Interactive Features

1. **Bar Chart**: A horizontal bar chart displays the top 10 OTUs found in an individual's sample. It uses `sample_values` as the values for the bars, `otu_ids` as the labels, and `otu_labels` as the hovertext. Users can select different individuals from the dropdown menu to see their corresponding data.

2. **Bubble Chart**: A bubble chart displays each sample's OTUs. It uses `otu_ids` for the x values, `sample_values` for the y values, `sample_values` for the marker size, `otu_ids` for the marker colors, and `otu_labels` for the text values. This chart provides a visual representation of OTUs across samples.

3. **Demographic Info**: A panel displays an individual's demographic information, including various key-value pairs. This information is updated when a new sample is selected from the dropdown menu.

### Deployment

Deploy your app to a free static page hosting service, such as GitHub Pages, and submit the links to your deployment and your GitHub repository. Ensure that your repository has regular commits and a thorough `README.md` file.

## Acknowledgments

- [D3.js Documentation](https://d3js.org/)
- Assignment instructions and starter code provided by your course instructor.
