import pandas as pd
from scipy import stats
import matplotlib.pylab as plt
import numpy as np

# Load the data
df = pd.read_csv('./data/brfss.csv')
df.set_index('idx')
df = df.dropna()

# Perform linear regression using linear least square
k, d, p, _, _= stats.linregress(df.htm3, df.wtkg2)

print("The line fit was successfl")

# Extract the data from the dataframe
x, y = df.htm3, df.wtkg2

# Use the linear regression model to predict new y values
# TODO: Explain this line better
y_model = k * x + d

# PLot the data and the fitted line
plt.plot(x,y, 'o',label='original data')
plt.plot(x, y_model, 'r', label='fitted line')
plt.legend()
plt.show()