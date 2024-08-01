import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Generate some sample data
np.random.seed(0)
data = pd.DataFrame({
    'A': np.random.normal(loc=0, scale=1, size=100),
    'B': np.random.normal(loc=5, scale=2, size=100),
    'C': np.random.normal(loc=10, scale=3, size=100)
})

# Set the style of the visualizations
sns.set_style('whitegrid')

# Histogram
plt.figure(figsize=(10, 6))
sns.histplot(data['A'], bins=20, kde=True)
plt.title('Histogram of A')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

# Scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(x=data['A'], y=data['B'])
plt.title('Scatter Plot of A vs B')
plt.xlabel('A')
plt.ylabel('B')
plt.show()

# Box plot
plt.figure(figsize=(10, 6))
sns.boxplot(data=data[['A', 'B', 'C']])
plt.title('Box Plot of A, B, and C')
plt.xlabel('Variable')
plt.ylabel('Value')
plt.show()
