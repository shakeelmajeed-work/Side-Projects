"""
ID: shakeel5
LANG: PYTHON3
TASK: grass planting  
"""

fin = open ('planting.in', 'r')
fout = open ('planting.out', 'w')

n = int(fin.readline())

deg_list = [0]*(n+1)

for i in range(n-1): 
    l = fin.readline()
    con = l.split()
    a,b = int(con[0])-1,int(con[1])-1

    deg_list[a]+=1
    deg_list[b]+=1

max_degree = max(deg_list)

max_degree+=1 #account for extra colour needed for the other node 

fout.write(str(max_degree)+'\n')
fout.close()