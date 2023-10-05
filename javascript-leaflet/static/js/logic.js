// Store our API endpoint as queryUrl.
let queryUrl = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson";


// Define a color scale for Earthquake depth
var colorScale = d3.scaleSequential(d3.interpolateInferno)
  .domain([0, 10]);

// Perform a GET request to the query URL.
d3.json(queryUrl).then(function (data) {
  console.log(data.features);

  let earthquakes = L.geoJSON(data.features, {
    pointToLayer: function (feature, latlng) {
      var magnitude = feature.properties.mag;
      var radius = Math.max(1, magnitude * 5);
      var depth = feature.geometry.coordinates[2];

      var geojsonMarkerOptions = {
        radius: radius,
        fillColor: colorScale(depth),
        color: 'black',
        weight: 1,
        opacity: 1,
        fillOpacity: 0.8
      };

      var marker = L.circleMarker(latlng, geojsonMarkerOptions);

      // Bind the popup and display earthquake information
      marker.bindPopup(
        "<h3>" + feature.properties.place + 
        "</h3><hr><p>" + new Date(feature.properties.time) + 
        "</p>" + "Earthquake Depth: " + feature.geometry.coordinates[2] + 
        "</p>" + "Earthquake Magnitude: " + feature.properties.mag);

      return marker;
    }
  });

  // Assuming createMap function is correctly defined elsewhere in your code
  createMap(earthquakes);
});

// Create the layers for the map 
function createMap(earthquakes) {
  // Create the base layers.
  let street = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  })

  let topo = L.tileLayer('https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png', {
    attribution: 'Map data: &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, <a href="http://viewfinderpanoramas.org">SRTM</a> | Map style: &copy; <a href="https://opentopomap.org">OpenTopoMap</a> (<a href="https://creativecommons.org/licenses/by-sa/3.0/">CC-BY-SA</a>)'
  });

  // Create a baseMaps object.
  let baseMaps = {
    "Street Map": street,
    "Topographic Map": topo
  };

  // Create an overlays object.
  let overlayMaps = {
    Earthquakes: earthquakes,
  };
  
  // Create a new map
  let myMap = L.map("map", {
    center: [
      37.09, -95.71
    ],
    zoom: 5,
    layers: [street, earthquakes]
  });

  // Create a layer control that contains our baseMaps.
  L.control.layers(baseMaps, overlayMaps, {
    collapsed: false
  }).addTo(myMap);

// Add in the Legend
// Define a color scale for Earthquake magnitude
var magnitudeColorScale = d3.scaleSequential(d3.interpolateViridis)
  .domain([0, 10]);

// Create the legend control
var legend = L.control({ position: 'bottomright' });

legend.onAdd = function (map) {
  var div = L.DomUtil.create('div', 'info legend');
  var labels = [];
  var magnitudes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

  // Loop through the magnitude values and generate labels
  for (var i = 0; i < magnitudes.length; i++) {
    var from = magnitudes[i];
    var to = magnitudes[i + 1];
    var color = magnitudeColorScale((from + to) / 2);

    labels.push(
      '<i style="background:' + color + '"></i> ' +
      from + (to ? '&ndash;' + to : '+'));
  }

  div.innerHTML = labels.join('<br>');
  return div;
};

// Add the legend to the map
legend.addTo(myMap);
  
}
