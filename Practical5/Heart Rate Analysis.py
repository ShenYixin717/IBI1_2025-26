'''
1.Heart rate data initialization and basic statistics calculation
2.Heart rate classification (low/normal/high) and category counting
3.Identification of the largest heart rate category
4.Pie chart creation for visualizing category proportions
5.Formatted output of all results
'''

import matplotlib.pyplot as plt

# Heart Rate Analysis
heart_rates	=[72,60,126,85,90,59,76,131,88,121,64]
print(f"There are {len(heart_rates)} heart rate measurements in the dataset and the mean heart rate is {sum(heart_rates)/len(heart_rates):.2f} bpm.")

# Classify each heart rate measurement and count how many fall into each category
n_low=0
n_normal=0
n_high=0
for i in heart_rates:
    if i < 60:
        print(f"{i} bpm is below the normal range.")
        n_low += 1
    elif 60 <= i <= 100:
        print(f"{i} bpm is within the normal range.")
        n_normal += 1
    else:
        print(f"{i} bpm is above the normal range.")
        n_high += 1
print(f"\nThere are {n_low} heart rate measurements below the normal range.")
print(f"There are {n_normal} heart rate measurements within the normal range.")
print(f"There are {n_high} heart rate measurements above the normal range.")

#stating which category	is	the	largest
n={"low":n_low,"normal":n_normal,"high":n_high}
largest_category=max(n, key=n.get)
print(f"\nThe largest category is '{largest_category}' with {n[largest_category]}")

#create	a pie chart
labels = ['Below Normal', 'Normal', 'Above Normal']
sizes = [n_low, n_normal, n_high]
colors = ['lightcoral', 'lightgreen', 'lightblue']
plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title('Heart Rate Categories')
plt.axis('equal')
plt.show()