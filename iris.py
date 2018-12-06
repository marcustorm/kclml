# Github link
# https://github.com/marcustorm/kclml/blob/master/iris.py

# Based off a project by Dr Jason Brownlee

import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
import sklearn
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score


# url = "http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ["sepal-length", "sepal-width", "petal-length", "petal-width", "class"]

# import the data from the web
dataset = pandas.read_csv("survey.csv", names=names)

# what are the dimensions of the data?
# print("Dimensions of data:", dataset.shape)

# make sure print all the columns
# print the first 10 rows of the data
pandas.set_option('display.width', 1000)
pandas.set_option('display.max_columns', 500)
# print(dataset.head(10))

# print(dataset.tail(10))

# statistical description
# print(dataset.describe())

# print number of items in each class
# print(dataset.groupby("class").size())

# plot boxplots
# dataset.plot(kind="box", subplots=True, layout=(2, 2), sharex=False, sharey=False)
# plt.show()

# plot historgram
# dataset.hist()
# plt.show()

# multivariate plot
# scatter_matrix(dataset)
# plt.show()

array = dataset.values
X = array[:, 0:4]
Y = array[:, 4]

validation_size = 0.2
seed = 7
X_train, X_validation, Y_train, Y_validation = sklearn.model_selection.train_test_split(X, Y, test_size=validation_size,
                                                                                        random_state=seed)
scoring="accuracy"

# Check algorithms

models = []
models.append(("LR", LogisticRegression()))
models.append(("LDA", LinearDiscriminantAnalysis()))
models.append(("KNN", KNeighborsClassifier()))
models.append(("CART", DecisionTreeClassifier()))
models.append(("NB", GaussianNB()))
models.append(("SVM", SVC()))

# evaluate models

my_flower = [4.5, 3.5, 6.1, 2.4]

results = []
names = []
my_flower_prediction = []

for name, model in models:
    kfold = sklearn.model_selection.KFold(n_splits=10, random_state=seed)
    cv_results = sklearn.model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
    results.append(cv_results)
    names.append(name)
    # my_flower_prediction.append(model.predict(my_flower))
    msg = "%s: %f(%f)" % (name, cv_results.mean(), cv_results.std())
    print(msg)
    # print(my_flower_prediction)
