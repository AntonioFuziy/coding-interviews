class TreeNode:
  def __init__(self, value=None, left=None, right=None, parent=None):
    self.value = value
    self.left = left
    self.right = right
    self.parent = parent

def in_order_succ(node: TreeNode) -> TreeNode:
  if node is None:
    return None
    
  if node.right:
    node = node.right
    while node.left:
      node = node.left
    
  else:
    while node.parent and node.parent.right == node:
      node = node.parent
    return node.parent
    
  return node