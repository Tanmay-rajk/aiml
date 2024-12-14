import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
def bayes_theorem(p_a, p_b, p_b_given_a):
p_a_given_b = (p_b_given_a * p_a) / p_b
return p_a_given_b
p_rain = 0.20
p_cloudy = 0.40
p_cloud_given_rain = 0.85
p_rain_given_cloudy = bayes_theorem(p_rain, p_cloudy, p_cloud_given_rain)
print(f"P(rain | cloudy) = {p_rain_given_cloudy}")
np.random.seed=42
x = np.random.rand(100, 2) * 10
y = np.array([0 if x[0] + x[1] < 10 else 1 for x in x])
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
model = GaussianNB()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
report = classification_report(y_test, y_pred)
print(f"Accuracy: {accuracy}")
print(f"Confusion Matrix:\n{conf_matrix}")
print(f"Classification Report:\n{report}")
plt.figure(figsize=(8, 6))
plt.scatter(x[:, 0], x[:, 1], c=y, cmap='coolwarm', edgecolor='k')
plt.title('Data Points Classification')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()
