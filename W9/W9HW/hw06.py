'''
Weston Guo
ACAD 191, Fall 2025
westongu@usc.edu
Homework 5
'''

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

def load_data(file_path):
    return pd.read_csv(file_path)

goldPrice = load_data("./Gold Price Regression.csv")
goldPrice = goldPrice.dropna()

#goldPrice.info()
#goldPrice.describe()
#goldPrice.hist(bins=50, figsize=(14,9))
#plt.show()

trainSet = goldPrice.sample(frac=0.8, random_state=1001)
testSet = goldPrice.drop(trainSet.index)

#goldPrice.plot.scatter(x="date", y="gold close",figsize=(18,10))
#plt.show()

#since gold price is the target variable, and gold price includes gold open, high, low, close, and volume. we can use the other variable to do the regression, in four times

targetVariable = ["gold open", "gold high", "gold low", "gold close", "gold volume"]
for target in targetVariable:
    correlation = trainSet.drop(["date"] + targetVariable, axis=1).corrwith(trainSet[target])
    print(f"Here is the correlation between {target} and the other variables:")
    print(correlation)
    print("--------------------------------")

#I didn't use corr() function because it only allows one series to be correlated with another series

