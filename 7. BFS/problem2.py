# reverse level order traversal of a binary tree


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def reverse_level_order(Tree):
    queue = []
    queue.append(Tree)
    result = []
    while queue:
        qlen = len(queue)
        current_level = []
        for i in range(qlen):
            node = queue.pop(0)
            if node:
                queue.append(node.left)
                queue.append(node.right)
                current_level.append(node.val)
        if(current_level):
            # only change - insert at start instead of the end.
            result.insert(0, current_level)

    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("reverse Level order traversal : ", str(reverse_level_order(root)))


main()
