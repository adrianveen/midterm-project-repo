from remove_zeros import remove_zeros
from keyword_col_names import keyword_col_names
from year_filter import year_filter

#remove 0 gdp values
def remove_null_gdp(df):

    countries_with_zero = [index for index, value in df.groupby('country')['gdp'].count().sort_values().items() if value == 0]
    df = df.loc[~df['country'].isin(countries_with_zero), :]
    
    return df

#iterate through a model and X dataframe to remove variables with high p-values
# one at a time until all variables have a p-value below 0.05
def remove_high_pvalue(model, X):
    while model.pvalues.max() > 0.05:
        p_values = model.pvalues
        p_values = p_values.drop('const')
        p_values = p_values[p_values != p_values.max()]
        p_values = p_values.index.tolist()
        X = X[p_values]
        X = sm.add_constant(X)
        lin_reg = sm.OLS(y, X)
        model = lin_reg.fit()
    return model