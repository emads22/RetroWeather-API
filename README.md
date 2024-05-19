# Historical Data Weather API

## Overview
Historical Data Weather API is a Flask application designed to provide weather data from CSV files sourced from the European Climate Assessment & Dataset (ECA&D). It offers endpoints for retrieving weather information based on station IDs and dates. Users can also utilize other resources as long as they replace the data files in the static folder.

## Features
- **Home Page**: Renders a web page displaying station data in HTML format. 
- **Weather API Endpoint**: Retrieves temperature data for a specific station and date.
- **One Station All Years Endpoint**: Retrieves all weather data for a specific station.
- **One Station One Year Endpoint**: Retrieves weather data for a specific station and year.

## Enhanced Homepage Styling
The homepage has undergone styling enhancements, resulting in a more visually appealing and engaging design. With updated color schemes, typography, and layout refinements, the homepage now offers a more attractive and enjoyable browsing experience.

## Setup
1. Clone the repository.
2. Ensure Python 3.x is installed.
3. Install the required dependencies using `pip install -r requirements.txt`.
4. Place your CSV data files in the `assets/data_small` directory. By default, the app expects CSV files from ECA&D.
5. Run the script using `python main.py`.

## Usage
1. Run the script using `python main.py`.
2. Access the home page at the root URL (e.g., `http://localhost:5000/`) to view station data.
3. Utilize the provided API endpoints to retrieve weather data:
   - `/api/v1/<station>/<date>`: Retrieve temperature data for a specific station and date.
   - `/api/v1/station/<station>`: Retrieve all weather data for a specific station.
   - `/api/v1/station/<station>/<year>`: Retrieve weather data for a specific station and year.

## Contributing
Contributions are welcome! Here are some ways you can contribute to the project:
- Report bugs and issues
- Suggest new features or improvements
- Submit pull requests with bug fixes or enhancements

## Author
- Emad &nbsp; E>
  
  [<img src="https://img.shields.io/badge/GitHub-Profile-blue?logo=github" width="150">](https://github.com/emads22)

## License
This project is licensed under the MIT License, which grants permission for free use, modification, distribution, and sublicense of the code, provided that the copyright notice (attributed to [emads22](https://github.com/emads22)) and permission notice are included in all copies or substantial portions of the software. This license is permissive and allows users to utilize the code for both commercial and non-commercial purposes.

Please see the [LICENSE](LICENSE) file for more details.