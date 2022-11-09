# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    memo = {
      0: [], 
      1: [TreeNode(0)]
    }

    def allPossibleFBT(self, N):
        if N not in Solution.memo:
            nodes = []
            for x in range(N):
                y = N - 1 - x
                for left in self.allPossibleFBT(x):
                    for right in self.allPossibleFBT(y):
                        node = TreeNode(0)
                        node.left = left
                        node.right = right
                        nodes.append(node)
            Solution.memo[N] = nodes

        return Solution.memo[N]