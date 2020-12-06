import pandas as pd
from matplotlib import pyplot
import numpy as np

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
# pyplot.figure()
# pyplot.hist(iris["sepal.length"])
# pyplot.xlabel("SepalLength")
# pyplot.ylabel("Freq")
#
# pyplot.show()

# data = [setosa["sepal.length"],
#        versicolor["sepal.length"], virginica["sepal.length"]]
# pyplot.figure()
#pyplot.boxplot(data, sym="k.")
# pyplot.xlabel("Name")
# pyplot.ylabel("sepal.length")
#ax = pyplot.gca()
#pyplot.setp(ax, xticklabels=["setosa", "versicolor", "virginica"])
# pyplot.show()

#pyplot.scatter(setosa["sepal.length"], setosa["sepal.width"])
# pyplot.xlabel("sepal.length")
# pyplot.ylabel("sepal.width")
# pyplot.show()
#
#corr = np.corrcoef(setosa["sepal.length"], setosa["sepal.width"])
#print(corr[0, 1])

pd.plotting.scatter_matrix(setosa)
pyplot.tight_layout()
pyplot.show()
