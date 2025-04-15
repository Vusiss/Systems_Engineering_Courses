from Lista4_classes_WiktorKuśnierkiewicz import BinaryTree
import networkx as nx
import matplotlib.pyplot as plt
    
    
def is_leaf_level(element,tree : BinaryTree):
        return tree.is_leaf(element),tree.get_level(element)    
    
def binary_tree_graph(tree : BinaryTree):
    n = tree.bfs_traversal()
    graph = nx.Graph()
    for i in n:
        k = n.index(i)
        if k > 0:
            graph.add_edge(n[k], tree.get_node_parent(n[k]).key)
    
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True)
    plt.show()
    
def poziom_drzewa(gałąź : BinaryTree, lewo = None, prawo = None):

        if lewo != None: gałąź.insert_left(lewo)
        if prawo != None: gałąź.insert_right(prawo)
        
        return gałąź
     
def drzewo(root):
    
    bin = BinaryTree(root)
    bin = poziom_drzewa(bin,1,2)

    a = bin.get_left_child()
    b = bin.get_right_child()

    a = poziom_drzewa(a,3,4)
    b = poziom_drzewa(b,5,6)
    
    c = a.get_left_child()
    d = a.get_right_child()
    
    c = poziom_drzewa(c,7,8)
    d = poziom_drzewa(d,9,10)
    
    return bin


bin = drzewo(0)
bfs = bin.bfs_traversal()

def a():
    binary_tree_graph(bin)

def b():
    elements = [0,0,0,0]
    leaves = 0
    for i in bfs:
        elements[bin.get_level(i)-1] +=1
        if bin.is_leaf(i): leaves +=1

    print(leaves, elements)

def c():
    level = None
    nearest_leaves = []
    for i in bfs:
        if bin.is_leaf(i) and level==None: 
            level = bin.get_level(i)
        if bin.get_level(i) == level:
            nearest_leaves.append(i)
            
    print(nearest_leaves)

a()