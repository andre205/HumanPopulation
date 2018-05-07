import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

#2018 growth rate: 1.09% per year
#Proposed carrying capacity: 10 billion
def model(y,t):
    k = 1.09
    dydt = k * (1-(y/10)) * y
    return dydt

#2018 population: 7.6 billion
y0 = 7.632819325
t = np.linspace(2018,2040)
y = odeint(model,y0,t)

plt.plot(t,y)
plt.xlabel('time')
plt.ylabel('human population (billion)')
plt.savefig('human_population_model.png')
