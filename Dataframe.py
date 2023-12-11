import pandas as pd

# Replace 'your_dataset.csv' with the actual path to your downloaded CSV file

df = pd.read_csv(r'C:\Users\USER\Documents\WORK\ME\Pavan\P_Data_Extract_From_World_Development_Indicators.csv')

# Transpose DataFrame with years as columns
df_years = df.set_index(['Series Name', 'Series Code', 'Country Name', 'Country Code']).transpose()

# Transpose DataFrame with countries as columns (replace swapaxes with transpose)
df_countries = df.set_index(['Series Name', 'Series Code', 'Country Name', 'Country Code']).transpose()

# Clean transposed DataFrames (example: converting values to numeric)
df_years = df_years.apply(pd.to_numeric, errors='coerce')
df_countries = df_countries.apply(pd.to_numeric, errors='coerce')


# Further cleaning steps as needed
def read_and_clean_data(filename):
    # Read the data
    df = pd.read_csv(r'C:\Users\USER\Documents\WORK\ME\Pavan\P_Data_Extract_From_World_Development_Indicators.csv')

    # Transpose DataFrames
    df_years = df.set_index(['Series Name', 'Series Code', 'Country Name', 'Country Code']).transpose()
    df_countries = df.set_index(['Series Name', 'Series Code', 'Country Name', 'Country Code']).transpose().swapaxes(0,
                                                                                                                     1)

    # Clean DataFrames
    df_years = df_years.apply(pd.to_numeric, errors='coerce')
    df_countries = df_countries.apply(pd.to_numeric, errors='coerce')

    return df_years, df_countries


print("Dataframe with years as columns:")
print(df_years)

print("\nDataframe with countries as columns:")
print(df_countries)

df = pd.read_csv(r'C:\Users\USER\Documents\WORK\ME\Pavan\P_Data_Extract_From_World_Development_Indicators.csv')
print("Original DataFrame:")
print(df)
