import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('./Unit5/nsfg_preg.csv') # NOTE: does not match the numbers in the codebook

# Filter the dataset to include only first births
first = df[df.birthord == 1] # According to the codebook, outcome == 1 means live birth

# Alternatively the data can also be filtered using pandas query method
firstv2 = df.query('birthord == 1 and outcome == 1')
print("Both methods produce the same result:",first.equals(firstv2)) # Check if the two dataframes are equal

# Do first babies arrive late?
# Print average and standard deviation
avg = first["prglngth"].mean()
std = first["prglngth"].std()
print(f"First babies arrive at {avg:.2f} weeks, with a standard deviation of {std:.2f}.")

# Print boxplot of the data
first.plot(kind='box', y='prglngth', title='Boxplot of pregnancy length for first babies', ylabel='Pregnancy length (weeks)')
plt.show()
