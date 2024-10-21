# modules/subject_analysis.py

import pandas as pd

def count_active_subjects(df: pd.DataFrame) -> int:
    """
    Count the number of active subjects.

    Args:
        df (pd.DataFrame): The DataFrame containing the data.

    Returns:
        int: Number of active subjects.
    """
    active_subjects = df[df['subjectStatus'] == 1]['subjectName'].nunique()
    return active_subjects

def get_counts_per_subject(df: pd.DataFrame) -> pd.DataFrame:
    """
    Get counts of active units, chapters, topics, and concepts per subject within each exam.

    Args:
        df (pd.DataFrame): The DataFrame containing the data.

    Returns:
        pd.DataFrame: A DataFrame with counts per exam and subject.
    """
    # Filter active subjects
    active_df = df[df['subjectStatus'] == 1]

    # Group by Exam and Subject
    grouped = active_df.groupby(['examName', 'subjectName'])

    # Aggregate counts
    counts = grouped.agg(
        **{
            'No. of Units': ('unitName', 'nunique'),
            'No. of Chapters': ('chapterName', 'nunique'),
            'No. of Topics': ('topicName', 'nunique'),
            'No. of Concepts': ('conceptName', 'nunique')
        }
    ).reset_index()

    return counts
