class BinaryTree:
    def __init__(self, key, level = 1,parent = None):
        self.key = key
        self.left = None
        self.right = None
        self.level = level
        self.parent = parent
        
    def insert_left(self, key):
        t = BinaryTree(key,level = self.level +1 ,parent = self)
        
        if self.left is None:
            self.left = t
        else:
            t.left = self.left
            self.left = t

    def insert_right(self, key):
        t = BinaryTree(key,level = self.level +1, parent = self)
        if self.right is None:
            self.right = t
        else:
            t.right = self.right
            self.right = t
            
    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right
    
    def bfs_traversal(self):
        result = []
        if self is None:
            return result

        queue = []
        queue.append(self)

        while queue:
            current_node = queue.pop(0)
            result.append(current_node.key)

            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

        return result
    
    def dfs_traversal(self):
        result = []
        if self is None:
            return result

        stack = []
        stack.append(self)

        while stack:
            current_node = stack.pop()
            result.append(current_node.key)

            if current_node.right:
                stack.append(current_node.right)
            if current_node.left:
                stack.append(current_node.left)

        return result
    
    def get_node_parent(self, key):
        node = self.find_node(key)
        if node:
            parent = node.parent if node.parent else None
            return parent
        else:
            return None
    
    def get_level(self,element):
        node = self.find_node(element)
        return node.level
    
    def is_leaf(self,element):
        node = self.find_node(element)
        liść = False
        children = [node.left.key if node.left else None, node.right.key if node.right else None]
        if children == [None,None]: liść = True
        
        return liść

    def find_node(self, key):
        if self is None:
            return None
        if self.key == key:
            return self
        if self.left:
            left_result = self.left.find_node(key)
            if left_result:
                return left_result
        if self.right:
            right_result = self.right.find_node(key)
            if right_result:
                return right_result

        
        return None
     
    def __str__(self):
        return f"[{self.key}; {self.left}; {self.right}]"