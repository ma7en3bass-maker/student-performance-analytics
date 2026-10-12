# Student Performance Analytics System

## 1. Project Title
**Student Performance Analytics System** (Python with AI – EWB Courses)

- Student Name: Mazen Abass
- Roll No: 2419000000179
- Batch: B.Tech CSE-AI

## 2. Objective
Teachers often have raw marks for many students but no quick way to see grades, pass/fail status, subject strengths and top performers. This project reads student data from a CSV file, processes it with NumPy and Pandas, and prints a clear report: totals, averages, grades, pass/fail statistics, subject-wise and department-wise performance, and top performers.

## 3. Technologies Used
- Python 3
- NumPy (numerical calculations)
- Pandas (DataFrame loading, grouping, analysis)

## 4. Dataset Description
`students.csv` has **20 student records** with these columns:

| Column | Meaning |
|---|---|
| Student_ID | Unique ID (S101–S120) |
| Name | Student name |
| Department | CSE, ECE, ME, CE or IT |
| Maths, Physics, Chemistry, English, Computer_Science | Marks out of 100 |
| Attendance | Attendance percentage |

The data is sample data created for this project.

## 5. Implementation
1. **Load data** – `load_data()` reads the CSV into a DataFrame; shape, columns and missing values are checked.
2. **Totals and averages** – `calculate_total_and_average()` converts the marks to a NumPy array and uses `np.sum` and `np.mean` with `axis=1`.
3. **Grades** – `add_grades()` loops over each student's average and calls `assign_grade()`.
   - A+ (90+), A (80–89), B (70–79), C (60–69), D (50–59), E (40–49), F (below 40)
4. **Pass/Fail** – `check_pass_fail()` uses a loop: a student **passes only if they score at least 40 in every subject**.
5. **Attendance** – `np.where` flags students below 75% as "Shortage".
6. **Analysis** – `class_statistics()`, `subject_analysis()` (NumPy per subject), `department_analysis()` (Pandas `groupby`) and `top_performers()` (sorting).
7. **Output** – `main.py` prints all sections and saves the processed table to `results.csv`.

## 6. Key Features
- Reusable functions in `functions.py`
- Total and average marks per student
- Rule-based grading and pass/fail
- Highest, lowest and class-average performance
- Subject-wise and department-wise analysis
- Top 5 performers, failed students list, attendance shortage list

## 7. How to Run
```bash
pip install -r requirements.txt
python main.py
```

