"""
ID: shakeel5
LANG: PYTHON3
TASK: mad scientist
"""

fin = open ('breedflip.in', 'r')
fout = open ('breedflip.out', 'w')

n = int(fin.readline())
a = str(fin.readline())
b = str(fin.readline())

flips = 0
ind = 0
mismatch = False

while ind<=len(a)-1:
    if b[ind] == a[ind]:
        mismatch = False
        ind+=1
    else:
        if not mismatch: #never thought of using bools here
            mismatch = True
            flips+=1
        ind+=1



fout.write(str(flips)+'\n')
fout.close()