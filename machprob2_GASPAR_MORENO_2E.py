from math import sqrt
import numpy as np
x1=int(input("X1: "))
y1=int(input("y1: "))
x2=int(input("X2: "))
y2=int(input("Y2: "))
x3=int(input("X3: "))
y3=int(input("Y3: "))
#midpoint
mpx12 = (x1+x2)/2
mpx13 = (x1+x3)/2
mpy12 = (y1+y2)/2
mpy13 = (y1+y3)/2
#slope
my12 = (y2-y1)/(x2-x1)
my31 = (y3-y1)/(x3-x1)
#perpendicular slope
p12 = (-1)*((x2-x1)/(y2-y1))
p13 = (-1)*((x3-x1)/(y3-y1))
#perpendicular line. We used array to solve the system of equation
A = np.array([[(-1*p12),1],[(-1*p13),1]])
B = np.array([[(mpy12-p12*mpx12)],[(mpy13-p13*mpx13)]])
z = np.linalg.solve(A,B)
#center
h = int(z[0])
k = int(z[1])
#radius
r = sqrt(pow(h-x1,2)+pow(k-y1,2))
#vector Dx+Ey+F=-x^2-y^2
def0=np.array([[x1,y1,1],[x2,y2,1],[x3,y3,1]])
a=(-(pow(x1,2)))-(pow(y1,2))
b = (-(pow(x2,2)))-(pow(y2,2))
c = (-(pow(x3,2)))-(pow(y3,2))
def1=np.array([[a],[b],[c]])
#VECTOR ANSWER
def2=np.linalg.solve(def0,def1)
print ('Center: (' + str(h) +','+ str(k) +')')
print ('Radius:'+str(r))
print ('vector: '+str(def2))
