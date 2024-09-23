# Input: A number S.
# Output: The square root of S approximated using the babylonian method. Answer should be accurate to 10 significant figures. That is, it should be correct to within 1 part in 10 billion, or the relative error should be lower than 10^-10. 




def babylonian_sqrt(S):
    
    x_n = S / 2  # initial guess

    if S == 0:
        return 0
    else:
        for i in range(0, 100):
            x_n = 1/2 * (x_n + S / x_n) # formula (Babylonian method)

    return x_n

print(babylonian_sqrt(150626.35019758446 ))
