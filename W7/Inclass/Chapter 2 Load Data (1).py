import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy
import sklearn

# Get the directory where this script is located
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
HOUSING_PATH = os.path.join(SCRIPT_DIR, "housing.csv")

def load_housing_data():
    return pd.read_csv(HOUSING_PATH)


housing = load_housing_data()
housing.info()  #The info method is useful to get a quick description of the data

print(housing["ocean_proximity"].value_counts()) #Shows what categories exist and how many districts belong to each category

print(housing.describe()) #This method shows a summary of the numerical attributes

housing.hist( bins=50, figsize=(14,9)) #shows the number of instances (vertical axis) that have a given value range
plt.show()   #Plots a histogram for each numerical attribute
