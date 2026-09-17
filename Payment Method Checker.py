# ====================== PAYMENT METHOD CHECKER ========================
# AUTHOR: JAIDEN MARS S. TAULI
# SECTION: 8-CAMIA
# SEPTEMBER 17 2026

# LIST OF VALID PAYMENT METHODS
Valid_mthod = ["Cash","cash","Card","card","Gcash","gcash"]

# INPUT STAGE
pymnt = input("Enter your payment method: ")

# SELECTION STRUCTURE AND INPUT VALIDATION STAGE
if pymnt in Valid_mthod:
    print("Valid payment method.")
else:
    print("Invalid payment method.")