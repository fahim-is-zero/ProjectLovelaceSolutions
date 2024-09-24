# Circumstellar Habitable Zone (CHZ)

# Input: The star's absolute luminosity L and the planet's distance from the star r.
# Output: The string "too cold" if the planet is too far away, "too hot" if it is too close, or "just right" if it is within the CHZ. 

from math import sqrt

def habitable_exoplanet(L, r):   # L = Star's absolute luminosity, r =  The planet's distance from the star

    r_i = sqrt(L/1.1)   # inner radius of CHZ Star (Unit : astroastronomical units(au))
    r_o = sqrt(L/0.54)   # outer radius of CHZ Star (Unit : astroastronomical units(au))

    if r_i < r < r_o:
        return "just right"
    elif r_o < r:
        return "too cold"
    elif r_i > r:
        return "too hot"
    
print(habitable_exoplanet(0.0015, 0.05))  # Proxima Centauri b
