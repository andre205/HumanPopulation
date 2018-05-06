from numpy import *
import pylab as p
from scipy import integrate

# Definition of parameters
a = 1.
b = 0.1
c = 1.5
d = 0.75
def dX_dt(X, t=0):
    """ Return the growth rate of fox and rabbit populations. """
    return array([ a*X[0] -   b*X[0]*X[1] , -c*X[1] + d*b*X[0]*X[1] ])

X_f0 = array([0. , 0.])
X_f1 = array([c/(d*b), a/b])

all(dX_dt(X_f0) == zeros(2) ) and all(dX_dt(X_f1) == zeros(2))

#X JACOBIAN
def d2X_dt2(X, t=0):
    return array([ [a-b*X[1], -b*X[0] ], [ b*d*X[1] , -c +b*d*X[0] ] ])

A_f0 = d2X_dt2(X_f0)
A_f1 = d2X_dt2(X_f1)

#EIGENVALS  +/- sqrt(c*a).j
lambda1, lambda2 = linalg.eigvals(A_f1)

#PERIOD
T_f1 = 2*pi/abs(lambda1)

#TIME
t = linspace(0, 15,  1000)
#INITIAL CONDITIONS
X0 = array([10, 5])
X, infodict = integrate.odeint(dX_dt, X0, t, full_output=True)


rabbits, foxes = X.T
f1 = p.figure()
p.plot(t, rabbits, 'r-', label='Rabbits')
p.plot(t, foxes  , 'b-', label='Foxes')
p.grid()
p.legend(loc='best')
p.xlabel('time')
p.ylabel('population')
p.title('Evolution of fox and rabbit populations')
f1.savefig('rabbits_and_foxes_1.png')
