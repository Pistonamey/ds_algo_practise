

class FindElements:

    def __init__(self, root):
        if root is not None:
            root.val = 0
            self.recover(root)
        self.tree = root

    def recover(self, root):
        if root.left is not None:
            root.left.val = 2 * root.val + 1
            self.recover(root.left)
        if root.right is not None:
            root.right.val = 2 * root.val + 2
            self.recover(root.right)

    def find(self, target: int) -> bool:
        return self.findelem(self.tree, target)

    def findelem(self, root, target):
        if root is None:
            return False
        if root.val == target:
            return True
        return self.findelem(root.left, target) or self.findelem(root.right, target)

# Usage example
# root = TreeNode(-1)
# root.left = TreeNode(-1)
# root.right = TreeNode(-1)
# root.left.left = TreeNode(-1)
# root.left.right = TreeNode(-1)
# obj = FindElements(root)
# print(obj.find(1))  # Should return true
# print(obj.find(3))  # Should return true
# print(obj.find(5))  # Should return false
