# Activity 2
# Tauli, Jaiden Mars S.
# 8-CAMIA
# October, 15 2026

# Input Stage:

FirNum = int(input("Enter the first Number: "))
SecNum = int(input("Enter the second Number: "))
Sum = 0
Dif = 0

# Calculation Stage:

def calculate_sum():
    global Sum
    Sum = FirNum + SecNum
    return Sum

def calculate_difference():
    global Dif
    Dif = FirNum - SecNum
    return Dif

# Output Stage:

print(f"Sum: {calculate_sum()}")
print(f"Difference: {calculate_difference()}")