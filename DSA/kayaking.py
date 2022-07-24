n = int(input())
tandems = n-1
singles = 2

weights = list(map(int,input().split()))
weights = sorted(weights)

min_ans = 100000000

for i in range(len(weights)):
    for j in range(i+1,len(weights)): #see every possible combi of people in single kayaks
        remaining = [weights[p] for p in range(len(weights)) if p!=i and p!=j] #to prevent 3rd for loop from iterating over any weight in the chosen kayak pair
        curr = 0
        for k in range(0,len(remaining)-1,2):
            curr+=abs(remaining[k]-remaining[k+1])
        min_ans = min(curr,min_ans)
print(min_ans)