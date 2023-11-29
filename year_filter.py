
def year_filter(df, year1, year2):
    """Filters the dataframe to include only rows with year values between year1 and year2."""
    
    df = df.copy()
    df = df.loc[(df['year'] >= year1) & (df['year'] <= year2), :]
    return df