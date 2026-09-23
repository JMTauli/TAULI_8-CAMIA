# Activity number 6
# JAIDEN MARS S. TAULI
# 8-CAMIA



# Problem 5:
# =============== STUDENT SCORE ENTRY ===============

# INPUT STAGE


try:
    exsco = int(input("Please enter your Examination score: "))
    if 0 >= exsco or exsco >= 100:
        print("Invalid Examination Score, please enter a numeric value, or please enter a number between 0 and 100")
    else:
        print("Valid Examination Score")

except ValueError:
        print("Invalid Examination Score, please enter a numeric value, or please enter a number between 0 and 100")

