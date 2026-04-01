# 4.1 Scotland Population Growth Calculation
# Scotland population in 2004 (millions)
a = 5.08
# Scotland population in 2014 (millions)
b = 5.33
# Scotland population in 2024 (millions)
c = 5.55

# Population change from 2004 to 2014
d = b - a
# Population change from 2014 to 2024
e = c - b

# Compare the two population changes
print(f"Population change 2004-2014: {d} million")
print(f"Population change 2014-2024: {e} million")
print(f"Result of d > e: {d > e}")

# Comment: Analysis of population growth trend
# d = 0.25, e = 0.22. Since e < d, Scotland's population growth rate has slowed down.

# 4.2 Boolean Operations
# Define boolean variables
X = True
Y = False
# Calculate W as the logical OR of X and Y
W = X or Y

# Print the result of W
print(f"\nWhen X={X}, Y={Y}, W(X or Y) = {W}")
# Comment: Truth table for logical OR (W = X or Y)
# X=True, Y=True → W=True
# X=True, Y=False → W=True
# X=False, Y=True → W=True
# X=False, Y=False → W=False
# Logical OR: Result is True if at least one operand is True.
