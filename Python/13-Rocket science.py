from math import e )

v_e = 2550  
M = 250000  

def rocket_fuel(v):

    m_fuel = M * (e**( v/v_e ) - 1)

    return m_fuel

