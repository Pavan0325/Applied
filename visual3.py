import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from Dataframe import read_and_clean_data

# Assuming df_years is the DataFrame with years as columns
# Replace 'your_dataset.csv' with the actual path to your downloaded CSV file
df_years, _ = read_and_clean_data('your_dataset.csv')

# Select 6 countries for analysis
selected_countries = ['Afghanistan', 'Albania', 'Argentina', 'Australia', 'Brazil', 'China']

# Extract data for selected countries
df_selected_countries = df_years[selected_countries]

# Calculate correlation matrix
correlation_matrix = df_selected_countries.corr()

# Define a custom color map
cmap = sns.diverging_palette(240, 10, as_cmap=True)

# Plotting Heatmap with colored boxes
plt.figure(figsize=(10, 8))
heatmap = sns.heatmap(correlation_matrix, annot=True, cmap=cmap, linewidths=.5, square=True, vmin=-1, vmax=1)

# Set axis labels
heatmap.set_xticklabels(heatmap.get_xticklabels(), rotation=45, horizontalalignment='right')
heatmap.set_yticklabels(heatmap.get_yticklabels(), rotation=0)

plt.title('Correlation Heatmap for Selected Countries')
plt.show()
