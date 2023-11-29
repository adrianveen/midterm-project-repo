def keyword_col_remove(df, to_remove):
    """Removes columns with the specified keywords."""
    
    df = df.copy()

    columns_to_remove = [col for col in df.columns if any(word in col for word in to_remove)]

    df = df.drop(columns_to_remove, axis=1)

    return df