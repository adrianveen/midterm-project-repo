def remove_zeros(df, cols):
    """Removes rows with zero values in the specified columns."""
    
    df = df.copy()
    for col in cols:
        df = df.loc[df[col] != 0, :]
    return df