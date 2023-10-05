# Import the dependencies.
import numpy as np
import pandas as pd
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################

# Create the engine
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)

# Save reference to the table
measurement = Base.classes.measurement
station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/date_range/start_date/final_date"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query Precipitation from the Jupyter Notebook
    date_o = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precip_results = session.query(measurement.date, measurement.prcp).filter(measurement.date > date_o).all()
    
    session.close()

    # Create the dictionary
    all_precip = []
    for date, prcp in precip_results:
        precip_dict = {}
        precip_dict["date"] = date
        precip_dict["prcp"] = prcp
        all_precip.append(precip_dict)

    return jsonify(all_precip)


@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query Station information
    station_results = session.query(station.station, station.name).all()

    session.close()

    # Create the dictionary
    all_stations = []
    for station_row, name in station_results:
        station_dict = {}
        station_dict["station"] = station_row
        station_dict["name"] = name
        all_stations.append(station_dict)

    # Return the JSON response
    return jsonify(all_stations)


@app.route("/api/v1.0/tobs")
def temperature():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query Station information
    station = 'USC00519281'
    date_o = dt.date(2017, 8, 18) - dt.timedelta(days=365)
    tobs_results = session.query(measurement.tobs, measurement.date).filter(measurement.date > date_o).filter(measurement.station == station).all()

    session.close()

    # Create the dictionary
    USC00519281_temperature = []
    for tobs, date in tobs_results:
        tobs_dict = {}
        tobs_dict["tobs"] = tobs
        tobs_dict["date"] = date
        USC00519281_temperature.append(tobs_dict)

    # Return the JSON response
    return jsonify(USC00519281_temperature)

@app.route("/api/v1.0/start/<start>")
def beginning_time(start):
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query Measurement information
    date_o = dt.date(2017, 8, 18) - dt.timedelta(days=365)
    tobs_results = session.query(func.min(measurement.tobs), func.max(measurement.tobs), func.avg(measurement.tobs))\
        .filter(measurement.date > start).all()

    session.close()

    # Create the list of dictionaries
    start_time_temperature = []
    for min_tobs, max_tobs, avg_tobs in tobs_results:
        tobs_dict = {}
        tobs_dict["min"] = min_tobs
        tobs_dict["max"] = max_tobs
        tobs_dict["avg"] = avg_tobs
        start_time_temperature.append(tobs_dict)

    # Return the JSON response
    return jsonify(start_time_temperature)

@app.route("/api/v1.0/date_range/<start_date>/<final_date>")
def date_range(start_date, final_date):
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query Measurement information
    tobs_results = session.query(func.min(measurement.tobs), func.max(measurement.tobs), func.avg(measurement.tobs))\
        .filter(measurement.date > start_date)\
        .filter(measurement.date < final_date).all()

    session.close()

    # Create the list of dictionaries
    range_temperature = []
    for min_tobs, max_tobs, avg_tobs in tobs_results:
        tobs_dict = {}
        tobs_dict["min"] = min_tobs
        tobs_dict["max"] = max_tobs
        tobs_dict["avg"] = avg_tobs
        range_temperature.append(tobs_dict)

    # Return the JSON response
    return jsonify(range_temperature)

if __name__ == '__main__':
    app.run(debug=True)

