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

# Average temperature per month
df["month"] = df["date_time"].dt.month
avg_temp_per_month = df.groupby("month")["temp_c"].mean()
print("Average Temperature per Month")
print(avg_temp_per_month)
print("-" * 30)