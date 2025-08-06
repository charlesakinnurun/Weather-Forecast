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