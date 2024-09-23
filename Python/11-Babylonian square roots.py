def babylonian_sqrt(S):
    
    x_n = S / 2 

    if S == 0:
        return 0
    else:
        for i in range(0, 100):
            x_n = 1/2 * (x_n + S / x_n) 

    return x_n
