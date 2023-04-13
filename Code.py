import pandas as pd
df = pd.read_csv('geo.csv')

import plotly.express as px
fig = px.density_mapbox(df, lat='Latitude', lon='Longitude', z='Magnitude', radius=10,
                        center=dict(lat=-25, lon=136), zoom=4,
                        mapbox_style="stamen-terrain")
fig.show()

# export all possible latitude and longitude combinations
import csv
# Define the output CSV file name and location
output_csv = "latlong.csv"
# Define the latitude and longitude ranges
min_lat = -90
max_lat = 90
min_lon = -180
max_lon = 180
# Create a new CSV file and write the latitude and longitude headers
with open(output_csv, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['latitude', 'longitude'])
    # Iterate over all possible latitude and longitude values and write them to the CSV file
    for lat in range(min_lat, max_lat+1):
        for lon in range(min_lon, max_lon+1):
            writer.writerow([lat, lon])


