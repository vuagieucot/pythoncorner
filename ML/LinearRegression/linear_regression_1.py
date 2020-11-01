import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
import pickle
import matplotlib.pyplot as pyplot
from matplotlib import style

data = pd.read_csv('bank.csv', sep=';')
data = data[['age', 'balance']]
dependent = 'balance'
independent = 'age'
x = np.array(data[[independent]])
y = np.array(data[[dependent]])
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)

# best = 0
# for _ in range(1000):
#     x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)
#     linear = linear_model.LinearRegression()
#     linear.fit(x_train, y_train)
#     acc = linear.score(x_test, y_test)
#     print(acc)
#     if acc > best:
#         best = acc
#         print('best = {}'.format(best))
#         with open('bankmodel.pickle', 'wb') as f:
#             pickle.dump(linear, f)
#
# print('final: {}'.format(best))

linear_pickle = open('bankmodel.pickle', 'rb')
linear = pickle.load(linear_pickle)

print('Co: {}\nIntercept: {}'.format(linear.coef_, linear.intercept_))

style.use('ggplot')
pyplot.scatter(data[independent], data[dependent])
pyplot.xlabel(independent)
pyplot.ylabel(dependent)
pyplot.show()