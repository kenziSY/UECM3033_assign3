
UECM3033 Assignment #3 Report
========================================================

- Prepared by:  *Wong Sin Yi*
- Tutorial Group: T2

--------------------------------------------------------

## Task 1 --  Gauss-Legendre formula

The reports, codes and supporting documents are to be uploaded to Github at: 

[https://github.com/kenziSY/UECM3033_assign3](https://github.com/kenziSY/UECM3033_assign3)


Explain how you implement your `task1.py` here.

For the implementation of self-define function "gausslegendre", the weights and nodes is first get from using the command of "numpy.polynomial.legendre.leggauss". After the nodes and weights are found for the n-point quadrature, the integral over [a,b] is approximated by using the equation 

$$\int_a^{b} f{(x)} dx = \frac{b-a}{2} \sum_{i=1}^n w_{i}f(\frac{b-a}{2}x_{i}+\frac{a+b}{2}).$$

Explain how you get the weights and nodes used in the Gauss-Legendre quadrature.

The weights and nodes are computed by using "numpy.polynomial.legendre.leggauss" command.
 
---------------------------------------------------------

## Task 2 -- Predator-prey model

Explain how you implement your `task2.py` here, especially how to use `odeint`.

To solve the ODE system with odeint, we must have first order ODE and parameters a and b which are already given, then a self-define function "ode" is created by using these two things. For initial conditions, the constants a and b and a initial vector of y is defined. Then, an array of times, t is generated from 0 to 5 and evenly partitioned into 101 parts.  The odeint is then called to generate the solution, the parameters a and  b are passed to "ode" using "args" argument. The solution is an 101*2 arrays, the first column of solution is y0 and second column of solution is y1. By using the "matplotlib.pyplot", the graphs of y0 and y1 against t and graph of y1 against y0 are plotted. 

Put your graphs here and explain.

When y0= 0.1, y1= 1.0

![](https://github.com/kenziSY/UECM3033_assign3/blob/master/Graphs%20of%20y1%20and%20y0%20%281%29.png)

![](https://github.com/kenziSY/UECM3033_assign3/blob/master/Graph%20of%20y0%20against%20y1%20%281%29.png)

When y0= 0.11, y1= 1.0

![](https://github.com/kenziSY/UECM3033_assign3/blob/master/Graphs%20of%20y1%20and%20y0%20%282%29.png)

![](https://github.com/kenziSY/UECM3033_assign3/blob/master/Graph%20of%20y0%20against%20y1%20%282%29.png)

y0 is the number of prey and y1 is the number of predators. From the graphs above, we can see that when the number of prey inreases, the number of predator decreases. Therefore, there is an inverse relationship between y0 and y1.

Is the system of ODE sensitive to initial condition? Explain.

No. The graphs show that there is only small changes when the initial value conditions change from 0.1 to 0.11. Thus, the system of ODE is not sensitive to initial condition.

-----------------------------------

<sup>last modified: 17.4.2016</sup>
