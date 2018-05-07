from numpy import *
import pylab as pl
from scipy import integrate

class vals:
    def __init__(self):
        a = 1.
        p = 0.1
        b = 1.5
        q = 0.75
    a = 1.
    p = 0.1
    b = 1.5
    q = 0.75

#X is the form [X,Y]
#dX_dt returns [ax-pxy, -by+qxy]
def dX_dt(X, t=0):
    return array([ vals.a*X[0] - vals.p*X[0]*X[1] , -vals.b*X[1] + vals.q*X[0]*X[1] ])

def d2X_dt2(X, t=0):
    return array([ [vals.a-vals.p*X[1], -vals.p*X[0] ], [ vals.p*vals.q*X[1] , -vals.b +vals.p*vals.q*X[0] ] ])

def lv_plot(a,p,b,q,X,Y,t0,tf,tdi):

    vals.a = a
    vals.p = p
    vals.b = b
    vals.q = q

    X_f0 = array([0. , 0.])
    X_f1 = array([b/(q*p), a/p])

    all(dX_dt(X_f0) == zeros(2) ) and all(dX_dt(X_f1) == zeros(2))

    A_f0 = d2X_dt2(X_f0)
    A_f1 = d2X_dt2(X_f1)

    #EIGENVALS  +/- sqrt(b*a).j
    lambda1, lambda2 = linalg.eigvals(A_f1)
    #PERIOD
    T_f1 = 2*pi/abs(lambda1)

    #TIME
    t = linspace(t0, tf, tdi)
    #INITIAL CONDITIONS
    X0 = array([X, Y])
    X = integrate.odeint(dX_dt, X0, t)

    pop_a, pop_b = X.T

    f1 = pl.figure()
    pl.plot(t, pop_a, 'r-', label='X')
    pl.plot(t, pop_b  , 'b-', label='Y')
    pl.grid()
    pl.legend(loc='best')
    pl.xlabel('time')
    pl.ylabel('population')
    titlestring = "Evolution of X and Y populations (a="+str(vals.a)+",p="+str(vals.p)+",b="+str(vals.b)+",q="+str(vals.q)+")"
    pl.title(titlestring)

    f1.savefig('img/lvimg.png')

# lv_plot(1.1,0.34,1.32,.55,20,15,0,10,1000)
