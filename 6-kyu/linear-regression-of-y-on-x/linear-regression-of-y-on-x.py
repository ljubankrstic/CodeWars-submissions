def regression_line(x, y):
    sum_of_x = sum(x)
    sum_of_y = sum(y)
    products_sum = sum([x[i] * y[i] for i in range(len(x))])
    sum_of_x_squared = sum([i * i for i in x])
    n = len(x)
    alpha = (sum_of_y * sum_of_x_squared - sum_of_x*products_sum)
    beta = (n*products_sum - sum_of_x*sum_of_y)
    divisor = (n*sum_of_x_squared - sum_of_x * sum_of_x)
    alpha/=divisor
    beta/=divisor
    return (round(alpha, 4),round(beta, 4))
​