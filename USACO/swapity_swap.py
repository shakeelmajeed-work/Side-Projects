"""
ID: shakeel5
LANG: PYTHON3
TASK: swapity swap
"""
#https://ncs6-my.sharepoint.com/:o:/g/personal/22smajeed_ncs6_org/EpQ61Z4a7zdOtUAB0oYG2aYBlpI-jpShZ-0Q_R4az1AnFQ?e=ZmWdz9
def swap(start,end,cows):
    if start == 1:
        cows[start-1:end] = cows[end-1::-1] #because if we used the below start-2 would throw an error
        return  
    cows[start-1:end] = cows[end-1:start-2:-1]

def process(cows):
    swap(a1,a2,cows)
    swap(b1,b2,cows)

fin = open ('swap.in', 'r')
fout = open ('swap.out', 'w')

n,k = map(int,fin.readline().strip().split())
a1,a2 = map(int,fin.readline().strip().split())
b1,b2 = map(int,fin.readline().strip().split())

cows = [i for i in range(n)] #instead of having n cows starting from 1, arr will have 0 - n-1 cows
sort = False
t=0 #num of times before we reach original cows

while not sort and t<k: #if we reach k repetitions before t then break
    t+=1
    process(cows)

    sort = True
    for i in range(n):
        if cows[i] != i:
            sort = False #not in order 
            break
s = k%t

ans = cows.copy()
while s != 0:
    process(ans)
    s -= 1

#either t=k or we have simulated s number of processes that was left to do. Either way we have finished 
for i in range(n):
    fout.write(str(ans[i]+1)+'\n')
fout.close()
