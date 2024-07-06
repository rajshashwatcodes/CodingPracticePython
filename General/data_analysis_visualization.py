import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Setting the style for seaborn
sns.set(style="whitegrid")

# Creating a sample dataset
np.random.seed(42)
data = {
    'Date': pd.date_range(start='1/1/2023', periods=100, freq='D'),
    'Temperature': np.random.normal(loc=20, scale=5, size=100),
    'Humidity': np.random.uniform(low=40, high=80, size=100),
    'Rainfall': np.random.poisson(lam=2, size=100)
}

df = pd.DataFrame(data)

# Data Cleaning: Handling missing values
df['Temperature'] = df['Temperature'].fillna(df['Temperature'].mean())
df['Humidity'] = df['Humidity'].fillna(df['Humidity'].mean())
df['Rainfall'] = df['Rainfall'].fillna(df['Rainfall'].mean())

# Feature Engineering: Adding a new column 'Feels Like Temperature'
df['Feels Like Temperature'] = df['Temperature'] - (0.55 - 0.55 * df['Humidity'] / 100) * (df['Temperature'] - 14.5)

# Plotting
fig, axes = plt.subplots(3, 1, figsize=(14, 18))

# Temperature Plot
sns.lineplot(ax=axes[0], x='Date', y='Temperature', data=df, color='red')
axes[0].set_title('Daily Temperature Over Time')
axes[0].set_xlabel('Date')
axes[0].set_ylabel('Temperature (°C)')

# Humidity Plot
sns.lineplot(ax=axes[1], x='Date', y='Humidity', data=df, color='blue')
axes[1].set_title('Daily Humidity Over Time')
axes[1].set_xlabel('Date')
axes[1].set_ylabel('Humidity (%)')

# Rainfall Plot
sns.lineplot(ax=axes[2], x='Date', y='Rainfall', data=df, color='green')
axes[2].set_title('Daily Rainfall Over Time')
axes[2].set_xlabel('Date')
axes[2].set_ylabel('Rainfall (mm)')

plt.tight_layout()
plt.show()

# Correlation Heatmap
plt.figure(figsize=(10, 8))
correlation_matrix = df[['Temperature', 'Humidity', 'Rainfall', 'Feels Like Temperature']].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.show()
