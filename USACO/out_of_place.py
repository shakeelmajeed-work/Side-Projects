"""
ID: shakeel5
LANG: PYTHON3
TASK: sleepy cow sorting
"""

fin = open ('outofplace.in', 'r')
fout = open ('outofplace.out', 'w')

n = int(fin.readline())
heights = []

for i in range(n):
    heights.append(int(fin.readline()))

sortd = sorted(heights)
swaps = 0

for i in range(len(sortd)):
    if heights[i] != sortd[i]:
        swaps+=1
        
fout.write(str(swaps-1)+'\n')
fout.close()