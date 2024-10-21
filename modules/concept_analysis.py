# modules/concept_analysis.py

import pandas as pd

def count_active_concepts(df: pd.DataFrame) -> int:
    """
    Count the number of active concepts.

    Args:
        df (pd.DataFrame): The DataFrame containing the data.

    Returns:
        int: Number of active concepts.
    """
    active_concepts = df[df['conceptStatus'] == 1]['conceptId'].nunique()
    return active_concepts
