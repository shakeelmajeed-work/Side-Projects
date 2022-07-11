"""
ID: shakeel5
LANG: PYTHON3
TASK: cow gymnastics
"""

fin = open ('gymnastics.in', 'r')
fout = open ('gymnastics.out', 'w')

k, n = map(int, fin.readline().split())
training_sessions = []
num_pairs = 0

for i in range(k):
    session = list(map(int, fin.readline().split()))
    training_sessions.append(session) #training_sessions becomes a 2d arr which we can traverse


#big mess up with regards to my understanding of how to solve this: instead of finding the combinations of the ranking of cows given the first training session as a template,
#saw solution where you 'brute force' the combination of cow numbers starting with 1,2 instead of (using test data) 4,1

for cow1 in range(1,n+1): #not really using this as an index
    for cow2 in range(1,n+1):
        if cow1 == cow2:
            continue
        
        check = 0
        for x in range(k): 
           if training_sessions[x].index(cow1)<training_sessions[x].index(cow2):
               check+=1
        if check == k:
            num_pairs+=1

fout.write(str(num_pairs)+'\n')
fout.close()