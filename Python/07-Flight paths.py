# Calculating distances on a sphere using haversine formula.

# Input: (Latitude, longitude) coordinates of two points. Latitudes go from -90 to +90. Longitudes go from -180 to +180. Convert angles from degrees to radians before using the sine and cosine functions!
# Output: The distance between the points in kilometers (km).

from math import radians, sqrt, asin, sin, cos  # asin = arcsin = sin^-1

R  = 6372.1  # Radius of the Earth [km]

def haversine_distance(lat1, lon1, lat2, lon2):
    d = 0
    
    if (-90 < lat1 and lat2 < +90) and (-180 < lon1 and lon2 < +180):
        lat1 = radians(lat1)  # degree to rad
        lat2 = radians(lat2)
        lon1 = radians(lon1)
        lon2 = radians(lon2)

        d = 2 * R * asin( sqrt( (sin( (lat2 - lat1)/2 ))**2 + cos(lat1) * cos(lat2) * (sin( (lon2 - lon1)/2 ))**2 ))

        return d
    else:
        return "out of range!"

print(haversine_distance(90, 145.73007535186804, -90, -18.96168923319783))  # Pole to pole
