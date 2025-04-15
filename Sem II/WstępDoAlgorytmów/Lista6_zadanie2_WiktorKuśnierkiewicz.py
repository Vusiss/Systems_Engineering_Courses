import networkx as nx
import matplotlib.pyplot as plt
import random


#Zadanie 2
def generate_graph_with_wages(number_of_elements,probability):
    graph = nx.gnp_random_graph(number_of_elements, probability)
    for (u, v, w) in graph.edges(data=True):
        w['weight'] = random.randint(1, 10)
    
    return graph
    
def use_dijkstras_algorithm(graph, start, end): 
    S = set() 
    Q = set(graph.nodes()) 
    d = {element: float('inf') for element in graph.nodes()}
    d[start] = 0
    p = {element: -1 for element in graph.nodes()} 
    while Q:
        u = min(Q, key=lambda element: d[element])
        Q.remove(u)
        S.add(u)
        for w in graph.neighbors(u):
            if w not in Q:
                continue

            if d[w] > d[u] + graph[u][w]['weight']: 
                d[w] = d[u] + graph[u][w]['weight']
                p[w] = u


    path = []
    current = end
    while current != -1:
        path.append(current)
        current = p[current]
    path.reverse()
    return d[end], path

def show_graph(graph, title):
    plt.title(title)
    position = nx.spring_layout(graph)
    nx.draw(graph, position, with_labels=True)
    weight = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, position, edge_labels=weight)
    plt.show()

def zad2():
    number_of_elements = 10
    probability = 0.3

    graph = generate_graph_with_wages(number_of_elements,probability)

    start = random.randint(0, number_of_elements-1)
    end = random.randint(0, number_of_elements-1)
    while start == end:
        end = random.randint(0, number_of_elements-1)


    l, path = use_dijkstras_algorithm(graph, start, end)
    print(start,end)
    if l == float('inf'):
        print("Nie istnieje sciezka miedzy wierzcholkami")
    else:
        print(path)
        print(l)
    show_graph(graph, "Graf z wagami")
    
# zad2()