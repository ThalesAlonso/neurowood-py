def load_data_set(filename):
    return sklearn.datasets.load_svmlight_file(filename)

def kfold_hit_ratio(n_splits,X,y,classifier_obj):
    kf = KFold(n_splits, True)
    for train_index, test_index in kf.split(X):
        X_train, X_test = X[train_index], X[test_index]
        y_train, y_test = y[train_index], y[test_index]


