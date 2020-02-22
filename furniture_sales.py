import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
import statsmodels.api as sm
import matplotlib

# matplotlib.use('TkAgg')
warnings.filterwarnings('ignore')
matplotlib.rcParams['axes.labelsize'] = 14
matplotlib.rcParams['xtick.labelsize'] = 12
matplotlib.rcParams['ytick.labelsize'] = 12
matplotlib.rcParams['text.color'] = 'k'


# Generalised function to read excel file
def read_xlx(filename, sheet_name):
    xl = pd.ExcelFile(filename)
    df = pd.read_excel(xl, sheet_name)
    return df


# Filtering data according to a category
def filtering_category(df, category):
    data = df.loc[df['Category'] == category].copy()
    return data


# Basic Preprocessing
def preproc(df):
    df.drop_duplicates(keep='first', inplace=True)
    df.reset_index(drop=True, inplace=True)
    return df


# Fitting arima model (p=d=q=1)
def arima_model(df):
    mod = sm.tsa.statespace.SARIMAX(df,
                                    order=(1, 1, 1),
                                    seasonal_order=(1, 1, 0, 12),
                                    enforce_stationarity=False,
                                    enforce_invertibility=False)
    results = mod.fit()
    print(results.summary())
    return results


# Done to organise data in regular intervals
def resampling_furniture(furniture):
    furniture = furniture.groupby('Order Date')['Sales'].sum().reset_index()
    furniture = furniture.set_index('Order Date')
    y = furniture['Sales'].resample('MS').mean()
    return y


# Checking the normality of the model
def diagnostics(results):
    results.plot_diagnostics(figsize=(16, 8))
    plt.show()


# Plotting the dataframe
def eda(df):
    df.plot(figsize=(15, 6))
    plt.show()


# Validating the model
def validating_results(df, results):
    pred = results.get_prediction(start=pd.to_datetime('2017-01-01'), dynamic=False)
    pred_ci = pred.conf_int()
    ax = df.plot(label='observed')
    pred.predicted_mean.plot(ax=ax, label='Forecast', alpha=.7, figsize=(14, 7))
    ax.fill_between(pred_ci.index,
                    pred_ci.iloc[:, 0],
                    pred_ci.iloc[:, 1], color='k', alpha=.2)  # For filling the predicted region. Can be commented.
    ax.set_xlabel('Date')
    ax.set_ylabel('Furniture Sales')
    plt.legend()
    plt.show()


# Checking mse,rmse and error % about mean.
def error_analysis(forecasted_val, true_val):
    error = ((forecasted_val - true_val) ** 2).mean()
    print('----------------------------------------------------------------------------------------------------------')
    print('The mean squared error is {}'.format(round(error, 2)))
    print('The root mean square error is {}'.format(round(np.sqrt(error), 2)))
    print('The error percent is approx- {}%'.format(
        abs((forecasted_val.mean() - true_val.mean()) / true_val.mean()) * 100))
    print('----------------------------------------------------------------------------------------------------------')


# Producing future forecasts
def produce_forecasts(df, results):
    pred = results.get_forecast(steps=100)
    print('Predicted Values:')
    print(pred.predicted_mean)
    print('----------------------------------------------------------------------------------------------------------')
    pred_ci = pred.conf_int()
    ax = df.plot(label='Observed', figsize=(14, 7))
    pred.predicted_mean.plot(ax=ax, label='Forecast')
    ax.fill_between(pred_ci.index,
                    pred_ci.iloc[:, 0],
                    pred_ci.iloc[:, 1], color='k', alpha=.25)
    ax.set_xlabel('Date')
    ax.set_ylabel('Furniture Sales')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    df = read_xlx('Sample - Superstore.xls', 'Orders')
    df = filtering_category(df, 'Furniture')
    df = preproc(df)
    df = resampling_furniture(df)
    results = arima_model(df)
    pred = results.get_prediction(start=pd.to_datetime('2017-01-01'), dynamic=False)
    forecasted_val = pred.predicted_mean
    true_val = df['2017-01-01':]
    error_analysis(forecasted_val, true_val)
    # eda(df)
    # diagnostics(results)
    # validating_results(df,results)
    produce_forecasts(df, results)
