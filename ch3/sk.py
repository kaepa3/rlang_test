import pandas as pd
from matplotlib import pyplot
import numpy as np
from sklearn import linear_model

iris = pd.read_csv("./iris.csv")
iris.info()

setosa = iris[iris["variety"] == "Setosa"]
versicolor = iris[iris["variety"] == "Versicolor"]
virginica = iris[iris[
    "variety"] == "Virginica"]

print(setosa.sum())
print("-------------------")

print(iris.groupby("variety").mean())

print("-------------------")

LinerRegr = linear_model.LinearRegression()
X = setosa["sepal.length"]
Y = setosa["sepal.width"]
LinerRegr.fit(X, Y)

pyplot.scatter(X, Y, color="black")
px = np.arrange(X.min(), X.max, .01)[:, np.newaxis]
py = LinerRegr.predict(px)
pyplot.xlabel("sepal.length")
pyplot.ylabel("sepal.width")
pyplot.show()

print(LinerRegr.coef_)
print(LinerRegr.intercept_)
