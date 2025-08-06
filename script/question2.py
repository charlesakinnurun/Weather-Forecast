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