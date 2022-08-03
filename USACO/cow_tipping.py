"""
ID: shakeel5
LANG: PYTHON3
TASK: cow tipping 
"""
#Learnt this from: https://www.youtube.com/watch?v=n3Wmor6RpzE
fin = open ('cowtip.in', 'r')
fout = open ('cowtip.out', 'w')

n = int(fin.readline())
grid = []
tips = 0

for i in range(n):
    line = list(fin.readline().strip())
    add = []
    for l in line:
        add.append(int(l))
    grid.append(add)

for row in range(n-1,-1,-1):
    for column in range(n-1,-1,-1):
        if grid[row][column] == 1:
            tips+=1
            for x in range(row+1):
                for y in range(column+1): #because going up to grid[row][column] which is bottom right corner of rect sub-grid
                    if grid[x][y] == 1:
                        grid[x][y] = 0
                    else:
                        grid[x][y] = 1

fout.write(str(tips)+'\n')
fout.close()