import sqlite3

# Connect to the database
connection = sqlite3.connect("sql/student_performance.db")

# Create a cursor
cursor = connection.cursor()

# Run SQL query
cursor.execute("""
    SELECT student_id, attendance_percent, final_score
    FROM students
    WHERE attendance_percent < 70
    AND final_score < 60
""")

# Get the results
results = cursor.fetchall()

# Display the results
for row in results:
    print(row)

# Close the connection
connection.close()