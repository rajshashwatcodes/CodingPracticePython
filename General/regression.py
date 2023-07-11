import numpy as np
from sklearn.linear_model import LinearRegression

# Generate some sample data
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 6, 8, 10])

# Create a linear regression model
model = LinearRegression()

# Train the model
model.fit(X, y)

# Predict using the trained model
X_test = np.array([[6], [7]])
predictions = model.predict(X_test)

# Print the predictions
for i in range(len(X_test)):
    print("Prediction for {}: {}".format(X_test[i][0], predictions[i]))
