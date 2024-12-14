import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
iris = load_iris()
X = iris.data # Features
y = iris.target # Labels
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy of k-NN classifier: {accuracy:.2f}")
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_pred, marker="o", label="Predicted")
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_test, marker="x", label="Actual")
plt.title("k-Nearest Neighbors Classification Results")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.legend()
plt.show()
