# Introduction
![Weather Forecast](assets/weather.jpg)
***
The dataset named "Weather Dataset.csv". It is a CSV (Comma Separated Values) file containing hourly weather data.
The dataset includes the following columns:
1. Date/Time: The date and time of the observation.
2. Temp_C: The temperature in degrees Celsius.
3. Dew Point Temp_C: The dew point temperature in degrees Celsius.
4. Rel Hum_%: The relative humidity as a percentage.
5. Wind Speed_km/h: The wind speed in kilometers per hour.
6. Visibility_km: The visibility in kilometers.
7. Press_kPa: The atmospheric pressure in kilopascals.
8. Weather: A text description of the weather conditions.

The file is a standard dataset for practicing data cleaning, analysis, and manipulation using tools like pandas in Python. The dataset contains a total of 8784 entries and does not have any missing values.
## Cleaning
1. To clean your data, you can follow these steps:
2. Load the data: The first step is to load the Weather Dataset.csv file into a pandas DataFrame. This allows you to perform various operations on the data.
3. Standardize column names: Column names like Date/Time and Rel Hum_% can be difficult to work with due to special characters and spaces. It's best practice to rename them to a consistent format, such as snake_case, for easier access and manipulation.
4. Convert data types: The date_time column was initially of the object data type. For any time-based analysis, this column needs to be converted to a datetime format.
5. Handle duplicate rows: It's important to check for and remove any duplicate rows that might skew your analysis.
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
## Analysis
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
10. What is the highest temperature (temp_c) recorded in each year

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
The remaining analysis can be found
[here](/script/)
## Tools I Used
* Python (pandas)
* Git
* Vscode
