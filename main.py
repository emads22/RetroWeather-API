from flask import Flask, render_template
import pandas as pd
from pathlib import Path


# Define the directory path for 'data_small' directory within the 'static' folder
DATA_DIR = Path("static") / "data_small"


# Create an instance of the Flask application
app = Flask(__name__)

# Define the path to the stations data file
stations_data_path = DATA_DIR / "stations.txt"
# Read the stations data file into a DataFrame, skipping the first 17 rows
stations_df = pd.read_csv(stations_data_path, skiprows=17)
# Select only the columns 'STAID' and 'STANAME' from the DataFrame
stations_df = stations_df[['STAID', 'STANAME                                 ']]

# Define a route for the home page ("/")
@app.route("/")
def home():
    # Render the template named "home.html" with the variable `stations_data` and return it as the response
    return render_template("home.html", stations_data=stations_df.to_html())    # Convert the stations DataFrame to HTML format


# Define a route for the weather API endpoint
@app.route("/api/v1/<string:station>/<string:date>")
def weather_api_default(station, date):

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


@app.route("/api/v1/station/<string:station>")
def one_station_all_years(station):
    # Construct the file path for the station data file using the station ID
    station_filepath = DATA_DIR / f"TG_STAID{str(station).zfill(6)}.txt"
    # Read the station data from the CSV file, skipping the first 20 rows and parsing the 'DATE' column as dates
    station_df = pd.read_csv(station_filepath, skiprows=20, parse_dates=["    DATE"])

    # Convert the DataFrame to a list of dictionaries, each representing a record,
    # using the 'records' orientation
    return station_df.to_dict(orient='records')

@app.route("/api/v1/station/<string:station>/<string:year>")
def one_station_one_year(station, year):
    # Construct the file path for the station data file using the station ID
    station_filepath = DATA_DIR / f"TG_STAID{str(station).zfill(6)}.txt"
    # Read the station data from the CSV file, skipping the first 20 rows and parsing the 'DATE' column as dates
    station_df = pd.read_csv(station_filepath, skiprows=20, parse_dates=["    DATE"])
    
    # Convert the '    DATE' column to datetime format if it's not already in datetime format
    # Filter the DataFrame to include only rows where the year component of the '    DATE' column matches the specified year
    # station_df['    DATE'].str.startswith(year) won't work is because .str.startswith() is a string method and can only be used on columns containing string data, and station_df['    DATE'] is a datetime column, not a string column. 
    station_df = station_df.loc[station_df['    DATE'].dt.year == int(year)] 

    # Convert the DataFrame to a list of dictionaries, each representing a record,
    # using the 'records' orientation
    return station_df.to_dict(orient='records')

def extract_specific_line_from_txt(file_path, line_number):
    """
    Extracts a specific line from a text file.

    Args:
        file_path (str): The path to the text file.
        line_number (int): The index of the line to extract (0-based indexing).

    Returns:
        str: The specific line extracted from the file.
    """

    # Open the text file
    with open(file_path, 'r') as file:
        # Read all lines into a list
        lines = file.readlines()        
        # Check if the line number is within the range of lines
        if line_number < 0 or line_number >= len(lines):
            raise ValueError("\nLine number is out of range.\n")        
        # Extract the specific line
        specific_line = lines[line_number]
    return specific_line


# If this script is executed directly (not imported as a module), start the Flask application
if __name__ == "__main__":
    # Run the Flask application in debug mode, allowing for debugging information to be displayed
    app.run(debug=True)
