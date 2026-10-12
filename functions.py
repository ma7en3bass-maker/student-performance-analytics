"""Reusable functions for the Student Performance Analytics System."""

import numpy as np
import pandas as pd

# ---------- Configuration ----------
SUBJECTS = ["Maths", "Physics", "Chemistry", "English", "Computer_Science"]
MAX_MARKS_PER_SUBJECT = 100
PASS_MARKS = 40           # a student must score at least this in EVERY subject
MIN_ATTENDANCE = 75       # attendance (%) required to avoid a shortage warning


def load_data(file_path):
    """Read the student CSV file into a Pandas DataFrame."""
    return pd.read_csv(file_path)


def calculate_total_and_average(df):
    """Add Total and Average columns using NumPy on the subject marks."""
    marks = df[SUBJECTS].to_numpy()                       # DataFrame -> NumPy array
    df["Total"] = np.sum(marks, axis=1)                   # row-wise total
    df["Average"] = np.round(np.mean(marks, axis=1), 2)   # row-wise average
    return df


def assign_grade(average):
    """Grading rule based on the average marks of a student."""
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    elif average >= 40:
        return "E"
    return "F"


def add_grades(df):
    """Loop over every student and store the grade in a new column."""
    grades = []
    for avg in df["Average"]:
        grades.append(assign_grade(avg))
    df["Grade"] = grades
    return df


def check_pass_fail(row):
    """Pass only if the student scored >= PASS_MARKS in every subject."""
    for subject in SUBJECTS:
        if row[subject] < PASS_MARKS:
            return "Fail"
    return "Pass"


def add_pass_fail(df):
    """Add a Result column (Pass / Fail) for each student."""
    df["Result"] = df.apply(check_pass_fail, axis=1)
    return df


def add_attendance_status(df):
    """Flag students whose attendance is below the required minimum."""
    df["Attendance_Status"] = np.where(df["Attendance"] >= MIN_ATTENDANCE, "OK", "Shortage")
    return df


def process_data(df):
    """Run the full processing pipeline."""
    df = calculate_total_and_average(df)
    df = add_grades(df)
    df = add_pass_fail(df)
    df = add_attendance_status(df)
    return df


def class_statistics(df):
    """Highest, lowest and average performance of the class."""
    top = df.loc[df["Average"].idxmax()]
    bottom = df.loc[df["Average"].idxmin()]
    return {
        "highest_total": int(df["Total"].max()),
        "lowest_total": int(df["Total"].min()),
        "class_average": round(float(np.mean(df["Average"])), 2),
        "topper_name": top["Name"],
        "topper_average": top["Average"],
        "lowest_name": bottom["Name"],
        "lowest_average": bottom["Average"],
        "passed": int((df["Result"] == "Pass").sum()),
        "failed": int((df["Result"] == "Fail").sum()),
        "pass_percentage": round(float((df["Result"] == "Pass").mean() * 100), 2),
    }


def subject_analysis(df):
    """Average, highest, lowest marks and pass count for every subject."""
    rows = []
    for subject in SUBJECTS:
        scores = df[subject].to_numpy()
        rows.append({
            "Subject": subject,
            "Average": round(float(np.mean(scores)), 2),
            "Highest": int(np.max(scores)),
            "Lowest": int(np.min(scores)),
            "Students_Passed": int(np.sum(scores >= PASS_MARKS)),
        })
    return pd.DataFrame(rows)


def department_analysis(df):
    """Average marks and pass count grouped by department."""
    summary = df.groupby("Department").agg(
        Students=("Student_ID", "count"),
        Avg_Marks=("Average", "mean"),
        Avg_Attendance=("Attendance", "mean"),
        Passed=("Result", lambda r: (r == "Pass").sum()),
    ).round(2)
    return summary.sort_values("Avg_Marks", ascending=False)


def top_performers(df, n=5):
    """Return the top n students ranked by average marks."""
    top = df.sort_values("Average", ascending=False).head(n)
    return top[["Student_ID", "Name", "Department", "Total", "Average", "Grade"]]
