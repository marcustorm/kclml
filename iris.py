# Github link
# https://github.com/marcustorm/kclml/blob/master/iris.py

import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
import sklearn

url = "http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ["sepal-length", "sepal-width", "petal-length", "petal-width", "class"]

# import the data from the web
dataset = pandas.read_csv(url, names=names)

# what are the dimensions of the data?
# print("Dimensions of data:", dataset.shape)

# make sure print all the columns
# print the first 10 rows of the data
pandas.set_option('display.width', 1000)
pandas.set_option('display.max_columns', 500)
# print(dataset.head(10))

# print(dataset.tail(10))

# print(dataset.describe())

# print(dataset.groupby("class").size())

dataset.plot(kind="box", subplots=True, layout=(2, 2), sharex=False, sharey=False)
plt.show()
