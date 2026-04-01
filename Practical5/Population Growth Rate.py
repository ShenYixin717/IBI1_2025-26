'''
1.Library import and population dataset creation
2.Percentage population change calculation
3.Data sorting by growth rate
4.Identification of countries with largest population increase/decrease
5.Colored bar chart creation for visualizing changes
6.Automatic percentage labels on chart bars

'''

import pandas as pd
import matplotlib.pyplot as plt

#create data box
data = {
    "Country": ["UK", "China", "Italy", "Brazil", "USA"],
    "Population_2020": [66.7, 1426, 59.4, 208.6, 331.6],
    "Population_2024": [69.2, 1410, 58.9, 212.0, 340.1]
}
df = pd.DataFrame(data)

#sort the data by percentage change
df["Percent_Change"] = ((df["Population_2024"] - df["Population_2020"]) / df["Population_2020"]) * 100

#sort the data by percentage change
print("Percentage Population Change for Each Country:")
print(df[["Country", "Percent_Change"]].round(2))
print("\nSorted Population Changes (Descending):")
df_sorted = df.sort_values(by="Percent_Change", ascending=False)
print(df_sorted[["Country", "Percent_Change"]].round(2))

#Identify the countries with the largest increase and decrease in population
max_increase = df_sorted.iloc[0]
max_decrease = df_sorted.iloc[-1]
print(f"\nCountry with Largest Increase: {max_increase['Country']} ({max_increase['Percent_Change'].round(2)}%)")
print(f"Country with Largest Decrease: {max_decrease['Country']} ({max_decrease['Percent_Change'].round(2)}%)")

#Create a bar chart to visualize the population changes
plt.figure(figsize=(10, 6))
bars = plt.bar(df_sorted["Country"], df_sorted["Percent_Change"], color=["green" if x > 0 else "red" for x in df_sorted["Percent_Change"]])

#Add percentage labels on top of the bars
plt.xlabel("Country", fontsize=12)
plt.ylabel("Population Change (%)", fontsize=12)
plt.title("Population Change by Country (2020-2024)", fontsize=14)
plt.grid(axis='y', linestyle='--', alpha=0.7)

#Add percentage labels on top of the bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{height:.2f}%',
             ha='center', va='bottom')

plt.tight_layout()
plt.show()