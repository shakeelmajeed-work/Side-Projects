"""
ID: shakeel5
LANG: PYTHON3
TASK: Blocked Billboard II
"""
#https://ncs6-my.sharepoint.com/:o:/g/personal/22smajeed_ncs6_org/EpQ61Z4a7zdOtUAB0oYG2aYBlpI-jpShZ-0Q_R4az1AnFQ?e=ZmWdz9
fin = open('billboard.in', 'r')
fout = open('billboard.out', 'w')

def covered_corner(x,y,BLcx,BLcy,TRcx,TRcy):
    return (x>=BLcx and x<=TRcx and y>=BLcy and y<=TRcy)


BLlx,BLly,TRlx,TRly = map(int,fin.readline().split()) 
BLcx,BLcy,TRcx,TRcy = map(int,fin.readline().split()) 

corners_covered = 0
if covered_corner(BLlx,BLly,BLcx,BLcy,TRcx,TRcy): #bottom left corner
    corners_covered+=1
if covered_corner(BLlx,TRly,BLcx,BLcy,TRcx,TRcy): #top left corner
    corners_covered+=1
if covered_corner(TRlx,BLly,BLcx,BLcy,TRcx,TRcy): #bottom right corner
    corners_covered+=1
if covered_corner(TRlx,TRly,BLcx,BLcy,TRcx,TRcy): #top right corner
    corners_covered+=1

area_lawnmower = (TRlx-BLlx) * (TRly-BLly)

if corners_covered <= 1:
    fout.write(str(area_lawnmower)+'\n')
    fout.close()
elif corners_covered == 2:
    #finding area of rect intersection
    width = min(TRlx,TRcx) - max(BLlx,BLcx)
    height = min(TRly,TRcy) - max(BLly,BLcy)

    interesection_area = area_lawnmower - (width*height)
    fout.write(str(interesection_area)+'\n')
    fout.close()
else:
    fout.write(str(0)+'\n')
    fout.close()    



