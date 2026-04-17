import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load data
df = pd.read_csv("./Unit7/brfss.csv")
df.set_index('idx')

# Pairplot for quick overview over a dataset
sns.pairplot(data=df, vars=["age", "wtyrago", "finalwt", "wtkg2"])
plt.show()

# Single Variable (Weight over Height)
sns.relplot(data=df, x='htm3', y='wtkg2', kind='scatter')
plt.show()

sns.relplot(data=df, x='htm3', y='wtkg2', hue="sex", kind='scatter')
plt.savefig("./Unit7/without_jitter.png")

# Add some jitter to compensate for rounding artifacts
def add_jitter(values, jitter=0.5):
    n = len(values)
    return np.random.uniform(-jitter, jitter, n) +values
df['htm3_jitter'] = add_jitter(df.htm3,1.3)
df['wtkg2_jitter'] = add_jitter(df.wtkg2, 0.5)

plt.figure()
sns.relplot(data=df, x='htm3_jitter', y='wtkg2_jitter', hue='sex', kind='scatter')
plt.savefig("./Unit7/with_jitter.png")