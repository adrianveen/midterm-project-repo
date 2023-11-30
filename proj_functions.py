from remove_zeros import remove_zeros
from keyword_col_remove import keyword_col_remove
from year_filter import year_filter

#remove 0 gdp values
def remove_null_gdp(df):

    countries_with_zero = [index for index, value in df.groupby('country')['gdp'].count().sort_values().items() if value == 0]
    df = df.loc[~df['country'].isin(countries_with_zero), :]
    
    return df