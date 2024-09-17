# code that returns the expected body mass of a moose living at the input latitude using the equation

def moose_body_mass(latitude):
    a = 2.757
    b = 16.793
    
    mass = a * latitude + b
    
    return mass

print(moose_body_mass(60.5))
