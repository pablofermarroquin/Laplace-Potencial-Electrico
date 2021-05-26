import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import numpy as np
from scipy.integrate import quad
from scipy.odr import ODR, Model, Data
from mpl_toolkits.mplot3d import Axes3D
from sklearn.metrics import mean_squared_error
import random

terminos=50#200
a=1.0

def VoY(y,n): #funcion a la que se iguala la serie de Fourier
    return (y)*np.sin(n*np.pi*y/a)

def Cn(y,n):
    Integral = quad(VoY, 0, a,args=(n))
    C=2*Integral[0]/a
    return C

# Make data.
X = np.linspace(0, a, 100)
Y = np.linspace(0, a, 100)
X, Y = np.meshgrid(X, Y)

Z = np.sqrt(X**2 + Y**2)
Z=Z-Z
for n in range(0,terminos,1):
    Z+=Cn(Y,n)*np.exp(-n*np.pi*X/a)*np.sin(n*np.pi*Y/a)
    #Z = np.sin(R)

fig = plt.figure()
ax = plt.axes(projection='3d')

ax.plot_surface(X, Y, Z,cmap='viridis', edgecolor='none')
#ax.set_title('Surface plot')
#plt.show()

X2 = np.linspace(0.2, a/2, 100)
Y2 = np.linspace(0.5, a, 100)
X2, Y2 = np.meshgrid(X2, Y2)
#Z2=0.5*Y-0.1*X
Z2=0.1*Y2-0.5*X2+0.1
ax.plot_surface(X2, Y2, Z2,cmap='viridis', edgecolor='none')

#ax.set_title('Surface plot')
ax.set_xlabel("X (m)")
ax.set_ylabel("Y (m)")
ax.set_zlabel("V(x,y) (V)")
plt.show()

mse = mean_squared_error(Z, Z2)
print(mse)
#===========================
#Cálculo de los términos de la serie de Fourier utilizando
#únicamente ciclos anidados
#Requiere una gran capacidad de memoria y tiempo de ejecución
"""
valor=0
dx=a/exactitud
dy=a/exactitud

for n in range (1,terminos+1,1):
    x=0
    i=0
    while(x < a):
        y=0
        j=0
        while(y < a):
            valor=np.exp(-n*np.pi*x/a)*Cn(y,n)*np.sin(n*y*np.pi/a)
            Vn[i][j]+=valor
            y+=dy
            j+=1
        x+=dx
        i+=1
    #VTot+=np.array(Vn)
    
print(VTot)
"""