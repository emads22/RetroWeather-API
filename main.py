from flask import Flask, render_template


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
    # Mock temperature value for demonstration purposes
    temperature = 23
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
