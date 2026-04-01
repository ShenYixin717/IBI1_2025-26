# What does this piece of code do?
# Answer: It generates ten random integers less than ten and sums them up. 

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

total_rand = 0
progress=0
while progress<=10:
	progress+=1                      # Loop runs 10 times, incrementing progress by 1 each time
	n = randint(1,10)                # Generate a random integer between 1 and 10
	total_rand+=n                    # Add the generated random integer to the total sum

print(total_rand)                    # Print the total sum of the ten random integers generated.

