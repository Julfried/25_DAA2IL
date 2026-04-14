import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('./Unit6/pima-indians-diabetes.csv')

# Get some useful statistics
print(df.describe())

# Filter by diabetes
with_diabetes = df.query("HasDiabetes == 1 and BloodP > 0")
without_diabetes = df.query("HasDiabetes == 0 and BloodP > 0")

# Plot CDFs
sns.histplot(with_diabetes, x="BloodP", stat="probability", kde=True, cumulative=False, color="red")
sns.histplot(without_diabetes, x="BloodP", stat="probability", kde=True, cumulative=False, color="blue")
plt.legend()
plt.show()

print("With diabetes: ", with_diabetes["BloodP"].mean())
print("Without diabetes: ", without_diabetes["BloodP"].mean())