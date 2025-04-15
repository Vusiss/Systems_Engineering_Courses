import sympy as sp
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Rozwiązanie dokładne
k, t, T0, Tenv = sp.symbols('k t T0 Tenv')
T = sp.Function('T')(t)
ode = sp.Eq(T.diff(t) + k * (T - Tenv), 0)

ics = {T.subs(t, 0): T0}
sol_with_ics = sp.dsolve(ode, T, ics=ics)
theta_sol = sol_with_ics.rhs

theta_analytic = sp.lambdify(t, theta_sol.subs({T0: 100, Tenv: 20, k: 0.1}), 'numpy')

# Rozwiązanie numeryczne
T0 = 100  
Tenv = 20
k = 0.1 


Time= 50  
dt = 0.01  
y0 = [T0]

def Proces_chlodzenia(t, T):
    dTdt = - k*(T - Tenv)
    return [dTdt]

t_span = (0, Time)
t_eval = np.arange(0, Time, dt)
sol = solve_ivp(Proces_chlodzenia, t_span, y0, t_eval=t_eval)

# Wyniki
T_num = sol.y[0]
time = sol.t

T_sympy = theta_analytic(time)






mae = np.mean(np.abs(T_sympy - T_num))
mse = np.mean((T_sympy - T_num)**2)
print(mae,mse)

plt.figure(figsize=(10, 6))
plt.plot(time, T_num, label='Rozwiązanie Numeryczne', linestyle = "-")
plt.plot(time, T_sympy, label='Rozwiązanie Analityczne',linestyle = "--")
plt.xlabel('t [s]')
plt.ylabel('T [°C]')
plt.legend()
plt.grid(True)
plt.subplots_adjust(bottom=0.22,top=0.9)
plt.figtext(0.5,0.05,f"Średni błąd bezwzgledny = {mae}, Średni błąd kwadratowy = {mse}",ha="center", fontsize=12)
plt.show()

mae2 = np.abs(T_sympy - T_num)
mse2 = (T_sympy - T_num)**2
plt.figure(figsize=(10, 6))
ax = plt.subplot(1,2,1)

ax.plot(time, mae2, label='Błąd bezwzględny', linestyle = "-")
plt.xlabel('t')
plt.ylabel('Odchylenie od wyniku dokładnego')
plt.legend()
plt.grid(True)
ax1 = plt.subplot(1,2,2)
ax1.plot(time, mse2, label='Błąd kwadratowy',linestyle = "--")
plt.xlabel('t')
plt.ylabel('Odchylenie od wyniku dokładnego')
plt.legend()
plt.grid(True)
plt.subplots_adjust(bottom=0.22,top=0.9)
plt.figtext(0.5,0.05,f"Średni błąd bezwzgledny = {mae}, Średni błąd kwadratowy = {mse}",ha="center", fontsize=12)
plt.show()