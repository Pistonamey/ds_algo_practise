#connect all the node to each other in level order

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right , self.next= None, None, None

    def print_level_order(self):
        current=self
        while current:
            print(str(current.val)+ " ",end=' ')
            current=current.next


def connect_node(root):
    queue=[]
    queue.append(root)
    previous=None
    while queue:
        qlen=len(queue)
        for i in range(qlen):
            node=queue.pop(0)
            if node:
                queue.append(node.left)
                queue.append(node.right)
                if(previous):
                    previous.next=node
                previous=node
    previous.next=None
    
    return "Done"

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level order all connector: ", str(connect_node(root)))
    root.print_level_order()


main()
