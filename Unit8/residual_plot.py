import seaborn as sns
import matplotlib.pyplot as plt

anscombe = sns.load_dataset("anscombe")
df_a = anscombe.query("dataset == 'I'")
sns.residplot(x="x", y="y", data=df_a)
plt.show()