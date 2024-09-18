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
