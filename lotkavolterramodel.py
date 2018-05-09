from numpy import *
import pylab as pl
from scipy import integrate
import vals

#XY is the form [X,Y]
#dX_dt returns [ax-pxy, -by+qxy]
def dX_dt(XY, t=0):
    return array([ vals.a*XY[0] - vals.p*XY[0]*XY[1] , -vals.b*XY[1] + vals.q*XY[0]*XY[1] ])
#jacobian
def Jac(XY, t=0):
    return array([ [vals.a - vals.p * XY[1], -vals.p*XY[0] ], [ vals.q*XY[1] , -vals.b +vals.q*XY[0] ] ])

def lv_plot(a,p,b,q,X,Y,t0,tf,tdi):
    #update user values
    vals.a = a
    vals.p = p
    vals.b = b
    vals.q = q

    #critical points
    cp1 = array([0. , 0.])
    cp2 = array([b/q, a/p])

    #evaluate critical points
    cp1_sol = Jac(cp1)
    cp2_sol = Jac(cp2)

    #find eigenvals  ( +/- i*sqrt(ab) )
    lambda1, lambda2 = linalg.eigvals(cp2_sol)

    #period (later returned)
    pd = 2*pi/abs(lambda1)

    #time series
    t = linspace(t0, tf, tdi)

    #initial conditions
    X0 = array([X, Y])

    #integration
    X = integrate.odeint(dX_dt, X0, t)

    #tuples transposed for x and y populations
    pop_x, pop_y = X.T

    #plotting
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

    #phase plane plotting

    #line thickness and colors
    v = linspace(0.25, 1, 5)
    vc = pl.cm.binary(linspace(0.25, 1, len(v)))

    f2 = pl.figure()

    #plot x vs y, no time axis
    for v, col in zip(v, vc):
        X0 = v * cp2
        X = integrate.odeint(dX_dt, X0, t)
        pl.plot(X[:,0], X[:,1], lw=3*v, color=col, label='X0=(%.f, %.f)' % ( X0[0], X0[1]) )

    #find max values
    ymax = pl.ylim(ymin=0)[1]
    xmax = pl.xlim(xmin=0)[1]

    #mesh grid density
    nb_points = 20

    #define grid
    x = linspace(0, xmax, nb_points)
    y = linspace(0, ymax, nb_points)
    X1 , Y1  = meshgrid(x, y)

    #compute derivatives
    DX1, DY1 = dX_dt([X1, Y1])

    #insure there is no division by 0
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

    #return the period for display on model page
    return pd
