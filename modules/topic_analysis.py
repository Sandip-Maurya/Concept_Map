# modules/topic_analysis.py

import pandas as pd

def count_active_topics(df: pd.DataFrame) -> int:
    """
    Count the number of active topics.

    Args:
        df (pd.DataFrame): The DataFrame containing the data.

    Returns:
        int: Number of active topics.
    """
    active_topics = df[df['topicStatus'] == 1]['topicName'].nunique()
    return active_topics

def get_counts_per_topic(df: pd.DataFrame) -> pd.DataFrame:
    """
    Get counts of active concepts per topic within each chapter, unit, subject, and exam.

    Args:
        df (pd.DataFrame): The DataFrame containing the data.

    Returns:
        pd.DataFrame: A DataFrame with counts per exam, subject, unit, chapter, and topic.
    """
    # Filter active topics
    active_df = df[df['topicStatus'] == 1]

    # Group by Exam, Subject, Unit, Chapter, and Topic
    grouped = active_df.groupby(['examName', 'subjectName', 'unitName', 'chapterName', 'topicName'])

    # Aggregate counts
    counts = grouped.agg(
        **{
            'No. of Concepts': ('conceptName', 'nunique')
        }
    ).reset_index()

    return counts
