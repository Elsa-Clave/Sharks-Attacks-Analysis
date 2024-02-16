def clean_rows_w_nulls(df):
    """
    Remove rows from a DataFrame that contain only null values.

    Parameters:
    df (pandas.DataFrame): Input DataFrame.

    Returns:
    pandas.DataFrame: DataFrame with rows containing only null values removed.
    """
    cleaned_df = df.dropna(axis=0, how='all')
    return cleaned_df
