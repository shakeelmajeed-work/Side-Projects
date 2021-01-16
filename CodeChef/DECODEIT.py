# if low and high are equal to each other index alphabet list 
#0000
#0,15
#0,7
#0,3
#0,1
#0,0

#1001
#0,15
#8,15
#8,11
#8,9
#9,9
t = int(input())
alpha = 'abcdefghijklmnop'
ans = []
def decoder(length,digit):
    for i in range(0,length,4):
        sub = digit[i:i+4]
        low,high = 0,15
        for j in range(len(sub)):
            if sub[j] == '0':
                high = (low+high)//2
            else:
                low = (low+high)//2+1
        if low==high:
            ans.append(alpha[low])
            
    return (ans)


while t!=0:
    length = int(input())
    digit = input()
    ans = decoder(length,digit)
    print(''.join(ans))
    ans.clear()
    t-=1
