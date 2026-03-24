import pandas as pd
import matplotlib.pyplot as plt

# ===================================================================================
# Workflow for loading data from a CSV file, cleaning it, and plotting it with pandas
# ===================================================================================
# Load a CSV file into a DataFrame
df = pd.read_csv("./Unit3/cities.csv")

print(df.head()) # Notice the first collumn is unamed

# So we rename first collumn to index
df = df.rename(columns={"Unnamed: 0": "index"})

print(df.head()) # Now we notice that the first collumn is actually not useful 

# Drop the index collumn
df.drop(columns=["index"], inplace=True)

print(df.head()) # The index collumn is now gone

# Now lets plot the cleaned data
df.plot(kind='bar', x='name', y='population', title="City Populations", legend=False)
plt.xlabel("City")
plt.ylabel("Population (in millions)")
plt.show()