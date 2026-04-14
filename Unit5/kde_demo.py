import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('./Unit5/nsfg_preg.csv')

# Filter the dataset to include only first births
first = df[df.birthord == 1]

# Now we can create the histogram
# Passing kde=True to the histplot function will overlay the estimated Density Function using Kernel Density Estimation (KDE) on top of the histogram
# Without KDE ==> Probability Mass Function (PMF)
# With KDE ==> Probability Density Function (PDF)
sns.histplot(data=first, x="prglngth",
    color="skyblue",label="firstbabies",
    kde=True,bins=range(20,50),
    stat="frequency")
plt.xlim(20,50)
plt.legend()
plt.show()


# Do the same for the cumulative distribution function (CDF) 
sns.histplot(data=first, x="prglngth",
    color="red",label="firstbabies",
    kde=True, cumulative=True, bins=range(20,50),
    stat="probability")
plt.xlim(20,50)
plt.legend()
plt.show()
