# calculate the average of every single level

import statistics


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def average_bfs(root):
    queue = []
    queue.append(root)
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
            result.append(statistics.mean(current_level))

    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.left.right = TreeNode(2)
    root.right.right = TreeNode(5)
    print("average for Level order traversal : ", str(average_bfs(root)))


main()
