def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        for j in range(len(nums)):
            if nums[j]!=nums[count]:
                count+=1
                nums[count]=nums[j]
        return count+1
