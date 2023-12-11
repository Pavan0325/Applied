import pandas as pd
import matplotlib.pyplot as plt

from Dataframe import read_and_clean_data

# Assuming df_years is the DataFrame with years as columns
# Replace 'your_dataset.csv' with the actual path to your downloaded CSV file
df_years, _ = read_and_clean_data(r'C:\Users\USER\Documents\WORK\ME\Pavan\P_Data_Extract_From_World_Development_Indicators.csv')

# Select a few countries for analysis
selected_countries = ['Afghanistan', 'Albania', 'Argentina', 'Australia', 'Brazil']

# Extract data for selected countries
df_selected_countries = df_years[selected_countries]

# Transpose the DataFrame to have indicators as columns
df_selected_countries_transposed = df_selected_countries.transpose()

# Calculate variance and correlation
variance = df_selected_countries.var()
correlation_matrix = df_selected_countries.corr()

# Plotting Variance Trajectories
df_selected_countries_transposed.plot(kind='line', title='Trajectory of Indicators for Selected Countries')
plt.ylabel('Value')
plt.xlabel('Year')
plt.legend(title='Indicator')
plt.show()

# Plotting Correlation
plt.figure(figsize=(10, 6))
plt.imshow(correlation_matrix, cmap='coolwarm', interpolation='none')
plt.colorbar()
plt.xticks(range(len(selected_countries)), selected_countries, rotation=45)
plt.yticks(range(len(selected_countries)), selected_countries)
plt.title('Correlation Matrix for Selected Countries')
plt.show()

# Print Summary Statistics and Standard Deviation
print("Summary Statistics:")
print(df_selected_countries.describe())

print("\nStandard Deviation:")
print(df_selected_countries.std())
