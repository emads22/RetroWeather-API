from flask import Flask, render_template
import pandas as pd
from pathlib import Path


# Define the directory path for 'data_small' directory within the 'static' folder
DATA_DIR = Path("static") / "data_small"


# Create an instance of the Flask application
app = Flask(__name__)


# Define a route for the home page ("/")
@app.route("/")
def home():
    # Render the template named "home.html" and return it as the response
    return render_template("home.html")


# Define a route for the weather API endpoint
@app.route("/api/v1/<string:station>/<string:date>")
def weather_api(station, date):

    # Construct the file path for the CSV file based on the station ID
    # DATA_DIR is assumed to be a pathlib.Path object representing the directory where the data files are stored
    # The station ID is padded with leading zeros to ensure it has six digits
    filepath = DATA_DIR / f"TG_STAID{str(station).zfill(6)}.txt"

    # Read the CSV file into a DataFrame
    # skiprows=20 skips the first 20 rows of the CSV file, useful if there are header lines or metadata at the beginning
    # parse_dates=["    DATE"] parses the "DATE" column as dates, assuming it's in a specific format
    df = pd.read_csv(filepath, skiprows=20, parse_dates=["    DATE"])

    # Retrieve the temperature for a specific date
    # df['   TG'][df['    DATE'] == date] selects the 'TG' temperature values for rows where the date matches the specified date
    # .squeeze() is used to convert the resulting Series to a scalar value, assuming there's only one matching row
    # Divide by 10 to convert from tenths of a degree Celsius to degrees Celsius
    temperature = df['   TG'][df['    DATE'] == date].squeeze() / 10
    # The temperature variable now contains the temperature in degrees Celsius for the specified date

    # Create a dictionary containing the station, date, and temperature
    weather_data = {
        'station': station,
        'date': date,
        'temperature': temperature
    }
    # Return the weather data as a JSON response
    return weather_data


# If this script is executed directly (not imported as a module), start the Flask application
if __name__ == "__main__":
    # Run the Flask application in debug mode, allowing for debugging information to be displayed
    app.run(debug=True)
