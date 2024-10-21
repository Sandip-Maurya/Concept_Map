# modules/data_loader.py

import pandas as pd

def load_data(filepath: str) -> pd.DataFrame:
    """
    Load the CSV data from the specified filepath.

    Args:
        filepath (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Loaded data as a pandas DataFrame.
    """
    try:
        df = pd.read_csv(filepath)
        return df
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {filepath} does not exist.")
    except pd.errors.ParserError:
        raise ValueError(f"Error parsing the file {filepath}. Please check the CSV format.")
