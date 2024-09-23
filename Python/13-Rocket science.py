# Input: The velocity 'v' the rocket needs to reach to escape the planet in meters per second (m/s).
# Output: The mass of fuel 'm_fuel' needed by the rocket to escape the planet in kilograms (kg).

from math import e   # e = euler's number (2.7182818284...)

v_e = 2550  # rocket exhaust velocity [m/s]
M = 250000  # Saturn V rocket dry mass [kg]

def rocket_fuel(v):  # v is planet escape velocity

    m_fuel = M * (e**( v/v_e ) - 1)  # Rearranged Tsiolkovsky rocket equation 

    return m_fuel

v_e_dict = {"Sun" : 617500,
            "Earth" : 11186,
            "Mars" : 5030,
            "Moon" : 2380,
            "Jupiter" : 60200,
            "Saturn" : 36090
}

print("Jupiter", rocket_fuel(v_e_dict["Jupiter"]))
print("Earth : ", rocket_fuel(11186))  # Earth  -->  almost 20M kg
