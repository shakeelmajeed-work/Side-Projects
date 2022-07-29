"""
ID: shakeel5
LANG: PYTHON3
TASK: sleepy cow herding
"""

fin = open ('herding.in', 'r')
fout = open ('herding.out', 'w')

numbers = list(map(int,fin.readline().split()))
numbers.sort()

a,b,c = numbers[0],numbers[1],numbers[2]

def finder(a,b,c):
    sols = []
    
    if c == a+2: #already consecutive
        sols.append(0)

    elif b-a == 2 or c-b==2:
        sols.append(1)
    else:
        sols.append(2)
    #end of min check
    
    sols.append(max(b - a, c - b) - 1) #max is legit just max diff between b,a and c,b (-1 because we counting number line spaces between the numbers) #didn't clock this before :()
    return sols

ans = finder(a,b,c)

fout.write(str(min(ans))+'\n'+str(max(ans))+'\n')
fout.close()