# modules/unit_analysis.py

import pandas as pd

def count_active_units(df: pd.DataFrame) -> int:
    """
    Count the number of active units.

    Args:
        df (pd.DataFrame): The DataFrame containing the data.

    Returns:
        int: Number of active units.
    """
    active_units = df[df['unitStatus'] == 1]['unitName'].nunique()
    return active_units

def get_counts_per_unit(df: pd.DataFrame) -> pd.DataFrame:
    """
    Get counts of active chapters, topics, and concepts per unit within each subject and exam.

    Args:
        df (pd.DataFrame): The DataFrame containing the data.

    Returns:
        pd.DataFrame: A DataFrame with counts per exam, subject, and unit.
    """
    # Filter active units
    active_df = df[df['unitStatus'] == 1]

    # Group by Exam, Subject, and Unit
    grouped = active_df.groupby(['examName', 'subjectName', 'unitName'])

    # Aggregate counts
    counts = grouped.agg(
        **{
            'No. of Chapters': ('chapterName', 'nunique'),
            'No. of Topics': ('topicName', 'nunique'),
            'No. of Concepts': ('conceptName', 'nunique')
        }
    ).reset_index()

    return counts
