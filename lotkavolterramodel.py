from numpy import *
import pylab as pl
from scipy import integrate
import vals

#X is the form [X,Y]
#dX_dt returns [ax-pxy, -by+qxy]
def dX_dt(X, t=0):
    return array([ vals.a*X[0] - vals.p*X[0]*X[1] , -vals.b*X[1] + vals.q*X[0]*X[1] ])
#jacobian
def Jac(X, t=0):
    return array([ [vals.a - vals.p * X[1], -vals.p*X[0] ], [ vals.q*X[1] , -vals.b +vals.q*X[0] ] ])

def lv_plot(a,p,b,q,X,Y,t0,tf,tdi):

    vals.a = a
    vals.p = p
    vals.b = b
    vals.q = q

    X_f0 = array([0. , 0.])
    X_f1 = array([b/q, a/p])

    A_f0 = Jac(X_f0)
    A_f1 = Jac(X_f1)

    #EIGENVALS  +/- i*sqrt(b*a)
    lambda1, lambda2 = linalg.eigvals(A_f1)
    #PERIOD
    pd = 2*pi/abs(lambda1)

    #TIME
    t = linspace(t0, tf, tdi)
    #INITIAL CONDITIONS
    X0 = array([X, Y])
    X = integrate.odeint(dX_dt, X0, t)

    pop_x, pop_y = X.T

    f1 = pl.figure()
    pl.plot(t, pop_x, 'r-', label='X')
    pl.plot(t, pop_y, 'b-', label='Y')
    pl.grid()
    pl.legend(loc='best')
    pl.xlabel('time')
    pl.ylabel('population')
    titlestring = "Evolution of X and Y populations (a="+str(vals.a)+",p="+str(vals.p)+",b="+str(vals.b)+",q="+str(vals.q)+")"
    pl.title(titlestring)

    f1.savefig('img/lvimg.png')

    v = linspace(0.25, 1, 5)
    vc = pl.cm.binary(linspace(0.25, 1, len(v)))

    f2 = pl.figure()

    for v, col in zip(v, vc):
        X0 = v * X_f1
        X = integrate.odeint(dX_dt, X0, t)
        pl.plot(X[:,0], X[:,1], lw=3*v, color=col, label='X0=(%.f, %.f)' % ( X0[0], X0[1]) )

    #find max values
    ymax = pl.ylim(ymin=0)[1]
    xmax = pl.xlim(xmin=0)[1]
    #mesh grid density
    nb_points = 20
    x = linspace(0, xmax, nb_points)
    y = linspace(0, ymax, nb_points)

    X1 , Y1  = meshgrid(x, y)
    DX1, DY1 = dX_dt([X1, Y1])
    M = (hypot(DX1, DY1))
    M[M == 0] = 1.
    DX1 /= M
    DY1 /= M

    pl.title('Phase Plane')
    Q = pl.quiver(X1, Y1, DX1, DY1, M, pivot='mid', cmap=pl.cm.jet)
    pl.xlabel('X Population')
    pl.ylabel('Y Population')
    pl.legend()
    pl.grid()
    pl.xlim(0, xmax)
    pl.ylim(0, ymax)
    f2.savefig('img/ppimg.png')

    return pd
