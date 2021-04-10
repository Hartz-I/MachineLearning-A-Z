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
