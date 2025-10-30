import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('train.csv')
print(df.head())
print(df.info())
print(df.describe())

# Visualize survival by class
df.groupby('Pclass')['Survived'].mean().plot(kind='bar')
plt.title('Survival Rate by Passenger Class')
plt.ylabel('Survival Rate')
plt.show()