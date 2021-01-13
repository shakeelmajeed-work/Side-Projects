test = int(input())
for i in range(test):
    n,k,d = map(int,input().split())
    my_array = list(map(int,input().split()))
    total = sum(my_array)
    num_of_contests = total//k
    print(min(d,num_of_contests))
   