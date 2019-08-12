import numpy as np
from sklearn import ensemble
from sklearn import datasets
from sklearn.utils import shuffle


def load_model():
    # Load data
    boston = datasets.load_boston()
    X, y = shuffle(boston.data, boston.target, random_state=13)
    X = X.astype(np.float32)

    # Fit regression model
    params = {'n_estimators': 500, 'max_depth': 4, 'min_samples_split': 2,
              'learning_rate': 0.01, 'loss': 'ls'}
    clf = ensemble.GradientBoostingRegressor(**params)
    clf.fit(X, y)

    return clf
