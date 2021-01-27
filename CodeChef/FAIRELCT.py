tests = int(input())
for t in range(tests):
    swaps = 0
    john,jack = map(int,input().split())
    john_votes = list(map(int,input().split()))
    jack_votes = list(map(int,input().split()))

    john_sum = sum(john_votes)
    jack_sum = sum(jack_votes)
    if john_sum>jack_sum:
        print(0)
        continue
    flag = False
    while john_sum <= jack_sum:
        low_index = john_votes.index(min(john_votes))
        high_index = jack_votes.index(max(jack_votes))
        if john_votes[low_index]<jack_votes[high_index]:
            john_votes[low_index],jack_votes[high_index] = jack_votes[high_index],john_votes[low_index]
            difference = abs(john_votes[low_index]-jack_votes[high_index])
            john_sum+=difference
            jack_sum-=difference
            swaps+=1
        else:
            flag=True
            break
    if flag==True:
        print(-1)
    else:
        print(swaps)



