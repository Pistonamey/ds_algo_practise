# minimum depth of a binary tree

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def min_depth_bfs(root):
    queue = []
    queue.append(root)
    min_depth = 1

    while queue:
        min_depth += 1
        qlen = len(queue)
        for i in range(qlen):
            node = queue.pop(0)
            if node:
                if(not(node.right) and not(node.left)):
                    return min_depth
                queue.append(node.left)
                queue.append(node.right)


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(10)
    root.left.right = TreeNode(2)
    print("Minimum depth : ", str(min_depth_bfs(root)))
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(5)
    print("minimum depth : ", str(min_depth_bfs(root)))


main()
