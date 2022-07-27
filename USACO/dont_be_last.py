"""
ID: shakeel5
LANG: PYTHON3
TASK: don't be last
"""

fin = open ('notlast.in', 'r')
fout = open ('notlast.out', 'w')

cows = ['Bessie', 'Elsie', 'Daisy', 'Gertie', 'Annabelle', 'Maggie', 'Henrietta']
n = int(fin.readline())
name_to_milk = dict()

for i in range(n):
    line = [x for x in fin.readline().split()] #e.g ['Bessie',1]
    print(line)
    if line[0] in name_to_milk:
        name_to_milk[line[0]] += int(line[1])
    else: 
        name_to_milk[line[0]] = int(line[1])

minimum = 'Gertie' #random name 

#check for any missing cows not in milking log 
for cow in cows:
    if cow not in name_to_milk:
        name_to_milk[cow] = 0

#finding M (minimum)
count = 0
for key in name_to_milk.keys():
    if name_to_milk[key]<name_to_milk[minimum]:
        minimum = key #easier than just storing the value of the cow with the minimum milk
        count = 0
    if name_to_milk[key] == name_to_milk[minimum]:
        count+=1

if count == 7:
    fout.write('Tie'+'\n')
    fout.close()


#separate out dictionary by keeping any key,value pair greater than minimum's
new_dict = {key: name_to_milk[key] for key in name_to_milk.keys() if name_to_milk[key]>name_to_milk[minimum]}

for cow in cows:
    if cow in new_dict:
        minimum = cow #temp minimum to allow for below comparison code to work
        break 

for key in new_dict.keys():
    if new_dict[key]<new_dict[minimum]:
        minimum = key

for key in new_dict.keys():
    if new_dict[minimum] == new_dict[key] and key!=minimum:
        fout.write('Tie'+'\n')
        fout.close()
        exit()
else:
    fout.write(str(minimum)+'\n')
    fout.close()