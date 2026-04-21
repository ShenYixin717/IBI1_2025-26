# Import the function
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Import the file
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dalys-rate-from-all-causes.csv")
    # I'm not sure whether the code would work if I write the code as the guidance written, 
    # so I use another way to import the file.
    # I am good at data processing I think, you can see the same procedure in my former practical.
dalys_data = pd.read_csv(path)

# Show the third and fourth columns (the year and the DALYs) for the first 10 rows (inclusive)
print(dalys_data.iloc[0:10,2:4])
    #1990 reported the maximum DALYs across the first 10 years for which DALYs were recorded in Afghanistan.

# Filter 2019 data
recent_data = dalys_data.loc[dalys_data.Year == 2019, ["Entity", "DALYs"]]

# Boolean selection for columns
zimbabwe_bool = dalys_data["Entity"] == "Zimbabwe"
zimbabwe_data = dalys_data.loc[zimbabwe_bool, "Year"]
print("Recording Year", zimbabwe_data.tolist())
print("The first year:", zimbabwe_data.min(), "The last year:", zimbabwe_data.max())
# First year: 1990
# Last year: 2019

# Find country with max and min DALYs in 2019
max_2019 = recent_data.loc[recent_data.DALYs.idxmax(), "Entity"]
min_2019 = recent_data.loc[recent_data.DALYs.idxmin(), "Entity"]
print("Max 2019 country:", max_2019)
print("Min 2019 country:", min_2019)
# Max DALYs country in 2019: [auto-filled by code]
# Min DALYs country in 2019: [auto-filled by code]

# Find max and min DALYs countries in 2019
max_country = recent_data.loc[recent_data.DALYs.idxmax()]
min_country = recent_data.loc[recent_data.DALYs.idxmin()]
print("Max 2019:", max_country)
print("Min 2019:", min_country)
# Max DALYs country: Lesotho
# Min DALYs country: Singapore

# Plot time series for one country
country_data = dalys_data.loc[dalys_data.Entity == min_country.Entity]
plt.plot(country_data.Year, country_data.DALYs, 'b+')
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.title("DALYs over time")
plt.show()

# Question: What is the DALYs distribution in 2019?
plt.boxplot(recent_data.DALYs.dropna())
plt.title("2019 DALYs Distribution")
plt.ylabel("DALYs")
plt.show()