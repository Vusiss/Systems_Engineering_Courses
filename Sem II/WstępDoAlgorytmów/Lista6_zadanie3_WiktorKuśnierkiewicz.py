import networkx as nx
import matplotlib.pyplot as plt
from Lista6_zadanie2_WiktorKuśnierkiewicz import generate_graph_with_wages


#Zadanie 3
class Divided_Elements:
    def __init__(self, n):
        self.parent = [w for w in range(n)]
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        u_root = self.find(u)
        v_root = self.find(v)

        if u_root == v_root:
            return False

        if self.rank[u_root] > self.rank[v_root]:
            self.parent[v_root] = u_root
        elif self.rank[u_root] < self.rank[v_root]:
            self.parent[u_root] = v_root
        else:
            self.parent[v_root] = u_root
            self.rank[u_root] += 1

        return True
    
def kruskal(graph): 
    edges = [(weight, u, v) for u, v, weight in graph.edges(data='weight')]
    edges.sort() 

    n = len(graph.nodes())
    mdr = nx.Graph()
    ds = Divided_Elements(n) 

    for weight, u, v in edges:
        if ds.union(u, v):
            mdr.add_edge(u, v, weight=weight)

    return mdr

def prim(graph): 
    start = list(graph.nodes())[0] 
    previous = set([start])
    edges = [(weight, start, v) for v, weight in graph[start].items()] 
    mdr = nx.Graph()

    while edges:
        edges = sorted(edges, key=lambda x: x[0]['weight']) 
        weight, u, v = edges.pop(0)  
        if v not in previous:
            previous.add(v)
            mdr.add_edge(u, v, weight=weight['weight'])
            for next_v, next_weight in graph[v].items():
                if next_v not in previous:
                    edges.append((next_weight, v, next_v))

    return mdr

def show_graph(graph, title, position):
    plt.subplot(1, 3, position) 
    plt.title(title)
    position_of_elements = nx.spring_layout(graph)
    nx.draw(graph, position_of_elements, with_labels=True)
    weight = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, position_of_elements, edge_labels=weight)
 
def zad3():  
    number_of_elements = 8
    probability = 0.3
    graph = generate_graph_with_wages(number_of_elements,probability)


    plt.figure(figsize=(12, 5))
    show_graph(graph, "Graf wyjściowy", 1)
    kruskal_po = kruskal(graph)
    prim_po = prim(graph) 
    show_graph(kruskal_po, "Kruskal", 2)
    show_graph(prim_po, "Prim", 3)
    plt.tight_layout()
    plt.show()

zad3()