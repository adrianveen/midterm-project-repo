# midterm-project-repo
Midterm project for Lighthouse Labs Data Science bootcamp

## Goals 

The goal of this project was to develop forecasting for trends in energy consumption and production, based on variables 
defined at a national level. We would do this by perfoming data cleaning and EDA on the dataset offered at
[Kaggle.com](https://www.kaggle.com/datasets/pralabhpoudel/world-energy-consumption?select=World+Energy+Consumption.csv)
and then use regressions and Tableau to create models that will allow us to explain and forecast these trends.

## Process

### 1. Data Cleaning
- A lot of the data did not exist before certain times periods or was not complete and was removed
- The data also included many regions that had census data from various organizations. This was extracted in the case we may use it but was not used for this project
- There were also many countries that no longer existed (e.g. Yugoslavia) and these were removed as the data was incomplete for them
- A significant number of null/zero values were found for various columns. If they did not benefit the model, they were removed.

### 2. Exploratory Data Analysis + Modeling
- First we used descriptive statistics, correlation heatmaps and pairplots to see what relationships may be found
- Many variables had high correlations between each other
	- regression modelling was used to further investigate these relationships
- A significant amount of the data was shown to have correlations and high R-squared values but low Durbin-Watson values leading to these models most likely having high colinearity or autocorrelation
- The models were not added directly to the dashboard but they did influence which visualizations were used in the final product

### 3. Dashboard
- Based on the modeling and EDA performed, 6 different graphs were added to the Tableau dashboard
- These charts model relationships such as how the gdp correlates with emissions of a given country or how the consumption of energy changes over time with a forecast
- The goal of the dashboard is to demonstrate trends in energy consumption by individual energy sources, as well as groups of energy sources. 
	- Through this, we would hope to be able to identify trends that would help estimate the makeup of different countries or regions energy production and consumption


## Results

Regression Models:
- Nearly all models with high R-squared values or correlations were highly colinear
- Some models were used to predict values outside of the source data but were not very reliable due to the collinearity or autocorrelation
- With additional data, this can potentially lead to better fitting models
 	- for example, we may expect to see a decrease in oil per capita over the years and an increase in renewables as a direct results of changing opinions on fossil fuels and the increased awareness of global warming

Dashboard:
- In the heatmap we see that generally colder places use more energy. This is most likely due to heating. 
	- Outliers here are Canada, Norway, Iceland and the US which can be attributed to the cold climates of the first 3 and the extensive vehicle usage due to distances in Canada and the US
- The % Change in use per energy source shows us that renewables are still increasing(although not exponentially), while fossil fuels are decreasing in their share of the total energy consumption
	- This is corroborated by the Energy Forecast which shows that the energy consumption per capita has been increasing for lower carbon sources, while coal and oil are descreasing or stagnating
	- Interestingly gas consumption has gone up
- GDP vs Emissions shows that as the gdp per capita of a country increase there will be an increase in the emissions per capita for that country
- The Consumption Per Capita graph and the Energy Consumption graph both give breakdowns as to how much of each energy source is being consumed in certain countries and globally

## Challenges

The data sets extreme size (127 columns) made it extremely unwieldy and difficult to focus in on certain aspects of the data. If we wanted to look at a heatmap or a pairplot we would need to truncate the values to create a more feasible data set. This combined with the many holes as well data that made cleaning the data quite difficult as well as modeling.

The data was a combination of different values. The countries column for example had regions, and regions from different data sources, as well as items like "low income countries" or "G20". this required some additional filtering, and removal of null values. 

There were many null values that were not converted to zeros, but with more time should have been. Some examples of these are the energy source production, consumption and other values, that traced back to 1965. For instance, many countries did not have renewable energy sources contributing to their overall production, but these values should be set to 0 instead of NaN or Null. 

One issue that was a significant setback was within tableaul. In order to create visuals that were wanted, one solution was to create a pivot. Without careful pivoting however, row duplicates were created. This was not realized until the dashboard was nearly done, which required that it was to be remade manually. The end product of the second dashboard was much better however. 

## Future Goals

Data:
- Many missing values from many columns
	- Could have looked for census information that could be inserted into the data to remove the missing values
	- Use data from countries that no longer exist to supplement existing country data (i.e. Yugoslavia to Serbia, Croatia, Bosnia etc.)
- The data included regions within which were ignored. These could be used to give insight into how different regions compare in their energy source usage(e.g. Americas vs Africa)

Modeling:
- While some modeling was included in the final dashboard, higher degree polynomial regression models could have been used to draw further conclusions
- There were some multi-variate regression models completed, but without data outside of population, gdp, and location, it was difficult to draw any concrete conclusions. 

Dashboard:
- Creating visualizations that showed percentages proved difficult, due to the organization of the dataset. With foresight during the cleaning and EDA stages, we may have been able to circumvent this. 


