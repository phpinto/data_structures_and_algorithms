def is_bst(root_node, min=None, max=None):
    if root_node is None:
        return True
    if root_node.data < min or root_node.data > max:
        return False
    return is_bst(root_node.left,min,root_node.data - 1) and is_bst(root_node.right,root_node.data,max)
    

    