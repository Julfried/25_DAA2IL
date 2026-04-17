import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('./data/brfss.csv')
df.set_index('idx')

# Calculate to covariance matrix
print(df.cov())

# Calculate pearson correlation coefficient
print(df.corr(method='pearson'))

# Visualize in a heatmap
sns.heatmap(df.corr(method='pearson'))
plt.show()

