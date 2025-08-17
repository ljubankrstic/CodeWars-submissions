def greatest_product(st):
    gr = 0
    for i in range(len(st)-4):
        prod = 1
        for i in st[i : i + 5]:
            prod *= int(i)
        if prod > gr:
            gr = prod
    return gr