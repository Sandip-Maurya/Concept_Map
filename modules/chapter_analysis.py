# modules/chapter_analysis.py

import pandas as pd

def count_active_chapters(df: pd.DataFrame) -> int:
    """
    Count the number of active chapters.

    Args:
        df (pd.DataFrame): The DataFrame containing the data.

    Returns:
        int: Number of active chapters.
    """
    active_chapters = df[df['chapterStatus'] == 1]['chapterName'].nunique()
    return active_chapters

def get_counts_per_chapter(df: pd.DataFrame) -> pd.DataFrame:
    """
    Get counts of active topics and concepts per chapter within each unit, subject, and exam.

    Args:
        df (pd.DataFrame): The DataFrame containing the data.

    Returns:
        pd.DataFrame: A DataFrame with counts per exam, subject, unit, and chapter.
    """
    # Filter active chapters
    active_df = df[df['chapterStatus'] == 1]

    # Group by Exam, Subject, Unit, and Chapter
    grouped = active_df.groupby(['examName', 'subjectName', 'unitName', 'chapterName'])

    # Aggregate counts
    counts = grouped.agg(
        **{
            'No. of Topics': ('topicName', 'nunique'),
            'No. of Concepts': ('conceptName', 'nunique')
        }
    ).reset_index()

    return counts
