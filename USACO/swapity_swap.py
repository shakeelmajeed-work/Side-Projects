"""
ID: shakeel5
LANG: PYTHON3
TASK: swapity swap
"""
#https://ncs6-my.sharepoint.com/personal/22smajeed_ncs6_org/_layouts/OneNote.aspx?id=%2Fpersonal%2F22smajeed_ncs6_org%2FDocuments%2FNotebooks%2FCoding&wd=target%28Practice.one%7C0CEE4E7B-D989-BD41-8020-FA322B679270%2FSwapity%20Swap%3A%7C1480CAD5-5455-AE4E-975A-49F8D7F5827C%2F%29onenote:https://ncs6-my.sharepoint.com/personal/22smajeed_ncs6_org/Documents/Notebooks/Coding/Practice.one#Swapity%20Swap&section-id={0CEE4E7B-D989-BD41-8020-FA322B679270}&page-id={1480CAD5-5455-AE4E-975A-49F8D7F5827C}&end
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
