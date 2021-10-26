from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    if root is None:
        return root

    temp = root.left
    root.left = invertTree(root.right)
    root.right = invertTree(temp)

    return root