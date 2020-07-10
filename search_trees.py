class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self, arr):
        self.root = None
        for i in arr:
            self.insert(self.root, Node(i))
            
    def insert(self, root, node):
        if root is None:
            self.root = node

        else:
            if root.value < node.value:
                if root.right is None:
                    root.right = node
                else:
                    self.insert(root.right, node)
            else:
                if root.left is None:
                    root.left = node
                else:
                    self.insert(root.left, node)
        
    # In-order: Left, Root, Right
    def inorder(self, node):
        if node is None:
            return
        
        self.inorder(node.left)
        print(node.value)
        self.inorder(node.right)

    # Pre-order: Root, Left, Right
    def preorder(self, node):
        if node is None:
            return

        print(node.value)
        self.preorder(node.left)
        self.preorder(node.right)

    # Post-order: Left, Right, Root
    def postorder(self, node):
        if node is None:
            return
        
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.value)

    def search(self, node, val):
        if node is None:
            print("Does not exist")
            return
        if node.value == val:
            print("Found", val, node.value, node)
            return node.value
        
        if node.value > val:
            return search(node.left, val)
        
        return search(node.right, val)

if __name__ == "__main__":
    arr = [4,3,5,1,2]
    t = Tree(arr)
    
    t.inorder(t.root)
    t.postorder(t.root)
    t.preorder(t.root)
