# Activity number 6
# JAIDEN MARS S. TAULI
# 8-CAMIA



# Problem 4:
# =============== PIN VALIDATOR ===============

# INPUT STAGE

Pin = input("Please enter your PIN (6 digits only): ")

if len(Pin) == 6 and Pin.isdigit():
    print("PIN is valid")
else:
    print("PIN is not valid, please enter exactly 6 digits only")