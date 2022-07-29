"""
ID: shakeel5
LANG: PYTHON3
TASK: promotion counting
"""

fin = open ('promote.in', 'r')
fout = open ('promote.out', 'w')

bronze = list(map(int,fin.readline().split()))
silver = list(map(int,fin.readline().split()))
gold = list(map(int,fin.readline().split()))
platinum = list(map(int,fin.readline().split()))

platinum_prom = platinum[1]-platinum[0]
gold_prom = platinum_prom+gold[1]-gold[0]
silver_prom  = gold_prom+silver[1]-silver[0]

fout.write(str(silver_prom)+'\n'+str(gold_prom)+'\n'+str(platinum_prom)+'\n')
fout.close()