# Github link
# https://github.com/marcustorm/kclml/blob/master/iris.py

import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
import sklearn

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ["sepal-length", "sepal-width", "petal-length", "petal-width", "class"]
dataset = pandas.read_csv(url, names=names)

print(dataset.shape)
