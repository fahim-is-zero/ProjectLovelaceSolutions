# Input: A distance in meters (m).
# Output: The time it takes for light to travel the input distance, in seconds (s).


c = 299792458  # Speed of light [m/s]

def light_time(distance):
    d = distance
    
    t = d/c

    return t

print(light_time(376291900)) # earth to moon