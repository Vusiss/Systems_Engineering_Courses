from Lista4_classes_WiktorKuśnierkiewicz import BinaryTree


def drzewo():
    def poziom_drzewa(gałąź : BinaryTree, lewo, prawo):
   
        gałąź.insert_left(lewo)
        gałąź.insert_right(prawo)
    
        return gałąź
    bin = BinaryTree(0)
    bin = poziom_drzewa(bin,1,2)

    a = bin.get_left_child()
    b = bin.get_right_child()

    a = poziom_drzewa(a,3,4)
    b = poziom_drzewa(b,5,6)
    return bin

bin = drzewo()


print(bin.dfs_traversal())
print(bin.bfs_traversal())

