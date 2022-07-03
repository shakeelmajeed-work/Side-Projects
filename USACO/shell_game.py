"""
ID: shakeel5
LANG: PYTHON3
TASK: shell game
"""
fin = open ('shell.in', 'r')
fout = open ('shell.out', 'w')

shells = [1,2,3]
num_swaps = int(fin.readline())
relating_points = [0,0,0] #essentially showing the points earned if shell 1, 2 or 3 were picked


for i in range(0,num_swaps):
    a,b,g = map(int,fin.readline().split())

    #make the actual swap
    shells[a-1],shells[b-1] = shells[b-1],shells[a-1] #could have done this using a temp variable

    for i in range(1,4):
       if i == g:
        concerned = shells[g-1]
        relating_points[concerned-1] +=1

maxi_points = max(relating_points)

fout.write (str((maxi_points)) + '\n')
fout.close()
