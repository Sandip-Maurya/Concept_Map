# app.py

import streamlit as st
import pandas as pd
from modules.subject_analysis import count_active_subjects, get_counts_per_subject
from modules.unit_analysis import count_active_units, get_counts_per_unit
from modules.chapter_analysis import count_active_chapters, get_counts_per_chapter
from modules.topic_analysis import count_active_topics, get_counts_per_topic
from utils.helpers import display_table, validate_columns, download_button

# -----------------------------
# 1. Streamlit Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Concept and Topic Map",
    layout="wide",
    initial_sidebar_state="collapsed"  # Sidebar is collapsed since we're focusing on main content
)

# -----------------------------
# 2. Custom CSS for Styling
# -----------------------------
st.markdown("""
<style>
/* Reduce margin between headers and content */
h1, h2, h3, h4, h5, h6 {
    margin-bottom: 0.5rem;
}

/* Reduce margin between sections */
.block-container > div {
    padding-top: 0.5rem;
    padding-bottom: 0.5rem;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# 3. Page Title
# -----------------------------
st.markdown("<h1 style='text-align: center;'>Concept and Topic Map</h1>", unsafe_allow_html=True)

# -----------------------------
# 4. Data Loading
# -----------------------------
@st.cache_data
def load_map_data():
    filepath = "data/map_data.csv"
    return pd.read_csv(filepath)

try:
    data = load_map_data()
except Exception as e:
    st.error(f"Error loading data: {e}")
    st.stop()

# -----------------------------
# 5. Data Validation
# -----------------------------
required_columns = [
    'examName', 'subjectName', 'unitName', 'chapterName', 'topicName', 'conceptName',
    'examStatus', 'subjectStatus', 'unitStatus', 'chapterStatus', 'topicStatus', 'conceptStatus',
    'examId', 'subjectId', 'unitId', 'chapterId', 'topicId', 'conceptId'
]

try:
    validate_columns(data, required_columns)
except ValueError as ve:
    st.error(str(ve))
    st.stop()

# -----------------------------
# 6. Section 1: Counts Data Per Exam
# -----------------------------
st.header("1. Counts Data Per Exam")

try:
    # Initialize list to store counts per exam
    counts_list_exam = []

    # Get unique exams
    exams = data['examName'].unique()

    # Iterate over each exam and calculate counts
    for exam in exams:
        exam_data = data[data['examName'] == exam]
        
        active_subjects = count_active_subjects(exam_data)
        active_units = count_active_units(exam_data)
        active_chapters = count_active_chapters(exam_data)
        active_topics = count_active_topics(exam_data)
        active_concepts = exam_data[exam_data['conceptStatus'] == 1]['conceptName'].nunique()
        
        counts_list_exam.append({
            'Exam': exam,
            'No. of Subjects': active_subjects,
            'No. of Units': active_units,
            'No. of Chapters': active_chapters,
            'No. of Topics': active_topics,
            'No. of Concepts': active_concepts
        })

    # Create DataFrame from counts_list_exam
    counts_df_exam = pd.DataFrame(counts_list_exam)
    
    st.dataframe(counts_df_exam)

except Exception as e:
    st.error(f"Error in Counts Data Per Exam: {e}")

# -----------------------------
# 7. Section 2: Counts Data Per Subject
# -----------------------------
st.header("2. Counts Data Per Subject")

try:
    # Get counts per subject
    counts_df_subject = get_counts_per_subject(data)

    # Reorder and rename columns for clarity
    counts_df_subject = counts_df_subject[['examName', 'subjectName', 'No. of Units', 'No. of Chapters', 'No. of Topics', 'No. of Concepts']]
    counts_df_subject.rename(columns={
        'examName': 'Exam',
        'subjectName': 'Subject'
    }, inplace=True)

    st.dataframe(counts_df_subject)

except Exception as e:
    st.error(f"Error in Counts Data Per Subject: {e}")

# -----------------------------
# 8. Section 3: Counts Data Per Unit
# -----------------------------
st.header("3. Counts Data Per Unit")

try:
    # Get counts per unit
    counts_df_unit = get_counts_per_unit(data)

    # Reorder and rename columns for clarity
    counts_df_unit = counts_df_unit[['examName', 'subjectName', 'unitName', 'No. of Chapters', 'No. of Topics', 'No. of Concepts']]
    counts_df_unit.rename(columns={
        'examName': 'Exam',
        'subjectName': 'Subject',
        'unitName': 'Unit'
    }, inplace=True)

    st.dataframe(counts_df_unit)

except Exception as e:
    st.error(f"Error in Counts Data Per Unit: {e}")

# -----------------------------
# 9. Section 4: Counts Data Per Chapter
# -----------------------------
st.header("4. Counts Data Per Chapter")

try:
    # Get counts per chapter
    counts_df_chapter = get_counts_per_chapter(data)

    # Reorder and rename columns for clarity
    counts_df_chapter = counts_df_chapter[['examName', 'subjectName', 'unitName', 'chapterName', 'No. of Topics', 'No. of Concepts']]
    counts_df_chapter.rename(columns={
        'examName': 'Exam',
        'subjectName': 'Subject',
        'unitName': 'Unit',
        'chapterName': 'Chapter'
    }, inplace=True)

    st.dataframe(counts_df_chapter)

except Exception as e:
    st.error(f"Error in Counts Data Per Chapter: {e}")

# -----------------------------
# 10. Section 5: Counts Data Per Topic
# -----------------------------
st.header("5. Counts Data Per Topic")

try:
    # Get counts per topic
    counts_df_topic = get_counts_per_topic(data)

    # Reorder and rename columns for clarity
    counts_df_topic = counts_df_topic[['examName', 'subjectName', 'unitName', 'chapterName', 'topicName', 'No. of Concepts']]
    counts_df_topic.rename(columns={
        'examName': 'Exam',
        'subjectName': 'Subject',
        'unitName': 'Unit',
        'chapterName': 'Chapter',
        'topicName': 'Topic'
    }, inplace=True)

    st.dataframe(counts_df_topic)

except Exception as e:
    st.error(f"Error in Counts Data Per Topic: {e}")

# -----------------------------
# 11. Section 6: Data Preview
# -----------------------------
st.header("6. Complete JEE Main and NEET Data with Status and ID")

try:
    st.dataframe(data)

except Exception as e:
    st.error(f"Error in Data Preview: {e}")
