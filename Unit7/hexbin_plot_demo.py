import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load data
df = pd.read_csv("./Unit7/brfss.csv")
df.set_index('idx')

# Add some jitter to compensate for rounding artifacts
def add_jitter(values, jitter=0.5):
    n = len(values)
    return np.random.uniform(-jitter, jitter, n) +values
df['htm3_jitter'] = add_jitter(df.htm3,1.3)
df['wtkg2_jitter'] = add_jitter(df.wtkg2, 0.5)

# Normal Scatter Plot
sns.relplot(data=df, x='htm3_jitter', y='wtkg2_jitter',hue="sex", kind='scatter')
plt.show()

sns.jointplot(data=df, x="htm3", y="wtkg2", kind="hex")
plt.show()