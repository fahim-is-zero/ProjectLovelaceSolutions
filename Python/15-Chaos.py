# Input: The parameter r.
# Output: A list containing the first 51 values of the logistic map (x_0, x_1, x_2,......x_49, x_50).


def logistic_map(r):
    x = [0.5]
    count = 0

    while count <= 49:
        val = r * x[-1] * (1 - x[-1])  # Formula : x_n+1 = r * x_n(1 - x_n)
        x.append(val)
        count += 1

    return x

print(logistic_map(1))  # death (r=1)
print(logistic_map(3.5))  # chaos (r=3.5)
