import pandas as pd

from functions import (
    calculate_total_average,
    add_grades_and_results,
    get_class_summary,
    get_subject_averages,
    get_top_students,
    save_report
    )


# Load the dataset
df = pd.read_csv("students.csv")
subjects = ["Python", "Maths", "DBMS", "AI"]

print("\n--- Student Dataset ---")
print(df.to_string(index=False))
print("\nTotal Students:", len(df))

# Calculate total, average, grade and result
df = calculate_total_average(df, subjects)
df = add_grades_and_results(df)

print("\n--- Student Performance Analysis ---")
print(
    df[["Student_ID", "Name", "Total",
        "Average", "Grade", "Result"]]
    .to_string(index=False)
)

# Class performance summary
(
    highest_student,
    lowest_student,
    class_average,
    pass_count,
    fail_count
) = get_class_summary(df)

print("\n--- Class Performance Analysis ---")
print("Highest Performer:", highest_student["Name"])
print("Highest Average:", highest_student["Average"])
print("Lowest Performer:", lowest_student["Name"])
print("Lowest Average:", lowest_student["Average"])
print("Class Average:", class_average)
print("Students Passed:", pass_count)
print("Students Failed:", fail_count)

# Subject-wise analysis
subject_averages = get_subject_averages(df, subjects)

print("\n--- Subject-Wise Performance ---")

# Loop through each subject and its average
for subject, average in subject_averages.items():
    print(f"{subject}: {average}")

print("Best Subject:", subject_averages.max())
print("Subject Needing Improvement:",subject_averages.min())

# Top 5 students
top_students = get_top_students(df)

print("\n--- Top 5 Performing Students ---")
print(
    top_students[["Student_ID", "Name", "Average", "Grade"]]
    .to_string(index=False)
)

# Save the final report
save_report(df, "student_performance_report.csv")
print("\nReport saved: student_performance_report.csv")