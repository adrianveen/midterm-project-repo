# midterm-project-repo
Midterm project for Lighthouse Labs Data Science bootcamp

## Goals 

The goal of this project was to develop forecasting for trends in energy consumption and production, based on variables 
defined at a national level. We would do this by perfoming data cleaning and EDA on the dataset offered at
https://www.kaggle.com/datasets/pralabhpoudel/world-energy-consumption?select=World+Energy+Consumption.csv 
and then use regressions and Tableau to create models that will allow us to explain and forecast these trends.

## Process

### 1. Data Cleaning
- A lot of the data did not exist before certain times periods or was not complete and was removed
- The data also included many regions that had census data from various organizations. This was extracted in the case we may use it but was not used for this project
- There were also many countries that no longer existed(e.g. Yugoslavia) and these were removed as the data was incomplete for them
- A significant amount of null/zero values were found as well for various columns when it would not make sense to have them. These were removed to not influence the models.

### 2. Exploratory Data Analysis + Modeling
- First we used descriptive statistics, correlation heatmaps and pairplots to see what relationships may be found
- Many variables had high correlations between each other so next step was the use of regression modeling to further describe these relationships
- A significant amount of the data was shown to have correlations and high R-squared values but low Durbin-Watson values leading to these models most likely having high colinearity
- Many of these models did not directly make it into the dashboard but they did influence our choice in sheets

### 3. Dashboard
- Based on the modeling and EDA we created 6 different graphs in Tableau for our dashboard
- These graphs model a variety of things such as how gdp of countries correlates with emissions and how the consumption of energy changes over time with a forecast
- The idea behind the dashboard is to show the ways in which energy source consumption is changing as well as the make up of modern(and past) energy consumption


## Results

Regression Models:
- Nearly all models with high R-squared values or correlations were highly colinear
- Some models were used to predict values past the data but were not very reliable due to the above point
- With outside knowledge this can still lead to good models as for the decrease in oil per capita over the years and the increase in renewables is directly the results of changing opinions on fossil fuels and the increased knowledge of global warming pushing for more sustainable energy

Dashboard:
- In the heatmap we see that generally colder places use more energy. This is most likely due to heating. 
	- Outliers here are Canada, Norway, Iceland and the US which can be attributed to the cold climates of the first 3 and the extensive vehicle usage due to distances in Canada and the US
- The % Change in use per energy source shows us that renewables are still increasing(although not exponentially) while fossil fuels are decreasing in how much they are used
	- This is corroborated by the Energy Forecast which shows that the energy consumption per capita(and therefore the production to meet the demand) have been increasing for green sources while for coal and oil they are falling or stagnating
	- Interestingly gas consumption has gone up
- GDP vs Emissions generally shows that as the gdp per capita of a country increase there will be an increase in the greenhouse emissions of the country
- The Consumption Per Capita graph and the Energy Consumption are graph both give breakdowns as to how and which energy sources are being consumed in certain countries and the world

## Challenges

The data sets extreme size (127 columns) made it extremely unwieldy and difficult to focus in on certain aspects of the data. If we wanted to look at a heatmap or a pairplot we would need to truncate the values to create a more feasible
data set. This combined with the many holes as well data that made cleaning the data quite difficult as well as modeling.

## Future Goals

Data:
- Many missing values from many columns
	- Could have looked for census information that could be inserted into the data to remove the missing values
	- Use data from countries that no longer exist to supplement existing country data (i.e. Yugoslavia to Serbia, Croatia, Bosnia etc.)
- The data included regions within which were ignored. These could be used to give insight into how different regions compare in their energy source usage(e.g. Americas vs Africa)

Modeling:
- While some modeling was included in the final dashboard there could have been room for using higher degree polynomial regression models to fit to the data 
- There was a small amount of multi-variate regression but this could have been done for more data to see if there were relationships which were not as obvious

Dashboard:
- We wanted to create a bar that showed exact percentages of how much each energy source was used as a percentage but were unable to implement it


