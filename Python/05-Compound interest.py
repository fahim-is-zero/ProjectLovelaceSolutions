def compound_interest(amount, rate, years):
    m = amount
    r = rate
    n = years

    M = m * (1 + r)** n

    return M
