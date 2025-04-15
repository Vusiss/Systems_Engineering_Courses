import networkx as nx
import matplotlib.pyplot as plt

#Zadanie 1
def DFS(graph, element_on_graph, graph_part_number, list_of_parts):
    if list_of_parts[element_on_graph] == 0:
        list_of_parts[element_on_graph] = graph_part_number
        for near_element in graph[element_on_graph]:
            DFS(graph, near_element, graph_part_number, list_of_parts)
                        
def divide_into_parts(graph):
    number_of_elements = len(graph)
    list_of_parts = [0] * number_of_elements
    graph_part_number = 0

    for i in range(number_of_elements):
        if list_of_parts[i] == 0:
            graph_part_number += 1
            DFS(graph, i, graph_part_number, list_of_parts)

    return list_of_parts, graph_part_number

def show_graph(graph, title):
    plt.title(title)
    position = nx.spring_layout(graph) 
    nx.draw(graph, position, with_labels=True)
    plt.show()

def zad1():
    number_of_elements = 12
    probability = 0.1

    graph = nx.gnp_random_graph(number_of_elements, probability)
    show_graph(graph, "Graf wyjściowy")


    list_of_parts, number_of_parts = divide_into_parts(graph)

    elements = [nx.Graph() for _ in range(number_of_parts)]
    for w in range(len(list_of_parts)):
        elements[list_of_parts[w] - 1].add_node(w)

    for ss in range(number_of_parts):
        show_graph(elements[ss], "Spójna składowa {}".format(ss+1))
        
zad1()