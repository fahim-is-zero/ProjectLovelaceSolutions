
def almost_pi(N):
    t = 0  # temp variable
    n = 1

    for i in range(1, (2 * N - 1) + 1, 2):  # generates 'N' - numbers odd numbers 
        p = 1/(i)
        if n % 2 == 0:
            t -= p
            n =+ 1
        else:
            t += p
            n += 1
    
    pi = 4 * t      # (See Leibniz formula)

    return pi

print(almost_pi(10000000))  # 10M times --> 6 accurate digits after decimal (3.141592)
