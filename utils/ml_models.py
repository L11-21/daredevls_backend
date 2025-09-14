import numpy as np
from sklearn.metrics import accuracy_score, mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsRegressor


def run_ml_models():
    # Simulated data
    X = np.array([[i, j] for i in range(4) for j in range(1, 8)])
    y = np.array([i + j for i, j in X])

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Naive Bayes
    gnb = GaussianNB()
    gnb.fit(X_train, y_train)
    y_pred_nb = gnb.predict(X_test)
    accuracy_nb = accuracy_score(y_test, y_pred_nb)

    # KNN
    knn = KNeighborsRegressor(n_neighbors=3)
    knn.fit(X_train, y_train)
    y_pred_knn = knn.predict(X_test)
    mse_knn = mean_squared_error(y_test, y_pred_knn)

    return {
        "naive_bayes_accuracy": round(accuracy_nb * 100, 2),
        "knn_mse": round(mse_knn, 2)
    }
