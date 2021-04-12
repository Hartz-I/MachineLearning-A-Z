#Data preprocessing

#importing dataset
dataset = read.csv('Data.csv') #must be single quote #added data into dataset variable
# dataset = dataset[, 2:3]

#Splitting dataset into train and test set
#install.packages('caTools')

library(caTools) #or just click on packages

set.seed(123) #setting seed any number. same number gives same split

split = sample.split(dataset$Purchased , SplitRatio = 0.8) #dividing
training_set = subset(dataset , split == TRUE) #take the element if in TRUE position
test_set = subset(dataset , split == FALSE)

#feature scaling
# training_set[, 2:3] = scale(training_set[, 2:3])
# test_set[, 2:3] = scale(test_set[, 2:3])


