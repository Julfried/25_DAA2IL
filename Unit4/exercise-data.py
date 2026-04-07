import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('./Unit4/exercise-data.csv')
print(df.head())

# Show dataframe collumn info
df.info()

# Get the summary of the data
print(df.isna().sum())

# Drop rows with missing values (NaN)
df = df.dropna()
df.dropna(inplace=True)
print(df.isna().sum())

# Line plot
df.plot(kind='line', x='Date', y='Calories')
plt.show()

# UNIVARIATE ANALYSIS
# Extract calories collum
calories = df['Calories']
print("The average calories consumed is:", calories.mean())
print("The variance in calories consumed is:", calories.var())
print("The standard deviation in calories consumed is:", calories.std())

# Calculate the five-number summary (min, Q1, median, Q3, max)
print("The minimum calories consumed is:", calories.min())
print("The 25th percentile of calories consumed is:", calories.quantile(0.25))
print("The 50th percentile of calories consumed is:", calories.quantile(0.5))
print("The 75th percentile of calories consumed is:", calories.quantile(0.75))
print("The maximum calories consumed is:", calories.max())

# Skewness with pearson skewness coefficient
skewness = 3 * (calories.mean() - calories.median()) / calories.std()
print("The skewness of calories consumed is:", skewness)

# Plot a histogram of calories consumed (to check for skewness)
calories.plot(kind='hist', bins=10, edgecolor='black')
plt.title('Distribution of Calories Consumed')
plt.xlabel('Calories')
plt.ylabel('Frequency')
plt.savefig('./Unit4/exercise-histogram.png', dpi=600)

# Calculate many statistics at once using df.describe()
print(df.describe())

# Box plot to visualize the distribution of all (collums)
plt.figure()
df.boxplot(column=['Calories', 'Duration', 'Pulse', 'Maxpulse'])
plt.title('Box Plot of Exercise Data')
plt.ylabel('Values')
plt.savefig('./Unit4/exercise-boxplot.png', dpi=600)
