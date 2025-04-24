from sklearn.metrics import accuracy_score, mean_squared_error
import numpy as np

def evaluate_classification(model, X, y):
    """Evaluate classification model."""
    y_pred = model.predict(X)
    accuracy = accuracy_score(y, y_pred)
    return accuracy

def evaluate_regression(model, X, y):
    """Evaluate regression model."""
    y_pred = model.predict(X)
    mse = mean_squared_error(y, y_pred)
    rmse = np.sqrt(mse)
    return rmse
