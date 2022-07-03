"""
ID: shakeel5
LANG: PYTHON3
TASK: blocked billboard
"""
fin = open ('billboard.in', 'r')
fout = open ('billboard.out', 'w')

bl_x1, bl_y1, tr_x1, tr_y1 = map(int, fin.readline().split()) #rectangle/billboard 1
bl_x2, bl_y2, tr_x2, tr_y2 = map(int, fin.readline().split()) #rectangle 2
bl_x3, bl_y3, tr_x3, tr_y3 = map(int, fin.readline().split()) #truck 

#find area of each rectangle and billboard, find area of intersection between each rectangle and truck, calculate combined viewable area of each rectangle
def area(bl_x,bl_y,tr_x,tr_y):
    width = tr_x - bl_x
    length = tr_y - bl_y
    return width * length

def area_intersect(bl_x3,bl_y3,tr_x3,tr_y3,bl_x,bl_y,tr_x,tr_y): #coords of truck and one of the rectangles 
    intersect_width = max(min(tr_x3,tr_x) - max(bl_x3,bl_x),0)  #negative values mean they don't overlap
    intersect_length = max(min(tr_y3,tr_y) - max(bl_y3,bl_y),0) #negative values mean they don't overlap

    return intersect_length * intersect_width

area_1 = area(bl_x1, bl_y1, tr_x1, tr_y1)
area_2 = area(bl_x2, bl_y2, tr_x2, tr_y2)
truck_area = area(bl_x3, bl_y3, tr_x3, tr_y3)

first_overlap = area_intersect(bl_x3, bl_y3, tr_x3, tr_y3,bl_x1, bl_y1, tr_x1, tr_y1)
second_overlap = area_intersect(bl_x3, bl_y3, tr_x3, tr_y3,bl_x2, bl_y2, tr_x2, tr_y2)

fout.write (str((area_1-first_overlap)+(area_2-second_overlap)) + '\n')
fout.close()
