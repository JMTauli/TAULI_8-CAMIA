import re
# Activity number 6
# JAIDEN MARS S. TAULI
# 8-CAMIA



# Problem 3:
# =============== STUDENT ID CHECKER ===============

# INPUT STAGE

ID = input("Please enter your student ID: ")

pttrn = r"\d{4}-\d{4}"

if re.fullmatch(pttrn,ID):
    print("Valid Student ID")
else:
    print("Invalid Student ID,please follow the given format")