#!/usr/local/bin/python

# 1. Load the dataset
import numpy as np
from sklearn.datasets import load_digits
digits = load_digits()
X, y = digits.data, digits.target

# 2. Split dataset into training and test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# 3. Choose estimator
from sklearn.svm import SVC
estimator = SVC(kernel='rbf')

# 4. Choose cross-validation iterator
from sklearn.cross_validation import ShuffleSplit
from sklearn.grid_search import GridSearchCV

cv = ShuffleSplit(X_train.shape[0], n_iter=10, test_size=0.2, random_state=0)
tuned_params = [{'gamma': np.logspace(-6, -1, 10)}]
classifier = GridSearchCV(estimator, tuned_params, cv=cv)
classifier.fit(X_train, y_train)
print("Validation score: {0}".format(classifier.best_score_))
print("Achieved with the following model: \n{0}\n".format(classifier.best_estimator_))

# 5. Score on the test set
print("Test set score: {0}".format(classifier.score(X_test, y_test)))
