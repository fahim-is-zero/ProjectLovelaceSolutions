from math import e 

v_e = 2550  # rocket exhaust velocity [m/s]
M = 250000  # Saturn V rocket dry mass [kg]

def rocket_fuel(v):  # v is planet escape velocity

    m_fuel = M * (e**( v/v_e ) - 1)  

    return m_fuel

print("Earth : ", rocket_fuel(11186))  
