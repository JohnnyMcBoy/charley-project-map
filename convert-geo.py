import pandas as pd

from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="kthrnsnclr@gmail.com")


# Use pandas to read the first column ("City")
locations = pd.read_csv("charley.csv", sep=",", header=0, usecols=['Location'])

# Access the DataFrame of the csv, created by pandas
df = pd.DataFrame(locations)

# Get amount of cities
LocationTotal=len(df)

# These are the lists that we will fill and add to csv
lat_list = [' ']*LocationTotal
lon_list = [' ']*LocationTotal

# Loop through each row of the DataFrame
for index, row in df.iterrows():
    location = row['Location']
    location_string = str(location)

    # Use geolocator to grab more verbose location information
    location_geo = geolocator.geocode(location_string)

    # Check that the location value exists. If it does, add to a list. If it doesn't, add empty string
    if location_geo != None:
        # print(index)
        lat_list[index] = location_geo.latitude
        lon_list[index] = location_geo.longitude
    else:
        print(location_string)
        lat_list[index] = ('')
        lon_list[index] = ('')
        continue

# Check that the list is full and the loop actually ends!
print('loop done!')

# Add lists to CSV
df = pd.read_csv("charley.csv")
df["newLong"] = lon_list
df["newLat"] = lat_list
df.to_csv("charley.csv", index=False)

print('csv done!')