import sklearn
from sklearn.neighbors import KNeighborsClassifier
from sklearn import linear_model, preprocessing
import pandas as pd
# from sklearn.utils import shuffle
# import numpy as np
# import matplotlib.pyplot as pyplot
# from matplotlib import style

data = pd.read_csv('car.data')
# print(data.head())

predict = 'class'

pre = preprocessing.LabelEncoder()

buying = pre.fit_transform(list(data['buying']))
maint = pre.fit_transform(list(data['maint']))
door = pre.fit_transform(list(data['door']))
persons = pre.fit_transform(list(data['persons']))
lug_boot = pre.fit_transform(list(data['lug_boot']))
safety = pre.fit_transform(list(data['safety']))
cls = pre.fit_transform(list(data['class']))
# print(buying)

x = list(zip(buying,maint,door,persons,lug_boot,safety))
y = list(cls)

x_train,x_test,y_train,y_test = sklearn.model_selection.train_test_split(x,y,test_size=0.05)

model = KNeighborsClassifier(n_neighbors=9)
model.fit(x_train, y_train)

acc = model.score(x_test, y_test)
print(acc)
predicte = model.predict(x_test)

names=['unacc','acc','good','vgood']

for x in range(len(x_test)):
    print('Predicted: {}, Data: {}, Actual: {}'.format(names[predicte[x]], x_test[x], names[y_test[x]]))
    n = model.kneighbors([x_test[x]], 9, True)
    print('N: {}'.format(n))