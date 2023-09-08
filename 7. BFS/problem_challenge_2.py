#right side view of a binary tree

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def right_side_view(root):
    queue=[]
    queue.append(root)
    result=[]

    while queue:
        qlen=len(queue)
        current_level=[]
        for _ in range(qlen):
            node=queue.pop(0)
            if node:
                queue.append(node.left)
                queue.append(node.right)
                current_level.append(node.val)
        if(current_level):
            result.append(current_level[-1])
    return result

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.left.left.left=TreeNode(3)
    print("Right Side view of the binary : ", str(right_side_view(root)))


main()