import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

# First we need to connect to database
conn = sqlite3.connect("./Unit9/pima.db")

# Exercise 1: Above 50
# Next we write a SQL query to select all data from the Pima table
query="""
SELECT *
FROM Pima
WHERE Age > 50
"""
# Now we can use pandas to execute the query and load the data into a DataFrame
df = pd.read_sql(query, conn)

# Show first rows
print("PIMA dataset loaded from SQLite database:")
print(df.describe())
print("\n")

# Exercise 2: Above 50
# Next we write a SQL query to select all data from the Pima table
query="""
SELECT PlGlcConc, BMI
FROM Pima
WHERE PlGlcConc > 140
"""
# Now we can use pandas to execute the query and load the data into a DataFrame
df = pd.read_sql(query, conn)

# Show first rows
print("PIMA dataset loaded from SQLite database:")
print(df.describe())
print("\n")

# Exercise 3: Show all patients with BMI between 30 and 40 and age < 40.
# Next we write a SQL query to select all data from the Pima table
query="""
SELECT *
FROM Pima
WHERE BMI BETWEEN 30 AND 40 AND Age < 40
"""
# Now we can use pandas to execute the query and load the data into a DataFrame
df = pd.read_sql(query, conn)

# Show first rows
print("PIMA dataset loaded from SQLite database:")
print(df.describe())
print("\n")

# Do a histogram of bloodpressure
df.plot.hist(column="BloodP", bins=20)
plt.show()