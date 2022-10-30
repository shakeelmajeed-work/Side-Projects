"""
ID: shakeel5
LANG: PYTHON3
TASK: Why did the cow cross the road III
"""
#https://ncs6-my.sharepoint.com/:o:/g/personal/22smajeed_ncs6_org/EpQ61Z4a7zdOtUAB0oYG2aYBlpI-jpShZ-0Q_R4az1AnFQ?e=ZmWdz9
fin = open('cowqueue.in', 'r')
fout = open('cowqueue.out', 'w')

n = int(fin.readline())
times = []

for i in range(n):
    curr = list(map(int,fin.readline().split()))
    times.append(curr)

times.sort()

track = 0 #end time of previous cow

for i in range(len(times)):
    if times[i][0]>track:
        track = times[i][0] + times[i][1]
    else:
        track += times[i][1]
fout.write(str(track)+'\n')
fout.close()

