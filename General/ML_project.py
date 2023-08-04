import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score

# Task 1: Logistic Regression with Binary Classification (USA and Non-USA)

# Load the training dataset
train_data = pd.read_csv('mpg_trainset.csv')

# Preprocess the dataset for binary classification (USA and Non-USA)
train_data['Origin'] = train_data['Origin'].replace({1: 'USA', 2: 'Non-USA', 3: 'Non-USA'})

# Convert 'USA' to 1 and 'Non-USA' to 0
train_data['Origin'] = train_data['Origin'].apply(lambda x: 1 if x == 'USA' else 0)

# Separate features (X) and class labels (y)
X_train = train_data.drop(columns=['Origin'])
y_train = train_data['Origin']

# Apply Logistic Regression with C = 0.1
C_values = [0.001, 0.01, 0.1, 1, 10, 100]
cost_values = []

for C_val in C_values:
    model = LogisticRegression(C=C_val)
    model.fit(X_train, y_train)
    cost_values.append(model.score(X_train, y_train))

# Plot the cost function J(θ) for the training dataset
plt.plot(C_values, cost_values, marker='o')
plt.xlabel('C Value')
plt.ylabel('Cost J(θ)')
plt.title('Cost Function for Logistic Regression')
plt.show()

# Load the test dataset
test_data = pd.read_csv('mpg_testset.csv')

# Preprocess the test dataset for binary classification (USA and Non-USA)
test_data['Origin'] = test_data['Origin'].replace({1: 'USA', 2: 'Non-USA', 3: 'Non-USA'})
test_data['Origin'] = test_data['Origin'].apply(lambda x: 1 if x == 'USA' else 0)

# Separate features (X_test) and class labels (y_test)
X_test = test_data.drop(columns=['Origin'])
y_test = test_data['Origin']

# Predict the target feature for the test dataset
y_pred = model.predict(X_test)

# Plot the confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(conf_matrix)

# Task 2: Logistic Regression with Multi-Class Classification (USA, Europe, and Japan)

# Load the dataset with 3 categories in the Origin target feature
mpg_data = pd.read_csv('mpg_trainset.csv')

# Preprocess the dataset
# We won't convert 'Origin' to numerical, as it is already categorical with 3 categories

# Separate features (X) and class labels (y)
X = mpg_data.drop(columns=['Origin'])
y = mpg_data['Origin']

# Apply Logistic Regression with C = 0.1
model_multi = LogisticRegression(C=0.1, multi_class='ovr')
model_multi.fit(X, y)

# Load the test dataset for multi-class classification
test_data_multi = pd.read_csv('mpg_testset.csv')

# Preprocess the test dataset for multi-class classification
X_test_multi = test_data_multi.drop(columns=['Origin'])
y_test_multi = test_data_multi['Origin']

# Classify the test instances into 1(USA), 2(Europe), or 3(Japan)
y_pred_multi = model_multi.predict(X_test_multi)

# Find how many of the test instances were predicted correctly.
accuracy = accuracy_score(y_test_multi, y_pred_multi)
print("Accuracy:", accuracy)

# Visualize the classified dataset with each class colored differently
plt.scatter(X_test_multi['Horsepower'], X_test_multi['Acceleration'], c=y_pred_multi)
plt.xlabel('Horsepower')
plt.ylabel('Acceleration')
plt.title('Classified Dataset')
plt.show()
