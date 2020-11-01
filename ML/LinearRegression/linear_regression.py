import numpy as np
import pandas as pd
import sklearn
from sklearn import linear_model
import matplotlib.pyplot as pyplot
import pickle
from matplotlib import style

data = pd.read_csv('LinearRegression/student-mat.csv', sep = ';')
#separator in csv file is ';'

data = data[['G1','G2','G3','studytime','failures','absences']]

predict = 'G3'

x = np.array(data.drop([predict], 1))
y = np.array(data[predict])
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size = 0.05)

# x = data.drop([predict], 1)
# y = data[[predict]]

"""best = 0
for _ in range(400):
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size = 0.1)
    #x_train + x_test = x \\ |x_test| = test_size * |x|
    #y_train + y_test = y \\ |y_test| = test_size * |y|

    linear = linear_model.LinearRegression()

    linear.fit(x_train, y_train)
    acc = linear.score(x_test, y_test)
    print(acc)

    if acc > best:
        print(acc, best)
        best = acc
        with open('studentmodel.pickle', 'wb') as f:
            pickle.dump(linear, f)"""

pickle_in = open('LinearRegression/studentmodel.pickle', 'rb')
linear = pickle.load(pickle_in)

acc = linear.score(x_test, y_test)

print(acc)
print('Co: {}'.format(linear.coef_))
print('Intercept: {}'.format(linear.intercept_))

predicti = linear.predict(x_test)

# for x in range(len(predicti)):
#     print(predicti[x], x_test[x], y_test[x])

p=['G1']
style.use('ggplot')
pyplot.scatter(data[p], data['G3'])
pyplot.xlabel(p)
pyplot.ylabel('Final grade')
pyplot.show()