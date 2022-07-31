"""
ID: shakeel5
LANG: PYTHON3
TASK: sleepy cow sorting
"""

fin = open ('sleepy.in', 'r')
fout = open ('sleepy.out', 'w')

n = int(fin.readline())

cows = list(map(int,fin.readline().split()))
changes = n-1 #max that it could be 

for i in range(n-2,-1,-1): #least i will be is 0 
    if cows[i] < cows[i+1]:
        changes = i
    else:
        break 


fout.write(str(changes)+'\n')
fout.close()