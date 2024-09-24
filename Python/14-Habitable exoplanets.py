# Circumstellar Habitable Zone (CHZ)

def habitable_exoplanet(L, r):  

    r_i = (L/1.1)**2   # inner radius of CHZ Star
    r_o = (L/0.54)**2   # outer radius of CHZ Star

    if r_i < r < r_o:
        return "just right"
    elif r_o < r:
        return "too cold"
    elif r_i > r:
        return "too hot"
    
print(habitable_exoplanet(0.0015, 0.05))  # Proxima Centauri b
