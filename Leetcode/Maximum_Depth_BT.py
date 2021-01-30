 def maxDepth(self, root: TreeNode) -> int:
        #first check if root is null, if so the maxDepth has to be 0
        #Recursively check the depth of the tree for left child and assign to variable
        #Do the above for the right child and asssign to variable
        #See which depth is bigger and return that depth and add one to it (accounts for root node)
        
        if root is None:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return max(left_depth, right_depth)+1
