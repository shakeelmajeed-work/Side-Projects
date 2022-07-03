"""
ID: shakeel5
LANG: PYTHON3
TASK: mixing milk
"""
fin = open ('mixmilk.in', 'r')
fout = open ('mixmilk.out', 'w')

c1,m1 = map(int, fin.readline().split())
c2,m2 = map(int,fin.readline().split())
c3,m3 = map(int,fin.readline().split())

def milk_rules(c1,m1,c2,m2): #this whole mechanism was something I couldn't come up with...
    amount_to_pour = min(m1,c2-m2)

    m2+=amount_to_pour
    m1-=amount_to_pour

    return [c1,m1,c2,m2]
    

for i in range(1,100): #will handle the final pour seperately 
    pour = milk_rules(c1,m1,c2,m2)
    c1,m1,c2,m2 = pour[0],pour[1],pour[2],pour[3]
    
    
    pour = milk_rules(c2,m2,c3,m3)
    c2,m2,c3,m3 = pour[0],pour[1],pour[2],pour[3]
   

    pour = milk_rules(c3,m3,c1,m1)
    c3,m3,c1,m1 = pour[0],pour[1],pour[2],pour[3]  


final_pour = milk_rules(c1,m1,c2,m2)
c1,m1,c2,m2 = final_pour[0],final_pour[1],final_pour[2],final_pour[3]


fout.write(str(m1) + '\n'+str(m2)+'\n'+str(m3)+'\n')
fout.close()
