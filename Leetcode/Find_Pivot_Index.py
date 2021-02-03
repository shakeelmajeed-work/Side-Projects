class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pivot = 1 
        if len(nums)==0:
            return -1
        elif len(nums)==1:
            return 0
        if sum(nums[1:])==0:
            return 0
        #defining sum of variables left on element (would be 0 but definition of pivot forces this value)
        left_sum = nums[0]
        #pivot is 1 so this is sum of 3rd to ith one
        right_sum = sum(nums[pivot+1:])
        #before even iterating, if they are the same (maybe some negative numbers) then return index of pivot (1)
        if left_sum == right_sum:
            return 1
        #indeterminate loop
        while pivot<len(nums)-1: # when pivot reaches last element and nothing is returned then there is no valid pivot index 
            
            #increment left sum by element at pivot (see line below)
            left_sum+=nums[pivot]
            #line above allows us to decrement right_sum by eventual next pivot (will be added to left sum on next iteration)
            right_sum-=nums[pivot+1]
            #increment pivot
            pivot+=1
            
            #after redefining the sums just return the index (or the pivot) 
            if left_sum==right_sum:
                return pivot
        #if loop breaks and nothing has been returned that it is not possible
        return -1
        
            
        
