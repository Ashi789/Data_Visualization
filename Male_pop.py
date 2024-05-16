import pandas as pd
import matplotlib.pyplot as plt

# Assuming the provided data is stored in a DataFrame or Series called 'df'

# Assuming the data is structured as follows:
# Index: Population category (e.g., 'Male Pop')
# Columns: Years (e.g., '1990 [YR1990]', '2000 [YR2000]', ...)
# Values: Population data

# We can set the variables accordingly:

# Fetching data (replace df with your actual DataFrame or Series)
df = pd.DataFrame({
    'Population Category': ['Male Pop'],
    '1990 [YR1990]': [2657088912],
    '2000 [YR2000]': [3088840111],
    '2014 [YR2014]': [3682046200],
    '2015 [YR2015]': [3725936179],
    '2016 [YR2016]': [3769467536],
    '2017 [YR2017]': [3812480158],
    '2018 [YR2018]': [3854339551],
    '2019 [YR2019]': [3894742852],
    '2020 [YR2020]': [3933158305],
    '2021 [YR2021]': [3966056767],
    '2022 [YR2022]': [3996520937]
})

# Extracting population category and population data
population_category = df.iloc[0]['Population Category']
years = df.columns[1:]  # Exclude the first column which contains population categories
population_data = df.iloc[0][1:]  # Exclude the first column which contains population categories

# Plotting the data
plt.figure(figsize=(10, 6))
plt.bar(years, population_data, color='skyblue')
plt.xlabel('Year')
plt.ylabel('Population')
plt.title(f'Male Population All Over The World')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
