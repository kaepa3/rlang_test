library(C50)

library(C50)
demo(package = "C50")
?C5.0
data(churn)

nstadata(mlc_churn)
treeModel <- C5.0(x = churnTrain[,-20], y = churnTrain$churn)
summary(treeModel)