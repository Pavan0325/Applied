import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from Dataframe import read_and_clean_data

# Assuming df_years is the DataFrame with years as columns
# Replace 'your_dataset.csv' with the actual path to your downloaded CSV file
df_years, _ = read_and_clean_data('your_dataset.csv')

# Select a few countries for analysis
selected_countries = ['Afghanistan', 'Albania', 'Argentina', 'Australia', 'Brazil']

# Extract data for selected countries
df_selected_countries = df_years[selected_countries]

# Calculate variance and correlation
variance = df_selected_countries.var()
correlation_matrix = df_selected_countries.corr()

# Plotting Variance
variance.plot(kind='bar', title='Variance of Indicators for Selected Countries')
plt.ylabel('Variance')
plt.xlabel('Indicators')
plt.show()

# Plotting Correlation
plt.figure(figsize=(10, 6))
plt.imshow(correlation_matrix, cmap='coolwarm', interpolation='none')
plt.colorbar()
plt.xticks(range(len(selected_countries)), selected_countries, rotation=45)
plt.yticks(range(len(selected_countries)), selected_countries)
plt.title('Correlation Matrix for Selected Countries')
plt.show()
