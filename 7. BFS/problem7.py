#connect the sister nodes with each other and the last one in every level to none

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right , self.next= None, None, None

    def print_level_order(self):
        nextLevelRoot=self
        while nextLevelRoot:
            current=nextLevelRoot
            nextLevelRoot=None

            while current:
                print(str(current.val)+ " ", end=" ")
                if not nextLevelRoot:
                    if current.left:
                        nextLevelRoot=current.left
                    elif current.right:
                        nextLevelRoot=current.right
                current = current.next
            print()


def connect_node(root):
    queue=[]
    queue.append(root)

    while queue:
        qlen=len(queue)
        previous=None
        for i in range(qlen):
            node=queue.pop(0)
            if node:
                queue.append(node.left)
                queue.append(node.right)
                if(previous):
                    previous.next=node
                previous=node
    
    return "Done"

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level order connector: ", str(connect_node(root)))
    root.print_level_order()


main()
