# Activity 1: Functions and Modular Programming in Python
# TAULI, JAIDEN MARS S.
# 8-CAMIA



# Input Stage:


def display_header():
    print("STUDENT PERFORMANCE REPORT")

def get_student_info():
    name = str(input("Enter student name: "))
    assess1 = float(input("Enter assessment 1: "))
    assess2 = float(input("Enter assessment 2: "))
    assess3 = float(input("Enter assessment 3: "))

    return name, assess1, assess2, assess3

# Data processing:

def evaluate_performance():
    name, assess1, assess2, assess3 = get_student_info()
    avg = (assess1 + assess2 + assess3)/3
    avg = round(avg,2)
    name = name

    if 90 <= avg <= 100:
        perf = "Outstanding"
    elif 85 <= avg <= 90:
        perf = "Very Satisfactory"
    elif 80 <= avg <= 85:
        perf = "Satisfactory"
    elif 75 <= avg <= 80:
        perf = "Fairly Satisfactory"
    else:
        perf = "Needs Improvement"

    return name, assess1, assess2, assess3, avg, perf

# Output stage:

def display_report():
    name, assess1, assess2, assess3, avg, perf = evaluate_performance()

    display_header()
    print(f"Student Name: {name}")
    print(f"Assessment scores: {assess1}, {assess2}, {assess3}")
    print(f"Average score: {avg}")
    print(f"Performance Level:{ perf}")

display_report()