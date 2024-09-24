def habitable_exoplanet(L, r):

    r_i = (L/1.1)**2
    r_o = (L/0.54)**2

    if r_i < r < r_o:
        return "just right"
    elif r_o < r:
        return "too cold"
    elif r_i > r:
        return "too hot"
    
