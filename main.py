import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = "Data/NCD_RisC_Lancet_2024_Diabetes_age_specific_countries.csv"
data = pd.read_csv(file_path)

# Filter data for the year 2022
data_2022 = data[data["Year"] == 2022]

# 1. Global Analysis: Trends over time
global_trend = data.groupby("Year")["Prevalence of diabetes"].mean().reset_index()

#Calculate percentage increase
start_year = global_trend.iloc[0]
end_year = global_trend.iloc[-1]
global_increase = ((end_year["Prevalence of diabetes"] - start_year["Prevalence of diabetes"]) / start_year["Prevalence of diabetes"]) * 100

# Visualization: Global trend
plt.figure(figsize=(10, 6))
sns.lineplot(data=global_trend, x="Year", y="Prevalence of diabetes")
plt.title("Global Diabetes Prevalence Over Time")
plt.xlabel("Year")
plt.ylabel("Prevalence (%)")
plt.grid()
plt.show()

print(f"Global diabetes prevalence increased by {global_increase:.2f}% from {start_year['Year']} to {end_year['Year']}.")

# 2. Top 10 and 10 Countries with the Lowest Prevalence in 2022
country_2022_avg = data_2022.groupby("Country/Region/World")["Prevalence of diabetes"].mean().reset_index()
top_10_countries = country_2022_avg.nlargest(10, "Prevalence of diabetes")
lowest_10_countries = country_2022_avg.nsmallest(10, "Prevalence of diabetes")

# Visualization: Top 10 Countries
plt.figure(figsize=(10, 6))
sns.barplot(data=top_10_countries, x="Prevalence of diabetes", y="Country/Region/World", palette="Reds_r")
plt.title("Top 10 Countries with Highest Diabetes Prevalence (2022)")
plt.xlabel("Prevalence (%)")
plt.ylabel("Country")
plt.grid()
plt.show()

# Visualization: 10 Countries with the Lowest Prevalence
plt.figure(figsize=(10, 6))
sns.barplot(data=lowest_10_countries, x="Prevalence of diabetes", y="Country/Region/World", palette="Greens")
plt.title("10 Countries with the Lowest Diabetes Prevalence (2022)")
plt.xlabel("Prevalence (%)")
plt.ylabel("Country")
plt.grid()
plt.show()

print("Top 10 Countries with Highest Diabetes Prevalence in 2022:")
print(top_10_countries)

print("\n10 Countries with the Lowest Diabetes Prevalence in 2022:")
print(lowest_10_countries)

# 3. U.S. Age Group Analysis
us_data = data[data["Country/Region/World"] == "United States of America"]
us_age_group = us_data.groupby("Age")["Prevalence of diabetes"].mean().reset_index()

# Age group with the highest prevalence
highest_age_group = us_age_group.loc[us_age_group["Prevalence of diabetes"].idxmax()]

# Visualization: Age group prevalence
plt.figure(figsize=(10, 6))
sns.barplot(data=us_age_group, x="Age", y="Prevalence of diabetes", palette="viridis")
plt.title("Diabetes Prevalence by Age Group in the U.S.")
plt.xlabel("Age Group")
plt.ylabel("Prevalence (%)")
plt.xticks(rotation=45)
plt.grid()
plt.show()

print(f"The age group with the highest diabetes prevalence in the U.S. is {highest_age_group['Age']} with a prevalence of {highest_age_group['Prevalence of diabetes']:.2f}%.")

# Summary of Insights
print("\nSummary of Insights:")
print(f"1. Global diabetes prevalence increased by {global_increase:.2f}% from {start_year['Year']} to {end_year['Year']}.")
print(f"2. Top 10 countries with the highest diabetes prevalence in 2022 are:\n{top_10_countries['Country/Region/World'].values}.")
print(f"3. 10 countries with the lowest diabetes prevalence in 2022 are:\n{lowest_10_countries['Country/Region/World'].values}.")
print(f"4. In the U.S., the age group with the highest prevalence is {highest_age_group['Age']} with {highest_age_group['Prevalence of diabetes']:.2f}%.")
