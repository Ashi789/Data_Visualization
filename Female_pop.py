import pandas as pd
import matplotlib.pyplot as plt

# Assuming the provided data is stored in a DataFrame or Series called 'df'

# Assuming the data is structured as follows:
# Index: Country names (e.g., 'World')
# Columns: Years (e.g., '1990 [YR1990]', '2000 [YR2000]', ...)
# Values: Population data

# We can set the variables accordingly:

# Fetching data (replace df with your actual DataFrame or Series)
df = pd.DataFrame({
    'Country': ['World'],
    '1990 [YR1990]': [2636306548],
    '2000 [YR2000]': [3055481352],
    '2014 [YR2014]': [3634994094],
    '2015 [YR2015]': [3677913970],
    '2016 [YR2016]': [3720947920],
    '2017 [YR2017]': [3763961798],
    '2018 [YR2018]': [3806031587],
    '2019 [YR2019]': [3847031725],
    '2020 [YR2020]': [3887047309],
    '2021 [YR2021]': [3922248931],
    '2022 [YR2022]': [3954425852]
})

# Extracting country name and population data
country = df.iloc[0]['Country']
years = df.columns[1:]  # Exclude the first column which contains country names
population_data = df.iloc[0][1:]  # Exclude the first column which contains country names

# Plotting the data
plt.figure(figsize=(10, 6))
plt.bar(years, population_data, color='Blue')
plt.xlabel('Year')
plt.ylabel('Population')
plt.title(f'Female Population All Over The World')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
