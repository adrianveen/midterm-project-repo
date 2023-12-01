def keyword_col_names(df, keywords):
    """creates a list of columns based on keywords"""
    
    df = df.copy()

    columns_to_remove = [col for col in df.columns if any(word in col for word in keywords)]

    return columns_to_remove