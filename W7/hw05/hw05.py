'''
Weston Guo
ACAD 191, Fall 2025
westongu@usc.edu
Homework 5
'''

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def load_data(file_path):
    return pd.read_csv(file_path)

goldPrice = load_data("./Gold Price Regression.csv")

goldPrice.info()
goldPrice.describe()
goldPrice.hist(bins=50, figsize=(14,9))
plt.show()

