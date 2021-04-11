#Data preprocessing

#importing dataset
dataset = read.csv('Data.csv') #must be single quote #added data into dataset variable

#ifelse(condtion, if true, if false)
dataset$Age = ifelse(is.na(dataset$Age),
                     ave(dataset$Age, FUN = function(x) mean(x, na.rm = TRUE)), #replacing with mean
                     dataset$Age)

dataset$Salary = ifelse(is.na(dataset$Salary),
                     ave(dataset$Salary, FUN = function(x) mean(x, na.rm = TRUE)), #replacing with mean
                     dataset$Salary)

#handling catagorical data
#replacing them with numbers
dataset$Country = factor(dataset$Country ,
                         levels = c('France' , 'Spain' , 'Germany'),
                         labels = c(1,2,3)
                         )

dataset$Purchased = factor(dataset$Purchased ,
                         levels = c('Yes' , 'No'),
                         labels = c(1 , 0)
                         )

#Splitting dataset into train and test set
#install.packages('caTools')

library(caTools) #or just click on packages

set.seed(123) #setting seed any number. same number gives same split

split = sample.split(dataset$Purchased , SplitRatio = 0.8) #dividing
training_set = subset(dataset , split == TRUE) #take the element if in TRUE position
test_set = subset(dataset , split == FALSE)

#feature scaling
training_set[, 2:3] = scale(training_set[, 2:3])
test_set[, 2:3] = scale(test_set[, 2:3])


