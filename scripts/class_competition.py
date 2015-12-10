#!/usr/local/bin/python
""" General skeleton for machine learning
"""

# 1. Load the dataset
from sklearn.datasets import load_digits
digits = load_digits()
X, y = digits.data, digits.target

# 2. Split the dataset into training and test set (e.g., 80/20)
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# 3. Choose estimator
from sklearn.svm import SVC
estimator = SVC(kernel='linear')

# 4. Choose cross-validation iterator
from sklearn.cross_validation import ShuffleSplit
cv = ShuffleSplit(X_train.shape[0], n_iter=10, test_size=0.2, random_state=0)

# 5. Tune the hyperparameters by applying cv iterator on the training set
from sklearn.grid_search import GridSearchCV
import numpy as np
tuned_params = [{'gamma': np.logspace(-6, -1, 10)}]
classifier = GridSearchCV(estimator, tuned_params, cv=cv)
classifier.fit(X_train, y_train)

# 6. Debug algorithm with learning curve
# X_train is randomly split into a training and test set 10 times
from sklearn.learning_curve import learning_curve
import matplotlib as plt

# title = 'Learning Curves (SVM, linear kernel, $\gamma=%.6f$)' % classifier.best_estimator_.gamma
# estimator = SVC(kernel='linear', gamma=classifier.best_estimator_.gamma)
# learning_curve.plot_learning_curve(estimator, title, X_train, y_train, cv=cv)
# plt.show()

# 7. Final evaluation on the test set
classifier.score(X_test, y_test)

# 7a. Test over-fitting in model selection with nested cross-validation
# (using the whole dataset)
from sklearn.cross_validation import cross_val_score
print(cross_val_score(classifier, X, y))

# 8. Train model on whole dataset
classifier.fit(X, y)
