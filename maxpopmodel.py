def model(y,t):
    k = 1
    dydt = k * (1-(y/1000)) * y
    return dydt
