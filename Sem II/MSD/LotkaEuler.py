import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

def lotka_volterry(xy,t, a, b, c, d):
    x, y = xy
    dxdt = a*x - b*x*y
    dydt = c*x*y - d*y
    return [dxdt, dydt]

def Euler():

    xy = np.zeros((num_steps, 2))
    xy[0] = x0y0
    for i in range(1, num_steps):
        xy[i] = xy[i - 1] + np.array(lotka_volterry(xy[i - 1],t[i - 1], a, b, c, d)) * dt
    
    return xy

def wykresy(t,xy,xy_ode,x0,y0,a,b,c,d):
    x,y = xy.T
    aode,bode = xy_ode.T
    błąd = xy_ode - xy
    błąd = (sum(abs(błąd)))/num_steps
    
    fig= plt.figure(figsize=(14, 7))
    plt.figtext(0.5,0.05,f"dt = {dt},\n Błąd aproksymacji dla x : {błąd[0]}, y : {błąd[1]},\nDane parametry: a = {a}, b = {b}, c = {c}, d = {d}. Wartości początkowe x = {x0}, y = {y0}",ha="center", fontsize=12)
    
    def wyk(i,a,b,Typ):
    
        ax = plt.subplot(2, 1, i)
        ax.plot(t, a, label='Ofiary')
        ax.plot(t, b, label='Drapieżniki')
        ax.set_title(f'Model Lotki-volterry - {Typ}')
        ax.set_xlabel('Czas')
        ax.set_ylabel('Populacja')
        plt.legend()
        ax.grid(True)
        
        plt.tight_layout()
        
    wyk(1,x,y,"Metoda Eulera")
    wyk(2,aode,bode,"Metoda odeint")
    
    
    
    plt.tight_layout()
    plt.subplots_adjust(bottom=0.22,top=0.9)
    plt.show()

def dane():
    a = 1.2  
    b = 0.6  
    c = 0.3  
    d = 0.8  

    x0 = 2  
    y0 = 1   
    x0y0 = [x0, y0]
    x0y0 = np.array(x0y0)  


    t_start = 0
    t_end = 30
    dt = 0.001  
    num_steps = int((t_end - t_start) / dt)  
    t = np.linspace(t_start, t_end, num_steps)

    return a,b,c,d,x0,y0,x0y0,t_start,t_end,dt,num_steps,t

a,b,c,d,x0,y0,x0y0,t_start,t_end,dt,num_steps,t = dane()
    
xy_ode = odeint(lotka_volterry,x0y0,t, args=(a, b, c, d))
xy = Euler()

wykresy(t,xy,xy_ode,x0,y0,a,b,c,d)