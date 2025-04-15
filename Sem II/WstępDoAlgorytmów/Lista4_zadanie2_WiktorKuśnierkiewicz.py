from Lista4_classes_WiktorKuśnierkiewicz import BinaryTree
import networkx as nx
import matplotlib.pyplot as plt

def DFS_on_queue(branch, Queue):
    
    stack = []
    stack.insert(0,branch)

    while stack != []:
        branch = stack.pop(0)
        Queue.append(branch)
        if branch != None:
            if branch.right:
                stack.insert(0,branch.right)
            else: stack.insert(0,None)
            if branch.left:
                stack.insert(0,branch.left)
            else: stack.insert(0,None)

def new_tree_from_leaf(leaf : BinaryTree):
    
    def new_tree(node, Q,parentJ=None):
        if node != None:
            new_root = BinaryTree(node.key,parent=parentJ)
            if Q != []:
                new_root.left = new_tree(Q.pop(0), Q,parentJ=new_root)
            if Q != []:
                new_root.right = new_tree(Q.pop(0), Q,parentJ=new_root)
            return new_root
        else: return None

    queue = []
    queue.append(leaf)

    while leaf.parent:
        queue.append(leaf.parent)
        if leaf.parent.left != leaf:
            DFS_on_queue(leaf.parent.left, queue)
        if leaf.parent.right != leaf:
            DFS_on_queue(leaf.parent.right, queue)
        leaf = leaf.parent
        
      
    return new_tree(queue.pop(0), queue)

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
    
    return bin

def binary_tree_graph(tree : BinaryTree,n : list):
    
    graph = nx.Graph()
    for i in n:
        k = n.index(i)
        if k > 0:
            graph.add_edge(n[k], tree.get_node_parent(n[k]).key)
    
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True)
    plt.show()


bin = drzewo(0)
leaf = bin.left.right
second_bin = new_tree_from_leaf(leaf)



print(bin)
print(second_bin)
binary_tree_graph(bin,bin.bfs_traversal())

