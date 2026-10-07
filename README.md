# Student Performance Prediction

## About the Project

This project is made to analyze student performance and predict the final score of a student using machine learning.

I used Python for data analysis and model building, SQLite for SQL queries, and Power BI to create a dashboard.

## What I Did

- Checked and analyzed the student data
- Found relationships between different factors and final score
- Built a Linear Regression model to predict final score
- Stored the data in SQLite and ran SQL queries
- Created a Power BI dashboard to visualize the results

## Tools Used

- Python
- Pandas
- Matplotlib
- Scikit-learn
- SQLite
- SQL
- Power BI

## Dataset

The dataset contains 500 student records.

Some of the columns are:

- Study Hours
- Attendance
- Previous Score
- Assignment Score
- Sleep Hours
- Internet Hours
- Participation Score
- Final Score
- Performance Category

## Machine Learning

I used Linear Regression for predicting the final score.

The model results were:

- MAE: 3.81
- R² Score: 0.73

## Power BI Dashboard

The dashboard shows:

- Total number of students
- Average final score
- Average study hours
- Average attendance
- Performance categories
- Study hours vs final score
- Attendance vs final score
- Student details

## How to Run

First install the required libraries:
pip install -r requirements.txt

Run the analysis:
python src/analysis.py

Run the prediction model:
python src/model.py

Create the database:
python sql/student_database.py

Author
Sneha Adhav