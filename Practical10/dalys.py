# Import required libraries
import os
import pandas as pd
import matplotlib.pyplot as plt

# Import the dataset
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dalys-rate-from-all-causes.csv")
dalys_data = pd.read_csv(path)

# Show the 3rd and 4th columns (Year and DALYs) for the first 10 rows (inclusive)
print(dalys_data.iloc[0:10, 2:4])
# 1998 reported the maximum DALYs across the first 10 years for which DALYs were recorded in Afghanistan.

# Boolean selection to get all recorded years for Zimbabwe
zimbabwe_filter = dalys_data["Entity"] == "Zimbabwe"
zimbabwe_years = dalys_data.loc[zimbabwe_filter, "Year"]
print("Recording Year", zimbabwe_years.tolist())
print("The first year:", zimbabwe_years.min(), " The last year:", zimbabwe_years.max())
# First year: 1990
# Last year: 2019

# Find countries with maximum and minimum DALYs in 2019
recent_data = dalys_data.loc[dalys_data.Year == 2019, ["Entity", "DALYs"]]
max_dalys_country = recent_data.loc[recent_data.DALYs.idxmax(), "Entity"]
min_dalys_country = recent_data.loc[recent_data.DALYs.idxmin(), "Entity"]
print("Max 2019 DALYs country:", max_dalys_country)
print("Min 2019 DALYs country:", min_dalys_country)
# Max DALYs country: Lesotho
# Min DALYs country: Singapore

# Plot time series of DALYs for the minimum DALYs country
country_time_series = dalys_data.loc[dalys_data.Entity == min_dalys_country]
plt.plot(country_time_series.Year, country_time_series.DALYs, 'b+')
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.title("DALYs over time in the minimum country")
plt.savefig("DALYs over time in the minimum country.png")
plt.show()

# Question: What is the distribution of DALYs across all countries in 2019?
plt.boxplot(recent_data.DALYs.dropna())
plt.title("2019 DALYs Distribution Across All Countries")
plt.xlabel("2019 Global DALYs")
plt.ylabel("DALYs Value")
plt.savefig("2019 DALYs Distribution.png")
plt.show()