
import numpy as np


def calculate_total_average(df, subjects):
    df["Total"] = df[subjects].sum(axis=1)
    df["Average"] = np.round(df[subjects].mean(axis=1), 2)
    return df


def assign_grade(average):
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
    else:
        return "F"


def check_result(average):
    if average >= 40:
        return "Pass"
    return "Fail"


def add_grades_and_results(df):
    df["Grade"] = df["Average"].apply(assign_grade)
    df["Result"] = df["Average"].apply(check_result)
    return df


def get_class_summary(df):
    highest_student = df.loc[df["Average"].max()]
    lowest_student = df.loc[df["Average"].min()]
    class_average = np.round(df["Average"].mean(), 2)

    pass_count = (df["Result"] == "Pass").sum()
    fail_count = (df["Result"] == "Fail").sum()

    return (
        highest_student,
        lowest_student,
        class_average,
        pass_count,
        fail_count
    )


def get_subject_averages(df, subjects):
    return np.round(df[subjects].mean(), 2)


def get_top_students(df, number=5):
    return df.sort_values(
        by="Average",
        ascending=False
    ).head(number)


def save_report(df, filename):
    report_columns = [
        "Student_ID", "Name", "Python", "Maths",
        "DBMS", "AI", "Total", "Average",
        "Grade", "Result", "Attendance"
    ]

    df[report_columns].to_csv(filename, index=False)
