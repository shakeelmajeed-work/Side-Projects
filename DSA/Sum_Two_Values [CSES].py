import enum


n,x = map(int,input().split())
vals = list(map(int,input().split()))

#I initially filled the required dict but meant that in some cases I exceeded the run time hence I do the same work I did for the making of the dict but just below
found = False
my_dict = {}

for i, val in enumerate(vals):
    if x-val in my_dict:
        print(i+1,my_dict[x-val])
        found = True
        break
    else:
        my_dict[val] = i+1 #have unique keys 

if not found:
    print("IMPOSSIBLE")