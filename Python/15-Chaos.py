def logistic_map(r):
    x = [0.5]
    count = 0

    while count <= 49:
        val = r * x[-1] * (1 - x[-1])
        x.append(val)
        count += 1

    return x
