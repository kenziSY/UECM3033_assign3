import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def ode(y, t, a, b):
    y0, y1 = y
    dydt = [a*(y0-y0*y1), b*(-y1+y0*y1)]
    return dydt

#initial conditions    
a = 1.0
b = 0.2
y_init = [0.1, 1.0] 
t = np.linspace(0, 5, 101)

sol = odeint(ode, y_init, t, args=(a, b))

#plot the Graphs of y0 and y1 against t
plt.plot(t, sol[:, 0], 'r', label='y0(t)')
plt.plot(t, sol[:, 1], 'b', label='y1(t)')
plt.title('Graphs of y0 and y1 against t with y0(0)= 0.1')
plt.legend(loc='best')
plt.xlabel('t')
plt.ylabel('y')
plt.grid()
plt.show()

#plot the graph of y1 against y0
plt.plot(sol[:, 0], sol[:,1], 'c')
plt.title('Graph of y1 against y0 with y0(0)= 0.1')
plt.xlabel('y0')
plt.ylabel('y1')
plt.grid()
plt.show()

############### Part 2 #################

y_init = [0.11, 1.0]   # when y0(0) = 0.11
sol2 = odeint(ode, y_init, t, args=(a, b))

#plot the graphs of y0 and y1 against t
plt.plot(t, sol2[:, 0], 'g', label='y0(t)')
plt.plot(t, sol2[:, 1], 'b', label='y1(t)')
plt.title('Graphs of y0 and y1 against t with y0(0)= 0.11')
plt.legend(loc='best')
plt.xlabel('t')
plt.ylabel('y')
plt.grid()
plt.show()

# plot the graph of y1 against y0
plt.plot(sol2[:, 0], sol2[:,1], 'c')
plt.title('Graph of y1 against y0 with y0(0)= 0.11')
plt.xlabel('y0')
plt.ylabel('y1')
plt.grid()
plt.show()