import os
import requests
import pandas as pd

def fetch_weather_data(latitude, longitude, start_date, end_date):
    url = "https://archive-api.open-meteo.com/v1/archive"
    
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "start_date": start_date,
        "end_date": end_date,
        "hourly": ["temperature_2m", "relative_humidity_2m", "dew_point_2m", "precipitation", "wind_speed_10m", "wind_speed_100m", "soil_temperature_0_to_7cm", "soil_temperature_7_to_28cm"]
    }
    
    response = requests.get(url, params=params)
    data = response.json()
    
    # Assuming the data is in the 'hourly' key
    hourly_data = data.get('hourly', {})
    
    # Convert the dictionary to a DataFrame
    df = pd.DataFrame(hourly_data)
    
    return df

# Example usage
df = fetch_weather_data(52.52, 13.41, "2025-01-16", "2025-01-22")
print(df)