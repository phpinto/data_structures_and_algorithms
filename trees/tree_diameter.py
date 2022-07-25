class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        node = self
        if node != None:
            s = str(node.val)
            if node.left: 
                s = node.left.__str__() + ' ' + s
            if node.right:
                s += ' ' + node.right.__str__()
            return s
        return ''

def get_height_and_d(node, d):

    if node is None:
        return -1, d
    lh, d = get_height_and_d(node.left,d)
    rh, d = get_height_and_d(node.right,d)
    d = max(d, (lh + rh + 2))

    return max(lh,rh) + 1, d

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.left.right.left = TreeNode(8)
root.left.right.right = TreeNode(9)
root.right.right.right = TreeNode(10)

print("Tree: " + root.__str__())
root_height, d = get_height_and_d(root, 0)
print("Root Height: %s Diameter: %s" % (root_height, d))

root = TreeNode('A')
root.left = TreeNode('D')
root.right = TreeNode('Z')
root.left.left = TreeNode('H')
root.left.right = TreeNode('L')
root.right.right = TreeNode('C')
root.left.right.right = TreeNode('P')
root.right.right.right = TreeNode('G')
root.right.right.left = TreeNode('B')
root.right.right.left.right = TreeNode('E')

print()
print("Tree: " + root.__str__())
root_height, d = get_height_and_d(root, 0)
print("Root Height: %s Diameter: %s" % (root_height, d))

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.right.right = TreeNode(7)
root.left.right.right.right = TreeNode(8)
root.left.right.right.right.right = TreeNode(9)
root.left.right.right.right.right.right = TreeNode(10)
root.left.right.left = TreeNode(6)
root.left.right.left.left = TreeNode(11)
root.left.right.left.left.left = TreeNode(12)
root.left.right.left.left.left.left = TreeNode(13)
root.left.right.left.left.left.left.left = TreeNode(14)

print()
print("Tree: " + root.__str__())
root_height, d = get_height_and_d(root, 0)
print("Root Height: %s Diameter: %s" % (root_height, d))