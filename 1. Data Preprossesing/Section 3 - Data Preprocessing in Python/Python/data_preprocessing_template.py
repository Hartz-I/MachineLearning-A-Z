#creating the template

#importing libraries
import numpy as np
import matplotlib.pyplot as plt #creates plot
import pandas as pd #to import and manage datasets

#importing the dataset
dataset = pd.read_csv("Data.csv")
X= dataset.iloc[: , :-1].values #row this to that , col this to that. -1 means all but last one
Y= dataset.iloc[: , 3].values #taking 4th column


#Spliting test and train set
from sklearn.model_selection import train_test_split #does the name

X_train , X_test , Y_train , Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0) #splitting the data! easy



#Feature scaling : turning different columns with similar values for calculation purposes and to reduce value high differece
"""
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()

X_train = sc_X.fit_transform(X_train) #for train it is fit and transform
X_test = sc_X.transform(X_test) #for test it's only transform
"""










