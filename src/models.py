from sklearn.linear_model import LogisticRegression, LinearRegression

def train_logistic(X, y):
    """Train a logistic regression model."""
    model = LogisticRegression()
    model.fit(X, y)
    return model

def train_linear(X, y):
    """Train a linear regression model."""
    model = LinearRegression()
    model.fit(X, y)
    return model
