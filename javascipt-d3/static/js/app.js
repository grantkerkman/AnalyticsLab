let url = "https://2u-data-curriculum-team.s3.amazonaws.com/dataviz-classroom/v1.1/14-Interactive-Web-Visualizations/02-Homework/samples.json";

// Create the function to handle all charting
function displayCharts(id) {

    // Fetch Data for charts
    d3.json(url).then(function(data) {

    samples = data.samples;

    console.log(samples);

    // Create the Data for the Bar Chart

    let selectedSample = samples.filter(sample => sample.id == id);

    console.log(selectedSample);

    otuIds = selectedSample[0].otu_ids.slice(0,10).reverse();
    otuLabels = selectedSample[0].otu_labels.slice(0,10).reverse();
    samplesValues = selectedSample[0].sample_values.slice(0,10).reverse();

    // Create the bar chart
        let barData = [{
            x: samplesValues,
            y: otuIds.map(id => `OTU ${id}`),
            text: otuLabels,
            type: 'bar',
            orientation: 'h'
      }];
  
    // Define the layout for the bar chart
        let barLayout = {
            title: 'Top 10 OTUs Found',
            xaxis: { title: 'Sample Values' },
            yaxis: { title: 'OTU ID' }
      };
  
    // Use Plotly to create the bar chart
    Plotly.newPlot('bar', barData, barLayout);

    // Create data for the bubble chart
    otuIdsBubble = selectedSample[0].otu_ids;
    otuLabelsBubble = selectedSample[0].otu_labels;
    samplesValuesBubble = selectedSample[0].sample_values;

    // Create the bubble chart
        let bubbleData = [{
            x: otuIdsBubble,
            y: samplesValuesBubble,
            text: otuLabelsBubble,
            mode: 'markers',
            marker: {
            size: samplesValuesBubble,
            color: otuIdsBubble,
            colorscale: 'Earth',
            colorbar: {
                title: 'OTU ID'
          }
        }
      }];
  
    // Define the layout for the bubble chart
        let bubbleLayout = {
            title: 'OTU Bubble Chart',
            xaxis: { title: 'OTU ID' },
            yaxis: { title: 'Sample Values' },
            showlegend: false,
            height: 500
      };
  
    // Use Plotly to create the bubble chart
    Plotly.newPlot('bubble', bubbleData, bubbleLayout);

    // Create the metadata panel
    metadata = data.metadata;
        
    let selectedMeta = metadata.filter(m => m.id == id);

    const demographicInfo = selectedMeta[0];

    const panelBody = document.getElementById("sample-metadata");
    
    // Clear previous content
    panelBody.innerHTML = "";

    // Create and append new content
        for (const key in demographicInfo) {
            if (demographicInfo.hasOwnProperty(key)) {
            const value = demographicInfo[key];
            const paragraph = document.createElement("p");
            paragraph.textContent = `${key}: ${value}`;
            panelBody.appendChild(paragraph);
        }
      }
    });
}

// Create function to handle changing a selection
function optionChanged(selectedId) {

    console.log(selectedId);

    displayCharts(selectedId);

}




function init () {
    // Fetch the JSON data and console log it
    d3.json(url).then(function(data) {
    
    console.log(data);

    // Fill the dropdown menu with all the IDs
    let dropdownMenu = d3.select("#selDataset");

    console.log(data.names);

    let ids = data.names;

    for (let i=0; i<ids.length; i++) {

        dropdownMenu.append("option").text(ids[i]).property("value", ids[i]);

    }

    first = ids[0];

    // Display Charts and panel with first ID
    displayCharts(first);
});
}

init()