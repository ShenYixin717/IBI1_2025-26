# Pseudo-code Planning
# 1. Define user parameters: age, weight, gender, serum creatinine concentration (Cr)
# 2. Validate input parameters:
#    - Age < 100 years
#    - 20kg < weight < 80kg
#    - 0 < Cr < 100 μmol/l
#    - Gender must be "male" or "female"
# 3. If validation fails, print specific error message
# 4. If validation passes, calculate CrCl using the formula:
#    - Male: CrCl = (140 - age) * weight / (72 * Cr)
#    - Female: CrCl = [(140 - age) * weight / (72 * Cr)] * 0.85
# 5. Print the final calculated result

# 1. Define user parameters (modify these values for testing)
age = 45               # Age (years)
weight = 65            # Weight (kg)
gender = "female"      # Gender: "male" or "female"
cr = 80                # Serum creatinine concentration (μmol/l)

# 2. Input validation
is_valid = True
error_msg = ""
# Validate age
if age >= 100:
    is_valid = False
    error_msg = "Age must be less than 100 years."
# Validate weight
elif weight <= 20 or weight >= 80:
    is_valid = False
    error_msg = "Weight must be between 20kg and 80kg."
# Validate creatinine concentration
elif cr <= 0 or cr >= 100:
    is_valid = False
    error_msg = "Creatinine concentration must be between 0 μmol/l and 100 μmol/l."
# Validate gender
elif gender not in ["male", "female"]:
    is_valid = False
    error_msg = "Gender must be 'male' or 'female'."

# 3. Calculate CrCl if validation passes; otherwise, print error
if is_valid:
    # Base formula calculation
    crcl_base = (140 - age) * weight / (72 * cr)
    # Apply gender correction factor for female patients
    if gender == "female":
        crcl = crcl_base * 0.85
    else:
        crcl = crcl_base
    # Print result (rounded to 2 decimal places for clinical precision)
    print(f"Calculated Creatinine Clearance (CrCl): {crcl:.2f} ml/min")
else:
    # Print error message
    print(f"Input parameter error: {error_msg} Please correct and recalculate.")
