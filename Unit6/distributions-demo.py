import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats



df = pd.read_csv('./Unit6/pima-indians-diabetes.csv')

# Get some useful statistics
print(df.describe())

# Filter by diabetes
with_diabetes = df.query("HasDiabetes == 1 and BloodP > 0")

# Plot BMI for Diabetes patients
# Plot CDFs
sns.histplot(with_diabetes, x="BMI", stat="probability", kde=True, cumulative=False, color="red")
plt.legend()
plt.show()

# Scipy probplot
bmi = with_diabetes.query("BMI > 0")["BMI"]
stats.probplot(bmi, dist=stats.uniform , plot=plt, rvalue=True)
plt.show()

# Problplot confirms that the data follows a normal distribution
# Estimate the parameters of this normal distribution using scipy.stats
mean, std = stats.norm.fit(bmi)

print("Estimated mean: ", mean)
print("Estimated standard deviation: ", std)