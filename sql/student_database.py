import sqlite3
import pandas as pd

# Load CSV file
data = pd.read_csv("data/student_data.csv")

# Connect to SQLite database
connection = sqlite3.connect("sql/student_performance.db")

# Store data in a table
data.to_sql("students", connection, if_exists="replace", index=False)

print("Student data added to database successfully.")

# Close connection
connection.close()