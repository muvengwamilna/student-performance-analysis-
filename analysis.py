# Project 1: Student Performance Data Analysis
# Simple beginner-friendly analysis using Python and Pandas.

import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the dataset
data = pd.read_csv("student_performance.csv")

# 2. View the data
print("First five rows:")
print(data.head())

# 3. Check the size and missing values
print("\nDataset shape:", data.shape)
print("\nMissing values:")
print(data.isnull().sum())

# 4. Basic statistics
print("\nBasic statistics:")
print(data.describe())

# 5. Average scores
print("\nAverage values:")
print("Average attendance:", round(data["Attendance_Percent"].mean(), 2))
print("Average study hours:", round(data["Study_Hours_Per_Week"].mean(), 2))
print("Average assignment score:", round(data["Assignment_Score"].mean(), 2))
print("Average exam score:", round(data["Exam_Score"].mean(), 2))

# 6. Find students with exam scores of 50 or more
passed = data[data["Exam_Score"] >= 50]
print("\nNumber of students with exam scores of 50 or more:", len(passed))

# 7. Find the student with the highest exam score
best_student = data.loc[data["Exam_Score"].idxmax()]
print("\nStudent with the highest exam score:")
print(best_student)

# 8. Compare attendance and exam performance
plt.figure(figsize=(7, 5))
plt.scatter(data["Attendance_Percent"], data["Exam_Score"])
plt.xlabel("Attendance (%)")
plt.ylabel("Exam Score")
plt.title("Attendance and Exam Performance")
plt.tight_layout()
plt.show()

# 9. Compare study hours and exam performance
plt.figure(figsize=(7, 5))
plt.scatter(data["Study_Hours_Per_Week"], data["Exam_Score"])
plt.xlabel("Study Hours Per Week")
plt.ylabel("Exam Score")
plt.title("Study Hours and Exam Performance")
plt.tight_layout()
plt.show()
