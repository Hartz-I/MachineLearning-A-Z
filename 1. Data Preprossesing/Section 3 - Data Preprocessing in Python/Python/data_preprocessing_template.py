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

#handling catagorical data
#converting text to numbers
#a individual number for individual names
from sklearn.preprocessing import LabelEncoder , OneHotEncoder

labelencoder_X = LabelEncoder() #putting the class into variables

X[: , 0] = labelencoder_X.fit_transform(X[: , 0]) #only on first column of X

#we have to create "dummy var" to prevent the computer from thing higher number as higher country somehow!

#onehotencoder = OneHotEncoder(categories=) #on which column
#X = onehotencoder.fit_transform(X).toarray 
#this doesn't work anymore!

#we simply transform the column into that
from sklearn.compose import ColumnTransformer
#name of column , what we are doing , on which column
ct = ColumnTransformer([('Country' , OneHotEncoder() , [0])] , remainder="passthrough")
X = ct.fit_transform(X) #applying the transformation

#we won't have to use the one hot encoder for the Y.
# as it is the dependant variable the model will automatically know it's catagorical!

labelencoder_Y = LabelEncoder() #putting the class into variables

Y = labelencoder_X.fit_transform(Y) #only on first column of Y


#Spliting test and train set
from sklearn.model_selection import train_test_split #does the name

X_train , X_test , Y_train , Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0) #splitting the data! easy















