import pandas as pd
from scipy import stats
import matplotlib.pylab as plt
from typing import Protocol, cast


class LinregressResultLike(Protocol):
	slope: float
	intercept: float
	rvalue: float

# Load the data
df = pd.read_csv('./data/brfss.csv')
df.set_index('idx')
df = df.dropna()

# Perform linear regression using linear least square
result = stats.linregress(df.htm3, df.wtkg2)
k = result.slope
d = result.intercept
r_squared = result.rvalue ** 2

print("The line fit was successfull")

# Extract the data from the dataframe
x, y = df.htm3, df.wtkg2

# Use the linear regression model to predict new y values
# TODO: Explain this line better
y_model = k * x + d

# Plot the data and the fitted line
plt.plot(x,y, 'o',label='original data')
plt.plot(x, y_model, 'r', label=f'fitted line (R^2={r_squared:.3f})')
plt.legend()
plt.show()