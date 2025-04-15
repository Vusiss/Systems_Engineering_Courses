import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

def lorenz(xyz,t,sigma,beta,rho):
    x,y,z = xyz
    dx_dt = sigma * (y - x)
    dy_dt = x * (rho - z) - y
    dz_dt = x * y - beta * z
    return dx_dt, dy_dt, dz_dt

def euler_method(xyz, t,dt, steps):
    for i in range(1, steps):
        xyz[i] = xyz[i-1]+ np.array(lorenz(xyz[i-1], t,sigma, beta, rho)) * dt
    return xyz

def wykresy(xyz,xyzode):
    x,y,z = xyz.T
    xode,yode,zode = xyzode.T
    błąd = xyz - xyz_ode
    błąd = (sum(abs(błąd)))/steps
    
    fig= plt.figure(figsize=(14, 7))
    plt.figtext(0.5,0.05,f"dt = {dt},\n Błąd aproksymacji dla x : {błąd[0]}, y : {błąd[1]}, z : {błąd[2]},\nDane parametry: sigma = {sigma}, beta = 8/3, rho = {rho}. Wartości początkowe x = {x0}, y = {y0}, z = {z0}",ha="center", fontsize=12)

    def wyk(i,x,y,lX,lY):
    
        ax = plt.subplot(2, 3, i)
        ax.plot(x, y)
        ax.set_title(f'Układ Lorenza - {lX}{lY}')
        ax.set_xlabel(lX)
        ax.set_ylabel(lY)
        ax.grid(True)
        
        plt.tight_layout()
    
    xs = [x,x,y,xode,xode,yode]
    ys = [y,z,z,yode,zode,zode]
    names = ["X","X","Y","X","X","Y","Y","Z","Z","Y","Z","Z"]
    
    for i in range(6):
        wyk(i+1,xs[i],ys[i],names[i], names[i+6])
    
    plt.tight_layout() 
    plt.subplots_adjust(bottom=0.22,top=0.9)
    plt.show()
    
    fig= plt.figure(figsize=(12, 6))
    plt.figtext(0.5,0.05,f"dt = {dt},\n Błąd aproksymacji dla x : {błąd[0]}, y : {błąd[1]}, z : {błąd[2]},\nDane parametry: sigma = {sigma}, beta = 8/3, rho = {rho}. Wartości początkowe x = {x0}, y = {y0}, z = {z0}",ha="center", fontsize=12)
    
    ax3d = fig.add_subplot(1,2,1,projection='3d')
    ax_ode3d = fig.add_subplot(1,2,2,projection='3d')
    
    ax3d.plot(x, y, z,lw=0.5)
    ax_ode3d.plot(xode, yode, zode,lw=0.5)
    
    ax3d.set_title(f'Układ Lorenza - Metoda Eulera')
    ax3d.set_xlabel("X")
    ax3d.set_ylabel("Y")
    ax3d.set_zlabel("Z")
    
    ax_ode3d.set_title(f'Układ Lorenza - Odeint')
    ax_ode3d.set_xlabel("X")
    ax_ode3d.set_ylabel("Y")
    ax_ode3d.set_zlabel("Z")
    
    plt.tight_layout() 
    plt.subplots_adjust(bottom=0.2,top=0.9)
    plt.show()

def dane():
    # Parametry
    sigma = 10
    beta = 8/3
    rho = 28

    # Warunki początkowe
    x0, y0, z0 = 1, 1, 1
        
    # Parametry symulacji
    t_start = 0
    t_end = 30
    dt = 0.01  
    steps = int((t_end - t_start) / dt)  
    t = np.linspace(t_start, t_end, steps)



    xyz = np.zeros((steps,3))


    xyz[0] = x0, y0, z0
    xyz_ode =  [x0, y0, z0]

    return sigma,beta,rho, dt, t,steps, xyz, xyz_ode, t_start, t_end, x0, y0, z0

sigma,beta,rho, dt, t,steps, xyz, xyz_ode, t_start, t_end, x0, y0, z0 = dane()

# Wywołanie metody Eulera
xyz = euler_method(xyz, t,dt, steps)
xyz_ode = odeint(lorenz, xyz_ode, t,args = (sigma,beta,rho))

wykresy(xyz,xyz_ode)