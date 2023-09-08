# zigzag level order traversal of a binary tree


class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left,self.right=None, None

def zigzag_level_order(Tree):
    queue=[]
    queue.append(Tree)
    result=[]
    left_to_right=True
    while queue:
        qlen=len(queue)
        current_level=[]
        for i in range(qlen):
            node=queue.pop(0)
            if node:
                queue.append(node.left)
                queue.append(node.right)

                #only change - have a boolean left to right
                if(left_to_right):
                    current_level.append(node.val)
                else:
                    current_level.insert(0,node.val)
        if(current_level):
            result.append(current_level)

    return result

def main():
    root = TreeNode(12)
    root.left=TreeNode(7)
    root.right=TreeNode(1)
    root.left.left=TreeNode(9)
    root.right.left=TreeNode(10)
    root.right.right=TreeNode(5)
    print("zigzag Level order traversal : ",str(zigzag_level_order(root)))

main()