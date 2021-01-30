class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        def pathSum(root,s):
            if not root:
                return s
            if not root.right and not root.left:
                #Will append the value when you reach leaf node (total of that path)
                self.l.append(s+root.val)
                return 
            if root.left:
                #we increment sum of path by node's value and pass in its left child
                pathSum(root.left,s+root.val)
            if root.right:
                
                #same as above 
                pathSum(root.right,s+root.val)
        #this list contains all of the possible values at end of each path
        self.l = []
        #starts code with sum as 0 so that it can be incremented
        pathSum(root,0)
        if targetSum in self.l:
            #if the target sum is in list of all the possible sum paths then return true 
            return True
