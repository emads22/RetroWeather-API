import pandas as pd


def get_dataframe(stations_data_path):
    """
    Reads the stations data from a specified file and returns a DataFrame with
    selected columns.

    Parameters:
    stations_data_path (str): The file path to the stations data CSV file.

    Returns:
    pd.DataFrame: A DataFrame containing the 'STAID' and 'STANAME' columns from
                  the input file.
    """
    # Read the stations data file into a DataFrame, skipping the first 17 rows
    df = pd.read_csv(stations_data_path, skiprows=17)

    # Select only the columns 'STAID' and 'STANAME' from the DataFrame
    df = df[['STAID', 'STANAME                                 ']]

    return df


def format_stations_dataframe(stations_df):
    """
    Converts a DataFrame to an HTML table with Bootstrap classes and additional
    formatting for improved styling.

    Parameters:
    stations_df (pd.DataFrame): The DataFrame containing station data.

    Returns:
    str: A string of HTML representing the formatted table.
    """
    # Convert DataFrame to HTML without the index
    stations_html_table = stations_df.to_html(index=False)

    # Replace default HTML table attributes with Bootstrap table classes
    stations_html_table = stations_html_table.replace(
        '<table border="1" class="dataframe">',
        '<table class="table table-striped table-hover">'
    )

    # Add scope attribute to table headers for better accessibility
    stations_html_table = stations_html_table.replace(
        '<th>',
        '<th scope="col">'
    )

    # Align table row text to the left
    stations_html_table = stations_html_table.replace(
        '<tr style="text-align: right;">',
        '<tr style="text-align: left;">'
    )

    return stations_html_table
