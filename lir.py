import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
np.random.seed(0)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.rand(100, 1)
model = LinearRegression()
model.fit(X, y)
X_new = np.array([[0], [2]])
y_pred = model.predict(X_new)
plt.scatter(X, y, label='Data Points')
plt.plot(X_new, y_pred, 'r-', label='Regression Line', linewidth=2)
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()
