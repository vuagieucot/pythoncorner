from sklearn.preprocessing import scale
from sklearn.datasets import load_digits
from sklearn.cluster import KMeans
from sklearn import metrics
import numpy as np

digits = load_digits()
data = scale(digits.data)
y = digits.target

k = 10
# k = len(np.unique(y))
samples, features = data.shape

def bench_k_means(estimator, name, data):
    estimator.fit(data)
    print('%-9s\t%i\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f'
          % (name, estimator.inertia_,
             metrics.homogeneity_score(y, estimator.labels_),
             metrics.completeness_score(y, estimator.labels_),
             metrics.v_measure_score(y, estimator.labels_),
             metrics.adjusted_rand_score(y, estimator.labels_),
             metrics.adjusted_mutual_info_score(y, estimator.labels_),
             metrics.silhouette_score(data, estimator.labels_,
                                      metric = 'euclidean')))

clf = KMeans(n_clusters=k, init='random', n_init=10)
clf.fit(data)
print(list(data))
print(list(clf.labels_))
print(len(list(y)))
pred = clf.predict(data)
print('='*20)
print(pred[-1])
# print('='*20)
# print(np.unique(y))
bench_k_means(clf, '1', data)