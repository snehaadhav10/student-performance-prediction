import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data/student_data.csv")

print(data.head())
print(data.shape)
print(data.columns)
data.info()

print(data.isnull().sum())
print("Duplicate rows:", data.duplicated().sum())
print(data.describe())

plt.scatter(data["attendance_percent"], data["final_score"])

plt.xlabel("Attendance Percentage")
plt.ylabel("Final Score")
plt.title("Attendance vs Final Score")

# Check correlation with final score
correlation = data.corr(numeric_only=True)

print("Correlation with Final Score:")
print(correlation["final_score"].sort_values(ascending=False))

# Attendance vs Final Score
plt.scatter(data["attendance_percent"], data["final_score"])

plt.xlabel("Attendance Percentage")
plt.ylabel("Final Score")
plt.title("Attendance vs Final Score")

plt.show()