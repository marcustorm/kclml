import numpy
import pandas
import nltk

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

# url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"

names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']

dataset = pandas.read_csv(url, names=names)


pandas.set_option('display.max_columns', 10)
print(dataset.head())
