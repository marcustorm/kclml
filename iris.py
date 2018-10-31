import numpy
import pandas
import nltk
from matplotlib.pyplot import plot as plt

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

# url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"

names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']

dataset = pandas.read_csv(url, names=names)


print(dataset.shape)

pandas.set_option('display.max_columns', 10)
print(dataset.head(20))

print(dataset.describe())

print(dataset.groupby('class').size())

plot = dataset.plot(kind='box')
plt.show()
