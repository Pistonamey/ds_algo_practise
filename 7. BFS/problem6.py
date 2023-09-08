# minimum depth of a binary tree

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def next_node(root, given_node):
    queue = []
    queue.append(root)
    min_depth = 1
    result = []
    while queue:
        min_depth += 1
        qlen = len(queue)
        for i in range(qlen):
            node = queue.pop(0)
            if node:
                queue.append(node.left)
                queue.append(node.right)
                result.append(node.val)

    index = result.index(given_node)
    return result[index+1]


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)

    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level order successor: ", str(next_node(root, 12)))
    print("Level order successor : ", str(next_node(root, 9)))


main()
