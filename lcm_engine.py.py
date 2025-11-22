
def lcm(a, b):
    a_factors = []
    b_factors = []
    common_factors = []
    for i in range(1, a+b):
        a_factors.append(a*i)
    for n in range(1, b+a):
        b_factors.append(b*n)
    for j in b_factors:
        if j in a_factors:
            common_factors.append(j)
    common_factors = sorted(common_factors)
    return common_factors[0]

# print(lcm(13, 17))