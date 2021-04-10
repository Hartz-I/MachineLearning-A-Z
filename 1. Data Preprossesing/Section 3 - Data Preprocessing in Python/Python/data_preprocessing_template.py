#data preprocessing

#importing libraries
import numpy as np
import matplotlib.pyplot as plt #creates plot
import pandas as pd #to import and manage datasets

#importing the dataset
#this has to be in the same folder with dataset to that folder be working directory

dataset = pd.read_csv("Data.csv")
X= dataset.iloc[: , :-1].values #row this to that , col this to that. -1 means all but last one
Y= dataset.iloc[: , 3].values #taking 4th column

#handling missing data
#take the mean of the columns put on missing place

#what missing values are we working with, what to do with them , 0=column mean and 1=row mean but axis not needed column automatic
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values = np.nan , strategy = 'mean') #instead of what was said
#has to be np.nan

imputer = imputer.fit(X[: , 1:3]) #fitting into all the rows and 2nd and 3rd column . 3 cuz upper bound excluded

X[: , 1:3] = imputer.transform(X[: , 1:3]) #replacing the column with mean encluded columns

