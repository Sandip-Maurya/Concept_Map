# utils/helpers.py

import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder
import streamlit as st

def display_table(df: pd.DataFrame, title: str, use_full_width: bool = True):
    """
    Display a DataFrame with numbering using AgGrid.

    Args:
        df (pd.DataFrame): DataFrame to display.
        title (str): Title of the table.
        use_full_width (bool): If True, table spans the full width of the container.
                               If False, table width adjusts to content.
    """
    st.subheader(title)
    
    # Add numbering column starting from 1
    df_display = df.copy()
    df_display.insert(0, 'No.', range(1, len(df_display) + 1))
    
    # Configure AgGrid options
    gb = GridOptionsBuilder.from_dataframe(df_display)
    gb.configure_pagination(paginationAutoPageSize=True)  # Enable pagination
    gb.configure_default_column(filter=True, sortable=True, resizable=True)  # Enable sorting and filtering
    gb.configure_grid_options(domLayout='autoHeight')  # Adjust grid height based on content
    
    # Set columns to fit content
    gb.configure_columns(columns=df_display.columns.tolist(), auto_size_columns=True)
    
    grid_options = gb.build()
    
    # Display AgGrid within a container
    AgGrid(
        df_display,
        gridOptions=grid_options,
        enable_enterprise_modules=True,
        allow_unsafe_jscode=True,
        theme='streamlit',  # Optional: Set a theme
        height=None,  # Let AgGrid handle the height
        fit_columns_on_grid_load=True,  # Automatically fit columns
    )

def validate_columns(df: pd.DataFrame, required_columns: list):
    """
    Validate that all required columns are present in the DataFrame.

    Args:
        df (pd.DataFrame): The DataFrame to validate.
        required_columns (list): List of required column names.

    Raises:
        ValueError: If any required columns are missing.
    """
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Missing columns in data: {missing_columns}")

def download_button(df: pd.DataFrame, filename: str, label: str = "Download CSV"):
    """
    Provides a download button for a DataFrame.

    Args:
        df (pd.DataFrame): DataFrame to download.
        filename (str): Name of the downloaded file.
        label (str): Label for the download button.
    """
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label=label,
        data=csv,
        file_name=filename,
        mime='text/csv',
    )
