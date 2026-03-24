import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Create a pandas DataSeries from a list of values
fruits = ['apples', 'oranges', 'cherries', 'pears']
ds1 = pd.Series(data=[20, 33, 52, 10], index=fruits)
print(ds1)

# Access values from the DataSeries using the name
print(ds1['oranges'])

# Accessing by index requires using the iloc property
print(ds1.iloc[1])

# Calculations
ds2 = pd.Series(data=[17, 13, 31, 32], index=fruits)
print(ds2)
print(ds1 + ds2)

# Plotting with pandas
ds3 = ds1 + ds2
ds3.plot(kind='bar')
plt.title("Fruit Counts")
plt.xlabel("Fruit")
plt.ylabel("Count")
plt.show()

# Applying functions to DataSeries
# Numpy functions 
ds4 = ds1.apply(np.sqrt)
print(ds4)

# Apply your own function to a DataSeries
def minus_one(x):
    return x - 1
ds5 = ds1.apply(minus_one)
print(ds5)

