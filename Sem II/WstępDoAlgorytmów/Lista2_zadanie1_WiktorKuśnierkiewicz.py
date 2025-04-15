import random
import time
import matplotlib.pyplot as plt
import math
import copy

def bubble(ist : list):
    
    for i in range(len(ist)):
        for j in range(len(ist) - 1 - i):
            if ist[j] > ist[j + 1]:
                p = ist[j]
                ist[j], ist[j + 1] = ist[j + 1], p
    return ist

def sort_by_inserion(List):
    for i in range(len(List)):
        for j in range(i):
            if List[i] < List[j]:
                temp = List[i]
                List[i], List[j] = List[j], temp
    return List

def sort_by_selection(List):
    for i in range(len(List)):
        for j in range(i + 1, len(List)):
            if List[i] > List[j]:
                temp = List[i]
                List[i], List[j] = List[j], temp 
    return List

# b)

def get_runtime(func, List):
    t = 0
    max = 0
    mid = 0
    for i in range(10):
        
        start = time.time()
        func(copy.deepcopy(List))
        end = time.time()
        
        t = end - start
        mid += t
        if max < t:
            max = t
    mid /= 10
    return [max, mid]

def gen_table(n):
    return [random.randint(1, 10000) for i in range(n)]

tab = gen_table(12)
b1 = get_runtime(bubble,tab.copy())
b2 = get_runtime(sort_by_inserion,tab.copy())
b3 = get_runtime(sort_by_selection,tab.copy())


# c)

lenght = [10, 20, 50, 100, 200, 500, 1000]
funkcje_sortowania = [bubble, sort_by_inserion, sort_by_selection]

mid_time = {func.__name__: [] for func in funkcje_sortowania}
max_time = {func.__name__: [] for func in funkcje_sortowania}
print(mid_time)

for i in lenght:
    tab = gen_table(i)
    for func in funkcje_sortowania:
        mid_time[func.__name__].append(get_runtime(func, tab.copy())[1])
        max_time[func.__name__].append(get_runtime(func, tab.copy())[0])

for funkcja in funkcje_sortowania:
    plt.plot(lenght, mid_time[funkcja.__name__], label=f'Mid {funkcja.__name__}')
    plt.plot(lenght, max_time[funkcja.__name__], label=f'Max {funkcja.__name__}')

plt.legend()
plt.grid(True)
plt.show()

# d)

def bubble_stop(List):
    List_copy = List.copy()
    for i in range(len(List)):
        for j in range(0, len(List) - 1 - i):
            if List[j] > List[j + 1]:
                temp = List[j]
                List[j], List[j + 1] = List[j + 1], temp
        if i != 0 and List_copy == List:
            return List
        List_copy = List.copy()
    return List

def bubble_slower(List):
    for i in range(len(List)):
        for j in range(0, len(List) - 1): 
            if List[j] > List[j + 1]:
                temp = List[j]
                List[j], List[j + 1] = List[j + 1], temp
    return List

# e)

e1 = get_runtime(bubble,tab.copy())
e2 = get_runtime(bubble_stop,tab.copy())
e3 = get_runtime(bubble_slower,tab.copy())
print(e1,e2,e3, sep= "\n")

# f)

n = [10, 100, 1000]
funcs = [bubble, sort_by_inserion, sort_by_selection]

for n in n:
    
    tab = gen_table(n)
    
    for func in funcs:
        start = time.time()
        func(tab.copy())
        end = time.time()
        t = end - start
        print(n * math.log(n) / t)
