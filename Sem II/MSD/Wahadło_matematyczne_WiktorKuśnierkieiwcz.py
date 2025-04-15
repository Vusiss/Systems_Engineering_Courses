import sympy as sp
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Rozwiązanie dokładne
g, l, t, theta0, theta_poch0 = sp.symbols('g l t theta0 theta_poch0')
theta = sp.Function('theta')(t)
ode = sp.Eq(theta.diff(t, 2) + (g / l) * theta, 0)

ics = {theta.subs(t, 0): theta0, theta.diff(t).subs(t, 0): theta_poch0}
sol_with_ics = sp.dsolve(ode, theta, ics=ics)
theta_sol = sol_with_ics.rhs

theta_analytic = sp.lambdify(t, theta_sol.subs({theta0: 0.3, theta_poch0: 0, g: 9.81, l: 1}), 'numpy')
print(theta_analytic)
# Rozwiązanie numeryczne
theta0 = 0.3  
theta_poch0 = 0 
g = 9.81  
l = 1  


T = 10  
dt = 1  
y0 = [theta0, theta_poch0]

def wahadlo_equation(t, y):
    theta, theta_poch = y
    dydt = [theta_poch,  - (g/l)*theta]
    return dydt

t_span = (0, T)
t_eval = np.arange(0, T, dt)
sol = solve_ivp(wahadlo_equation, t_span, y0, t_eval=t_eval)

# Wyniki
theta_num = sol.y[0]
time = sol.t

theta_sympy = theta_analytic(time)






abs_error = np.mean(np.abs(theta_sympy - theta_num))
square_error = np.mean((theta_sympy - theta_num)**2)
print(abs_error,square_error)

plt.figure(figsize=(10, 6))
plt.plot(time, theta_num, label='Rozwiązanie Numeryczne', linestyle = "-")
plt.plot(time, theta_sympy, label='Rozwiązanie Analityczne',linestyle = "--")
plt.xlabel('t [s]')
plt.ylabel('Theta [rad]')
plt.legend()
plt.grid(True)
plt.subplots_adjust(bottom=0.22,top=0.9)
plt.figtext(0.5,0.05,f"Średni błąd bezwzgledny = {abs_error}, Średni błąd kwadratowy = {square_error}",ha="center", fontsize=12)
plt.show()

abs_error2 = np.abs(theta_sympy - theta_num)
square_error2 = (theta_sympy - theta_num)**2
plt.figure(figsize=(10, 6))
ax = plt.subplot(1,2,1)

ax.plot(time, abs_error2, label='Błąd bezwzględny', linestyle = "-")
plt.xlabel('t')
plt.ylabel('Odchylenie od wyniku dokładnego')
plt.legend()
plt.grid(True)
ax1 = plt.subplot(1,2,2)
ax1.plot(time, square_error2, label='Błąd kwadratowy',linestyle = "--")
plt.xlabel('t')
plt.ylabel('Odchylenie od wyniku dokładnego')
plt.legend()
plt.grid(True)
plt.subplots_adjust(bottom=0.22,top=0.9)
plt.figtext(0.5,0.05,f"Średni błąd bezwzgledny = {abs_error}, Średni błąd kwadratowy = {square_error}",ha="center", fontsize=12)
plt.show()