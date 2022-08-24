"""
ID: shakeel5
LANG: PYTHON3
TASK: milk factory
"""

fin = open ('factory.in', 'r')
fout = open ('factory.out', 'w')

n = int(fin.readline())

incoming = [0]*n
outgoing = [0]*n #smart way of solving this (finding num of sinks/roots)
for i in range(n-1):
    a, b = map(int, fin.readline().split())

    outgoing[a-1] +=1
    incoming[b-1] +=1

ans = -1

if outgoing.count(0) > 1: #no answer since there has to be only one sink in total
    ans = -1
else:
    ans = outgoing.index(0) + 1

fout.write(str(ans)+'\n')
fout.close()
