class Solution:
    def canPlaceFlowers(self, l: List[int], n: int) -> bool:
        free = 0
        for i in range(len(l)):
            #i==0 and i==len(l)-1 is for the indexes of start and end of list 
            if l[i]==0 and (i==0 or l[i-1]==0) and (i==len(l)-1 or l[i+1]==0):
                l[i]=1
                free+=1
            if free>=n:
                return True
        return False
