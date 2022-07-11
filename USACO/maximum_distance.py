n = int(input())
x_coords = list(map(int, input().split()))
y_coords = list(map(int, input().split()))

def distance_calc(x1,x2,y1,y2):
    return (x2-x1)**2+(y2-y1)**2

max_distance = 0

for i in range(n): #initally I put len(x_coords)
    for j in range(i+1,n): #initially I put len(y_coords) but i+1 gets rid of duplicates 
        curr_distance = distance_calc(x_coords[i],x_coords[j],y_coords[i],y_coords[j])
        if curr_distance>max_distance: #could use a max statement here 
            max_distance = curr_distance

print(round(max_distance))