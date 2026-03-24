import pandas as pd
import matplotlib.pyplot as plt

# Create the range of years (avoid having to write list manually)
years = range(2014, 2018)

# Create column of sales data for each shop (each column is a DataSeries)
shop1 = pd.Series([2409.14, 2941.01, 3496.83,3119.55],index=years)
shop2 = pd.Series([1203.45, 3441.62, 3007.83,3619.53],index=years)
shop3 = pd.Series([3412.12, 3491.16, 3457.19,1963.10],index=years)

# Now we can combine these collumns into a table (DataFrame)
shops_df = pd.concat([shop1, shop2, shop3], axis=1)

# Add labels to the columns for better readability
shops_df.columns = ["Vienna", "Berlin", "Paris"]

# Now we can print the first few rows of the DataFrame to see what it looks like
print(shops_df.head()) # use head() to print only the first few rows of the DataFrame

# Similar to DataSeries, we can also access single values from a DataFrame
# Accesing a single column (which is a DataSeries)
print("\nSales in Vienna:")
print(shops_df['Vienna'])

# And we can do even more complex filtering by using the loc property
print("\nSales in Vienna from 2014 to 2016:")
print(shops_df.loc['2014':'2016', 'Vienna']) # Attention last value is included in this case!

# Now the data is in a nice table format ==> we can easily plot it
shops_df.plot(kind='bar')
plt.title("Sales by City")
plt.xlabel("Year")
plt.ylabel("Sales (in Euros)")
plt.show()