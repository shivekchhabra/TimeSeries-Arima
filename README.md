## What does the repository contain?
The repository contains a code for Time Series modelling using ARIMA. 
The output is the produced forecasts. However methods for eda,diagnostics and validation have been made and may be uncommented from main to check.

## How to use this repository?
Simply install requirements by doing:
	pip install -r requirements.txt

and run furniture_sales.py

You may use your own dataset and check the prediction.

Original Data:




![alt text](https://github.com/shivekchhabra/TimeSeries-Arima/blob/master/Outputs/Original_data.png)



Model Diagnostics:





![alt text](https://github.com/shivekchhabra/TimeSeries-Arima/blob/master/Outputs/Diagnostics.png)



Validation:





![alt text](https://github.com/shivekchhabra/TimeSeries-Arima/blob/master/Outputs/Validation.png)









Forecasting:





![alt text](https://github.com/shivekchhabra/TimeSeries-Arima/blob/master/Outputs/Forecasts.png)












## Helpful Notes:

### Time Series

- Constant time interval
- Might have a seasonality trend

For coding in python the date column needs to be the index.

### Stationarity in TS

A TS is said to be stationary if statistical properties such as mean,variance remain constant over time. This is helpful in determining the trend overtime.

Hence, the first task is to always stationarise the TS.

For further reference you may check the Dicky Fuller Test/Random Walk test.

### Pandas.resample

Is a method for frequency conversion and resampling of time series. 

### Pandas.date_range

Used to return a fixed frequency of datetime index.

### Arima

p,d,q are the 3 important factors.

Auto Regressive Integrated Moving Average.
If series is already stationary d=0
Else d= minimum number of differencing needed to make the series stationary.

Please note: For Arima it is advisable to use grid search to find the optimum value of p,d,q. This is done by ensuring minimum AIC value. 

Auto Regressive- Means when prediction depends on its own lags.
Moving Average- Is onee where prediction only depends on lagged forecasted erorrs.

Hence, the final equation is of the form:

Predicted= Constant + Linear Combination of Lags + Linear Combination of lagged error forecasts.


### Kurtosis:

Defines the heaviness of distribution tails

(https://corporatefinanceinstitute.com/resources/knowledge/other/kurtosis/)


### Hetroscedasticity:

Refers to the circumstance in which the variability of a variable is unequal across the range of values of a second variable that predicts it.

(http://www.statsmakemecry.com/smmctheblog/confusing-stats-terms-explained-heteroscedasticity-heteroske.html)










Special Thanks to Susan Li for the dataset.
