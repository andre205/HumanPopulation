import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def model(y,t):
    k = 1.09
    dydt = k * (1-(y/10)) * y
    return dydt

y0 = 7.632819325
t = np.linspace(2018,2040)
y = odeint(model,y0,t)

plt.plot(t,y)
plt.xlabel('time')
plt.ylabel('human population (billion)')

plt.savefig('test.png')
