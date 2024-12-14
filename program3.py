import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
iris = load_iris()
x=iris.data
y= iris.target
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.4, random_state=42)
cff = DecisionTreeClassifier(criterion='gini', random_state=42)
cff.fit(X_train, y_train)
accuracy = cff.score(X_test, y_test)
print(f'{accuracy:.2f}')
plt.figure(figsize=(12, 8))
tree.plot_tree(cff,
filled=True,
feature_names=iris.feature_names,
class_names=iris.target_names)
plt.show()
