# Practical 4 - Infection Rate Time Simulation
# Pseudo-code Planning
# 1. Define initial infected count, daily growth rate, and total class size
# 2. Initialize day counter and current infected count
# 3. Loop: calculate daily new infected count = current infected count * (1 + growth rate)
# 4. Increment day counter and print daily infection data
# 5. Stop loop when current infected count >= total class size
# 6. Print total days required to infect all students

# Define basic parameters
initial_infected = 5  # Initial number of infected students
growth_rate = 0.4     # Daily infection growth rate (40%)
total_students = 91   # Total number of students in the class

# Initialize simulation variables
current_infected = initial_infected
days = 0

# Print initial simulation info
print("IBI1 Class Infection Simulation")
print(f"Initial infected: {initial_infected}, Daily growth rate: {growth_rate*100}%")
print("-" * 30)

# Loop to calculate daily infection numbers
while current_infected < total_students:
    days += 1
    # Update current infected count (rounded to 1 decimal place for realism)
    current_infected = current_infected * (1 + growth_rate)
    # Print daily result
    print(f"Day {days}: Infected students = {current_infected:.1f}")

# Loop ends, print total days required
print("-" * 30)
print(f"All the {total_students} students would be infected after {days} days")
