# WeatherTweet

WeatherTweet is a Flask-based web application that allows users to post tweets with their current location and the current weather information. Users can also view tweets posted by other users within a certain radius of their current location.

## Prerequisites
- Python 3.7 or higher
- PostgreSQL 10 or higher with PostGIS extension

## Language and Frameworks

- Python - 3.10
- Flask - 2.2
- Flask-SQLAlchemy==3.0.3

## Getting Started

1. Clone this repository to your local machine.
2. Install the required dependencies using pip install -r requirements.txt.
3. Set up the database:
    - Create a new database in PostgreSQL: `CREATE DATABASE weathertweets`
    - Enable the PostGIS extension in the database: `CREATE EXTENSION postgis`
4. Run the application using `python run.py`.
5. The API will now be running on http://localhost:5000.
