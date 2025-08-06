import pandas as pd

# Load the dataset
df = pd.read_csv("datasets/Weather Dataset.csv")

# Clean the data as per the previous steps
column_mapping = {
    'Date/Time': 'date_time',
    'Temp_C': 'temp_c',
    'Dew Point Temp_C': 'dew_point_temp_c',
    'Rel Hum_%': 'rel_hum',
    'Wind Speed_km/h': 'wind_speed_kmh',
    'Visibility_km': 'visibility_km',
    'Press_kPa': 'press_kpa',
    'Weather': 'weather'
}
df = df.rename(columns=column_mapping)
df['date_time'] = pd.to_datetime(df['date_time'])

# Filter for high wind speed and low visibilty
high_wind_low_visibility = df[(df["wind_speed_kmh"] > 20) & (df["visibility_km"] < 10)]
print("Count of records with wind speed > 20 km/h and visibilty < 10 km")
print(high_wind_low_visibility.shape[0])
print("First 5 records")
print(high_wind_low_visibility.head())
print("-" * 30)