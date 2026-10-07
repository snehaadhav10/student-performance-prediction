import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score


# Load the dataset
data = pd.read_csv("data/student_data.csv")


# Select input features
X = data[
    [
        "study_hours",
        "attendance_percent",
        "previous_score",
        "assignment_score",
        "sleep_hours",
        "internet_hours",
        "participation_score"
    ]
]

# Select the target
y = data["final_score"]


# Split the data into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Create the model
model = LinearRegression()


# Train the model
model.fit(X_train, y_train)


# Make predictions
predictions = model.predict(X_test)


# Check model performance
mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)


print("Mean Absolute Error:", mae)
print("R2 Score:", r2)

# Predict performance for a new student

new_student = pd.DataFrame([{
    "study_hours": 6,
    "attendance_percent": 85,
    "previous_score": 75,
    "assignment_score": 80,
    "sleep_hours": 7,
    "internet_hours": 3,
    "participation_score": 8
}])
predicted_score = model.predict(new_student)
score = predicted_score[0]

if score >= 90:
    category = "Excellent"
elif score >= 75:
    category = "Good"
elif score >= 60:
    category = "Average"
else:
    category = "Needs Improvement"

print("Predicted Final Score:", score)
print("Predicted Performance:", category)