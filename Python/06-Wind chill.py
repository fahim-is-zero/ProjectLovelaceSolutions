# Wind chill [T(wc)] formula : T_wc = 13.12 + 0.6215*T_a - 11.37*v^0.16 + 0.3965*T_a*v^0.16
# Where T_a is the temperature of air in C and v is the wind speed in m


# Input: The air temperature T_a in Celcius (°C) and the wind speed v in kilometers per hour.
# Output: The wind chill factor T_wc



def wind_chill(T_a, v):

    T_wc = 13.12 + 0.6215 * T_a - 11.37 * v**0.16 + 0.3965 * T_a * v**0.16   # Formula

    return T_wc

print(wind_chill(-25, 30))
