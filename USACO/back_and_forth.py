"""
ID: shakeel5
LANG: PYTHON3
TASK: back and forth
"""
fin = open ('backforth.in', 'r')
fout = open ('backforth.out', 'w')


values = set()


def readings(days,b1,new1,b2,new2):
    if days == 4:
        values.add(b1)
        return
    for i in range(len(new1)):
        curr = new1[i]

        new_first_barn = new1.copy()
        del new_first_barn[i]
        new_second_barn = new2.copy()
        new_second_barn.append(curr)

        readings(days+1,b2+curr,new_second_barn,b1-curr,new_first_barn)
        #took me a long time to understand the trick in the line above 

first_barn = list(map(int,fin.readline().split()))
second_barn = list(map(int,fin.readline().split()))
readings(0,1000,first_barn,1000,second_barn)

fout.write(str(len(values))+'\n')
fout.close()