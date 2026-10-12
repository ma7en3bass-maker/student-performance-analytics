"""Student Performance Analytics System - main program."""

import pandas as pd
import functions as fn

pd.set_option("display.width", 200)
pd.set_option("display.max_columns", None)


def heading(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


def main():
    # Step 1 & 2: load and inspect data
    df = fn.load_data("students.csv")
    heading("1. DATASET OVERVIEW")
    print(f"Records : {df.shape[0]}")
    print(f"Columns : {list(df.columns)}")
    print("\nFirst 5 records:")
    print(df.head())
    print(f"\nMissing values: {int(df.isnull().sum().sum())}")

    # Step 3: process
    df = fn.process_data(df)
    heading("2. STUDENT RESULTS (Total, Average, Grade, Result)")
    print(df[["Student_ID", "Name", "Department", "Total", "Average",
              "Grade", "Result", "Attendance_Status"]].to_string(index=False))

    # Step 4: analysis
    stats = fn.class_statistics(df)
    heading("3. CLASS STATISTICS")
    print(f"Overall class average : {stats['class_average']}")
    print(f"Highest total marks   : {stats['highest_total']} / "
          f"{len(fn.SUBJECTS) * fn.MAX_MARKS_PER_SUBJECT}")
    print(f"Lowest total marks    : {stats['lowest_total']}")
    print(f"Highest average       : {stats['topper_name']} ({stats['topper_average']})")
    print(f"Lowest average        : {stats['lowest_name']} ({stats['lowest_average']})")
    print(f"Students passed       : {stats['passed']}")
    print(f"Students failed       : {stats['failed']}")
    print(f"Pass percentage       : {stats['pass_percentage']}%")

    heading("4. GRADE DISTRIBUTION")
    order = ["A+", "A", "B", "C", "D", "E", "F"]
    print(df["Grade"].value_counts().reindex(order, fill_value=0).to_string())

    heading("5. SUBJECT-WISE PERFORMANCE")
    sub = fn.subject_analysis(df)
    print(sub.to_string(index=False))
    best = sub.loc[sub["Average"].idxmax()]
    weak = sub.loc[sub["Average"].idxmin()]
    print(f"\nBest subject (highest average)  : {best['Subject']} ({best['Average']})")
    print(f"Weakest subject (lowest average): {weak['Subject']} ({weak['Average']})")

    heading("6. DEPARTMENT-WISE PERFORMANCE")
    print(fn.department_analysis(df))

    heading("7. TOP 5 PERFORMERS")
    print(fn.top_performers(df, 5).to_string(index=False))

    heading("8. STUDENTS WHO FAILED")
    failed = df[df["Result"] == "Fail"]
    print(failed[["Student_ID", "Name", "Department", "Average"]].to_string(index=False))

    heading("9. ATTENDANCE SHORTAGE (below 75%)")
    short = df[df["Attendance_Status"] == "Shortage"]
    print(short[["Student_ID", "Name", "Attendance"]].to_string(index=False))

    # Save processed results
    df.to_csv("results.csv", index=False)
    print("\nProcessed results saved to results.csv")


if __name__ == "__main__":
    main()
