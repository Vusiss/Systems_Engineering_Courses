import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import pandas as pd


def zad1(f = 10):
    
    t = np.linspace(0, 1, 1000) 

    x_sin = np.sin(2 * np.pi * f * t)
    x_rect = signal.square(2 * np.pi * f * t)
    x_saw = signal.sawtooth(2 * np.pi * f * t)
    f1 = 10
    f2 = 40
    x_chirp = signal.chirp(t, f0=f1, f1=f2, t1=t[-1], method='linear')

    x_super = np.sin(2 * np.pi * f1 * t) + 0.5 * np.cos(2 * np.pi * f2 * t)
    x_imp = np.zeros(len(t))
    x_imp[0] = 1
    
    ig, axs = plt.subplots(6, figsize=(8, 12))


    signals = [x_sin, x_rect, x_saw, x_chirp, x_super, x_imp]
    titles = ['Sygnał sinusoidalny','Sygnał prostokątny','Sygnał piłokształtny','Sygnał świergotliwy','Superpozycja funkcji sinus i cosinus','Impuls jednostkowy']


    for i in range(6):
        axs[i].plot(t, signals[i])
        axs[i].set_title(titles[i])
        axs[i].set_xlabel('Czas [s]')
        axs[i].set_ylabel('Amplituda')

    plt.tight_layout()
    plt.show()
      
def zad2_3():
    fs = 100.0 
    t = np.arange(0, 1, 1/fs)  
    f = 10.0 
    A = 1.0  
    sygnał = A * np.sin(2 * np.pi * f * t)

    
    sygnał_szum = sygnał + 0.1 * np.random.randn(len(t))

 
    pd.DataFrame(sygnał_szum).to_csv('sygnał.csv',  index=False)

    sygnał_wczytany = pd.read_csv('sygnał.csv', header=None)
    
    print(sygnał_wczytany)

def zad4():
    t = np.arange(0, 100, 0.1)
    x_rand = np.random.rand(len(t))
    x_randn = np.random.randn(len(t))

    ig, axs = plt.subplots(2, figsize=(8, 12))
    axs[0].hist(x_rand, bins=50, label='rand', edgecolor='black')
    axs[0].set_title('Histogram rand')
    axs[1].hist(x_randn, bins=50, label='randn', edgecolor='black')
    axs[1].set_title('Histogram randn')
    plt.legend()
    plt.show()

def zad5():
    t = np.arange(0, 10, 0.1)
    x1 = np.random.normal(0, 1, len(t))
    x2 = np.random.normal(2, 3, len(t))
    x3 = np.random.normal(-1, 2, len(t))

    # Wyznaczenie histogramów
    ig, axs = plt.subplots(3, figsize=(8, 12))
    axs[0].hist(x1, bins=50, label='μ=0, σ=1')
    axs[1].hist(x2, bins=50, label='μ=2, σ=3')
    axs[2].hist(x3, bins=50, label='μ=-1, σ=2')
    plt.show()
    
def zad6():
    t = np.arange(0, 10, 0.1)
    x = np.cumsum(np.random.randn(len(t)))

    # Wyznaczenie histogramu
    plt.hist(x, bins=50)
    plt.show()
    
def zad7():
    # t1 = np.arange(0, 10, 0.1)
    # t2 = np.arange(0, 10, 0.1)
    # x = np.zeros((len(t1), len(t2)))
    # for i in range(len(t1)):
    #     for j in range(len(t2)):
    #         x[i, j] = np.cumsum(np.random.randn(i+1)) + np.cumsum(np.random.randn(j+1))

    # plt.imshow(x, cmap='hot', interpolation='nearest')
    # plt.show()
    def generate_brownian_motion(n, delta=1, start_pos=(0, 0)):
        
        x0, y0 = start_pos
        dX = np.random.normal(0, delta, size=(n, 2))  # Kroki losowe w obu wymiarach
        X = np.cumsum(dX, axis=0)  # Skumulowana suma tworząca trajektorię ruchu Browna
        X[:, 0] += x0
        X[:, 1] += y0
        return X[:, 0], X[:, 1]

    # Parametry symulacji
    n_steps = 1000  # Liczba kroków

    delta = 1  # Skalowanie losowego ruchu
    x, y = generate_brownian_motion(n_steps, delta)

    # Wizualizacja
    plt.figure(figsize=(8, 8))
    plt.plot(x, y, linestyle='-', linewidth=1, alpha=0.75, label="Ruch Browna")
    plt.scatter(x[0], y[0], color='red', label='Start')
    plt.scatter(x[-1], y[-1], color='blue', label='Koniec')
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Dwuwymiarowy szum czerwony (Ruch Browna)")
    plt.legend()
    plt.grid()
    plt.show()