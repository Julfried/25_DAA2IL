import pandas as pd
import sqlite3

# PIMA dataset
# Load from JSON file
df = pd.read_json("./Unit9/pima.json")

# Show first rows
print("PIMA dataset loaded from JSON file:")
print(df.head())
print("\n")

# Do the same thing using a simple SQLite database
# First we need to connect to database
conn = sqlite3.connect("./Unit9/pima.db")

# Next we write a SQL query to select all data from the Pima table
query="""
SELECT *
FROM Pima
"""
# Now we can use pandas to execute the query and load the data into a DataFrame
df = pd.read_sql(query, conn)

# Show first rows
print("PIMA dataset loaded from SQLite database:")
print(df.head())
print("\n")

# You can write more complex querries to filter the data. e.g.
query="""
SELECT * FROM Pima
WHERE Age > 30
"""
df = pd.read_sql(query, conn)

# Show statistics
print("Statistics of the filtered DataFrame:")
print(df.describe())
print("\n")

# Finally we should close the connection to the database
conn.close()