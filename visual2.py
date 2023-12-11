import pandas as pd
import matplotlib.pyplot as plt

from Dataframe import read_and_clean_data

# Assuming df_years is the DataFrame with years as columns
# Replace 'your_dataset.csv' with the actual path to your downloaded CSV file
df_years, _ = read_and_clean_data('your_dataset.csv')

# Select a few countries for analysis
selected_countries = ['Afghanistan', 'Albania', 'Argentina', 'Australia', 'Brazil']

# Extract data for selected countries
df_selected_countries = df_years[selected_countries]

# Transpose the DataFrame for time series analysis
df_selected_countries_transposed = df_selected_countries.transpose()

# Plotting Time Series
df_selected_countries_transposed.plot(title='Time Series of Indicators for Selected Countries')
plt.ylabel('Values')
plt.xlabel('Years')
plt.show()
