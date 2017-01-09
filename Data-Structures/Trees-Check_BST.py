# Enter your code here. Read input from STDIN. Print output to STDOUT
""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""

def checkBST(root):
    ret = [root.data, root.data]
    if (not root.left) and (not root.right): return ret
    if root.left:
        left = checkBST(root.left)
        if not left or left[1] >= root.data: return None
        ret[0] = left[0]
    if root.right:
        right = checkBST(root.right)
        if not right or right[0] <= root.data: return None
        ret[1] = right[1]
    return ret
        

def check_binary_search_tree_(root):
    if not root: return True
    return True if checkBST(root) else False
