from pylab import *


n = -10
m = 10
X, Y = mgrid[n:m,n:m]
U, V = 1.0/X, 1.0/Y

r = sqrt(U*U + V*V)
t = arctan2(V,U)
t = t+1.57

u = r*cos(t)
v = r*sin(t)




J, K = X-10, Y

r = sqrt(J*J + K*K)
t = arctan2(K,J)
t = t+1.57

j = r*cos(t)
k = r*sin(t)

#print r, t

quiver(X,Y, u, v, linewidth=.5, color='red')
#quiver(X,Y, j, k, linewidth=.5, color='blue')

#quiver(X,Y, u+j, v+k, linewidth=.5, color='blue')

show()