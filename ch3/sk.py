import pyper
import pandas as pd
from matplotlib import pyplot
import numpy as np
from sklearn import linear_model
import sklearn
iris = pd.read_csv("./iris.csv")
iris.info()

setosa = iris[iris["variety"] == "Setosa"]
versicolor = iris[iris["variety"] == "Versicolor"]
virginica = iris[iris["variety"] == "Virginica"]

usedata = np.logical_or(iris["variety"] == "Setosa",
                        iris["variety"] == "Virginica")

setosa_versinica = iris[usedata]
print(setosa_versinica)
X = setosa_versinica[["sepal.length", "sepal.width"]]
Y = setosa_versinica["variety"]

LogRegr = sklearn.linear_model.LogisticRegression(C=1.0)
LogRegr.fit(X, Y)
print(LogRegr.coef_)
print(LogRegr.intercept_)
print(pd.crosstab(Y, LogRegr.predict(X)))

xMin = X['sepal.length'].min()
xMax = X['sepal.length'].max()
yMin = X['sepal.width'].min()
yMax = X['sepal.width'].max()
xx, yy = np.meshgrid(np. arange(xMin, xMax, 0.01), np.arange(yMin, yMax, 0.01))
Z = LogRegr.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

pyplot.figure()
pyplot.xlim(xx.min(), xx.max())
pyplot.ylim(yy.min(), xx.max())

pyplot.scatter(X["sepal.length"].ix[Y.values == 0],
               X["sepal.width"].ix[Y.values == 0], marker="o", c="black")

pyplot.scatter(Y["sepal.length"].ix[Y.values == 1],
               Y["sepal.width"].ix[Y.values == 1], marker="+", c="black")

# 単回帰分析
# LinerRegr = linear_model.LinearRegression()
# X = setosa[['sepal.length']]
# Y = setosa[['sepal.width']]
# LinerRegr.fit(X, Y)
# pyplot.scatter(X, Y, color='black')
# px = np.arange(X.min(), X.max(), .01)[:, np.newaxis]
# py = LinerRegr.predict(px)
# pyplot.plot(px, py, color='blue', linewidth=3)
# pyplot.xlabel('sepal.length')
# pyplot.ylabel('sepal.width')
# pyplot.show()
# print(LinerRegr.coef_)
# print(LinerRegr.intercept_)
# # 決定係数
# print(LinerRegr.score(X, Y))

# LinerRegr = linear_model.LinearRegression()
# X = setosa[['sepal.length', 'petal.length', 'petal.width']]
# Y = setosa[['sepal.width']]
#
# print(LinerRegr.fit(X, Y))
# print(LinerRegr.score(X, Y))
#
# r = pyper.R(use_pandas='True')
# r.assign('data', iris)
# print(r('rlm <- lm(Sepal.Width ~ Sepal.Length + Petal.Length + Petal.Width , data=iris)'))
# print(r('rlm'))
