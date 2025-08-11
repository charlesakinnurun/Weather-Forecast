## Introduction
The dataset named "Weather Dataset.csv". It is a CSV (Comma Separated Values) file containing hourly weather data.
The dataset includes the following columns:*Date/Time: The date and time of the observation.
* Temp_C: The temperature in degrees Celsius.
* Dew Point Temp_C: The dew point temperature in degrees Celsius.
* Rel Hum_%: The relative humidity as a percentage.
* Wind Speed_km/h: The wind speed in kilometers per hour.
* Visibility_km: The visibility in kilometers.
* Press_kPa: The atmospheric pressure in kilopascals.
* Weather: A text description of the weather conditions.
### Data Cleaning
```python
import pandas as pd

# 1. Load the dataset
df = pd.read_csv("datasets/Weather Dataset.csv")

# 2. Standardize the column names
column_mapping = {
    "Date/Time": "date_time",
    "Temp_C": "temp_c",
    "Dew Point Temp_C": "dew_point_temp_c",
    "Rel Hum_%": "rel_hum",
    "Wind Speed_Km/h": "wind_speed_kmh",
    "Visibility_km": "visibilty_km",
    "Press_kPa": "press_kpa",
    "Weather": "weather"
}
df = df.rename(columns=column_mapping)

# 3. Convert the "date_time" column to datetime objects
df["date_time"] = pd.to_datetime(df["date_time"])

# 4. Check and handle duplicates rows
duplicates_before = df.duplicated().sum()
if duplicates_before > 0:
    df.drop_duplicates(inplace=True)
duplicates_after = df.duplicated().sum()

print(f"Number of duplicates before removal:{duplicates_before}")
print("Number of duplicates after removal: {duplicates_after}")

# Display the cleaned data info to show the changes
print("Cleaned Data Info")
print(df.info())

# Display the first few rows of the cleaned data
print("First 5 rows of the cleaned  data")
print(df.head())

# Save the cleaned data
df.to_csv('datasets/Weather Dataset Cleaned.csv', index=False)
```
### Analysis
Here are 10 analytical questions you can solve using pandas with the provided weather dataset:
1. What is the average temperature (temp_c) for each month?
2. What is the maximum wind speed (wind_speed_kmh) recorded in the dataset?
3. How many times was the weather condition exactly 'Clear'?
4. How many unique weather conditions are there in the dataset?
5. What is the mean visibility (visibility_km) when the weather condition is 'Fog'?
6. Find all instances where the wind speed (wind_speed_kmh) was greater than 20 km/h and visibility (visibility_km) was less than 10 km.
7. For each unique weather condition, what are the minimum, maximum, and average values of the pressure (press_kpa)?
8. Show all records where the weather condition is 'Snow'.
9. What is the average relative humidity (rel_hum) for each hour of the day?
10. What is the highest temperature (temp_c) recorded in each year?
#### What is the average temperature (temp_c) for each month?
```python
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
```
#### What is the maximum wind speed (wind_speed_kmh) recorded in the dataset?
```python
import pandas as pd

# Load the dataset
df = pd.read_csv("datasets/Weather Dataset.csv")

# Clean the data as per previous steps
column_mapping = {
    "Date/Time": "date_time",
    "Temp_C": "temp_c",
    "Dew Point Temp_C": "dew_point_temp_c",
    "Rel Hum_%": "rel_hum",
    "Wind Speed_km/h": "wind_speed_km",
    "Visibilty_km": "visibility_km",
    "Press_kPa": "press_kpa",
    "Weather": "weather"
}
df = df.rename(columns=column_mapping)
df["date_time"] = pd.to_datetime(df["date_time"])

# Maximum wind speed
max_wind_speed = df["wind_speed_kmh"].max()
print("Maximum Wind Speed (Km/h)")
print(max_wind_speed)
print("-" * 30)
```
#### How many times was the weather condition exactly 'Clear'?
```python
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

# Count of "Clear" weather
clear_weather_count = df[df["weather"] == "Clear"].shape[0]
print("Count of 'Clear' Weather")
print(clear_weather_count)
print("-" * 30)
```
#### How many unique weather conditions are there in the dataset?
```python
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

# Number of unique weather conditions
unique_weather_count = df["weather"].nunique()
print("Number of Unique Weather Conditions")
print(unique_weather_count)
print("-" * 30)
```
#### What is the mean visibility (visibility_km) when the weather condition is 'Fog'?
```python
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

# Mean visbility when weather is "Fog"
mean_visiblity_fog = df[df["weather"] == "Fog"]["visibility_km"].mean()
print("Mean Visibility when Weather is Fog")
print(mean_visiblity_fog)
print("-" * 30)
```
#### Find all instances where the wind speed (wind_speed_kmh) was greater than 20 km/h and visibility (visibility_km) was less than 10 km.
```python
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
```
#### For each unique weather condition, what are the minimum, maximum, and average values of the pressure (press_kpa)?
```python
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

# Min, max, and average pressure per weather condition
pressure_per_weather = df.groupby("weather")["press_kpa"].agg(["min","max","mean"])
print("Min,Max and Average Pressure per Weather Condition")
print(pressure_per_weather)
print("-" * 30)
```
#### Show all records where the weather condition is 'Snow'.
```python
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

# Records where weather is "Snow"
snow_records = df[df["weather"].str.contains('Snow',case=False,na=False)]
print("Count of records with 'Snow' in Weather Condition")
print(snow_records.shape[0])
print("First 5 records")
print(snow_records.head())
print("-" * 30)
```
#### What is the average relative humidity (rel_hum) for each hour of the day?
```python
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

# Average relative humidity per hour
df["hour"] = df["date_time"].dt.hour
avg_hum_per_hour = df.groupby("hour")["rel_hum"].mean()
print("Average Relative Humidity per Hour")
print(avg_hum_per_hour)
print("-" * 30)
```
#### What is the highest temperature (temp_c) recorded in each year?
```python
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

# Highest Temperature per year
df["year"] = df["date_time"].dt.year
max_temp_per_year = df.groupby("year")["temp_c"].max()
print("Highest Temperature per Year")
print(max_temp_per_year)
```
