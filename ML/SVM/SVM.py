import sklearn
from sklearn import datasets
from sklearn import svm
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier

cancer = datasets.load_breast_cancer()
# print(cancer.feature_names)
# print(cancer.target_names)

x = cancer.data
y = cancer.target

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size = 0.01)

classes = ['malignant', 'benign']

# clf = KNeighborsClassifier(n_neighbors=7)
clf = svm.SVC(kernel='linear')
clf.fit(x_train, y_train)

y_pred = clf.predict(x_test)

acc = metrics.accuracy_score(y_test, y_pred)

for i in range(len(x_test)):
    if y_pred[i]!=y_test[i]:
        print('x: {}.y: {}. actual: {}'.format(x_test[i], classes[y_pred[i]], classes[y_test[i]]))
print(acc)