## 8. Output
```

======================================================================
1. DATASET OVERVIEW
======================================================================
Records : 20
Columns : ['Student_ID', 'Name', 'Department', 'Maths', 'Physics', 'Chemistry', 'English', 'Computer_Science', 'Attendance']

First 5 records:
  Student_ID          Name Department  Maths  Physics  Chemistry  English  Computer_Science  Attendance
0       S101  Aarav Sharma        CSE     85       78         82       74                91          92
1       S102   Priya Verma        ECE     72       68         75       80                70          88
2       S103   Rohan Gupta         ME     55       48         60       65                58          76
3       S104  Ananya Singh        CSE     92       88         90       85                95          96
4       S105  Vikram Yadav         CE     38       45         42       50                40          64

Missing values: 0

======================================================================
2. STUDENT RESULTS (Total, Average, Grade, Result)
======================================================================
Student_ID           Name Department  Total  Average Grade Result Attendance_Status
      S101   Aarav Sharma        CSE    410     82.0     A   Pass                OK
      S102    Priya Verma        ECE    365     73.0     B   Pass                OK
      S103    Rohan Gupta         ME    286     57.2     D   Pass                OK
      S104   Ananya Singh        CSE    450     90.0    A+   Pass                OK
      S105   Vikram Yadav         CE    215     43.0     E   Fail          Shortage
      S106    Sneha Patel        ECE    350     70.0     B   Pass                OK
      S107    Karan Mehta         ME    244     48.8     E   Pass          Shortage
      S108     Neha Joshi        CSE    408     81.6     A   Pass                OK
      S109    Arjun Reddy         CE    301     60.2     C   Pass                OK
      S110   Pooja Mishra         IT    428     85.6     A   Pass                OK
      S111    Rahul Kumar         IT    214     42.8     E   Fail          Shortage
      S112     Divya Nair        ECE    371     74.2     B   Pass                OK
      S113  Siddharth Rao         ME    299     59.8     D   Pass                OK
      S114     Kavya Iyer        CSE    421     84.2     A   Pass                OK
      S115  Manish Tiwari         CE    251     50.2     D   Pass          Shortage
      S116    Isha Kapoor         IT    372     74.4     B   Pass                OK
      S117 Aditya Chauhan        CSE    315     63.0     C   Pass                OK
      S118     Riya Sinha        ECE    453     90.6    A+   Pass                OK
      S119  Harsh Agarwal         ME    225     45.0     E   Fail          Shortage
      S120   Meera Pillai         IT    392     78.4     B   Pass                OK

======================================================================
3. CLASS STATISTICS
======================================================================
Overall class average : 67.7
Highest total marks   : 453 / 500
Lowest total marks    : 214
Highest average       : Riya Sinha (90.6)
Lowest average        : Rahul Kumar (42.8)
Students passed       : 17
Students failed       : 3
Pass percentage       : 85.0%

======================================================================
4. GRADE DISTRIBUTION
======================================================================
Grade
A+    2
A     4
B     5
C     2
D     3
E     4
F     0

======================================================================
5. SUBJECT-WISE PERFORMANCE
======================================================================
         Subject  Average  Highest  Lowest  Students_Passed
           Maths    65.75       92      35               18
         Physics    65.45       89      39               19
       Chemistry    65.85       93      38               19
         English    71.35       90      50               20
Computer_Science    70.10       95      40               20

Best subject (highest average)  : English (71.35)
Weakest subject (lowest average): Physics (65.45)

======================================================================
6. DEPARTMENT-WISE PERFORMANCE
======================================================================
            Students  Avg_Marks  Avg_Attendance  Passed
Department                                             
CSE                5      80.16           89.60       5
ECE                4      76.95           89.75       4
IT                 4      70.30           82.00       3
ME                 4      52.70           72.50       3
CE                 3      51.13           70.67       2

======================================================================
7. TOP 5 PERFORMERS
======================================================================
Student_ID         Name Department  Total  Average Grade
      S118   Riya Sinha        ECE    453     90.6    A+
      S104 Ananya Singh        CSE    450     90.0    A+
      S110 Pooja Mishra         IT    428     85.6     A
      S114   Kavya Iyer        CSE    421     84.2     A
      S101 Aarav Sharma        CSE    410     82.0     A

======================================================================
8. STUDENTS WHO FAILED
======================================================================
Student_ID          Name Department  Average
      S105  Vikram Yadav         CE     43.0
      S111   Rahul Kumar         IT     42.8
      S119 Harsh Agarwal         ME     45.0

======================================================================
9. ATTENDANCE SHORTAGE (below 75%)
======================================================================
Student_ID          Name  Attendance
      S105  Vikram Yadav          64
      S107   Karan Mehta          70
      S111   Rahul Kumar          58
      S115 Manish Tiwari          68
      S119 Harsh Agarwal          66

Processed results saved to results.csv

```

## 9. Final Outcome
The program ran without errors on 20 records. It found a class average of 67.7, 17 of 20 students passing (85%), Riya Sinha as the top performer (90.6 average), English as the strongest subject and Physics as the weakest. CSE had the best department average, and every student with an attendance shortage was in the lower-performing group. The output is readable without opening the code.

## 10. Challenges & Learning
- **Defining pass/fail clearly:** a student can have an acceptable average but fail one subject, so I used a per-subject minimum of 40 and kept grading separate (based on average).
- **Combining NumPy and Pandas:** I learned to convert DataFrame columns to NumPy arrays for fast row-wise and column-wise calculations.
- **Organising code:** splitting logic into `functions.py` and keeping `main.py` for output made the code easier to test and read.

## 11. GitHub Repository
https://github.com/ma7en3bass-maker/student-performance-analytics

## Project Structure
```
student-performance-analytics/
├── main.py
├── functions.py
├── students.csv
├── results.csv        (generated when you run main.py)
├── requirements.txt
└── README.md
```
