# code that computes the final amount M after starting with an amount m compounded yearly at a r rate for n years.

def compound_interest(amount, rate, years):
    m = amount  # starting amount
    r = rate
    n = years

    M = m * (1 + r)** n  # Formula of compound interest

    return M

print(compound_interest(1000, 0.07 ,25))
