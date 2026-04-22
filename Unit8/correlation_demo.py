import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('./Unit8/corrdata.csv')

# Single Variable (a over b)
sns.relplot(data=df, x='a', y='b', kind="scatter")
plt.show()

# Calculate Covariance
cov = df.cov()
corr = df.corr("pearson")

# Show the difference between covariance and pearson correalation
print(cov)
print(corr)

# Show in heatmap
sns.heatmap(cov)
plt.show()
sns.heatmap(corr)
plt.show()
