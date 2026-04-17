import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load data
df = pd.read_csv("./Unit7/brfss.csv")
df.set_index('idx')

# Add line plot
sns.relplot(data=df, x="htm3", y="wtkg2", kind="line")
plt.show()

# Add line plot with average line included
sns.lmplot(data=df, x="htm3", y="wtkg2", x_estimator=np.mean)
plt.show()