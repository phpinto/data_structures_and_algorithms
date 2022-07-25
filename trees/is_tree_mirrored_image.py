class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def is_mirror(left_node, right_node):

    if left_node.val is None and right_node.val is None:
        return True
    if left_node.val is None or right_node.val is None:
        return False
    
    return left_node.val == right_node.val and \
        is_mirror(left_node.left, right_node.right) and \
        is_mirror(left_node.right, right_node.left)

def is_tree_mirrored_image(root):
    if root is None:
        return True
    
    return is_mirror(root.left, root.right)
