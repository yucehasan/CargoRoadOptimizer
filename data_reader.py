import pandas as pd
import math

def intersect(Ax, Ay, Bx, By, Cx, Cy, R):

    # compute the euclidean distance between A and B
    LAB = math.sqrt( (Bx-Ax)**2 +(By-Ay)**2 )

    # compute the direction vector D from A to B
    Dx = (Bx-Ax)/LAB
    Dy = (By-Ay)/LAB

    # the equation of the line AB is x = Dx*t + Ax, y = Dy*t + Ay with 0 <= t <= LAB.

    # compute the distance between the points A and E, where
    # E is the point of AB closest the circle center (Cx, Cy)
    t = Dx*(Cx-Ax) + Dy*(Cy-Ay)    

    # compute the coordinates of the point E
    Ex = t*Dx+Ax
    Ey = t*Dy+Ay

    # compute the euclidean distance between E and C
    LEC = math.sqrt((Ex-Cx)**2+(Ey-Cy)**2)

    # test if the line intersects the circle
    if( LEC < R ):
        return True


    # tangent point to circle is E or line doesn't touch circle
    else:
        return False

locations = pd.read_excel('data.xlsx', sheet_name='Locations')

loc_x_coordinates = locations['X Coordinate'].values.tolist()
loc_y_coordinates = locations['Y Coordinate'].values.tolist()
distances = []
'''for i in range(30):
    for j in range(30):
        if i != j:
            x1 = loc_x_coordinates[i]
            x2 = loc_x_coordinates[j]
            y1 = loc_y_coordinates[i]
            y2 = loc_y_coordinates[j]
            d = math.sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))
            distances.append(d)

print(distances)
print(len(distances))
'''
'''
Ax = float(input("X coordinate of point A:"))
Ay = float(input("Y coordinate of point A:"))
Bx = float(input("X coordinate of point B:"))
By = float(input("Y coordinate of point B:"))
Cx = float(input("X coordinate of center of circle:"))
Cy = float(input("Y coordinate of center of circle:"))
R  = float(input("Radius of circle:"))'''

storms = pd.read_excel('data.xlsx', sheet_name='Storms')
material = pd.read_excel('data.xlsx', sheet_name='Road Material')

st_x_coordinates = storms['X Coordinate'].values.tolist()
st_y_coordinates = storms['Y Coordinate'].values.tolist()
st_radius = storms['Radius'].values.tolist()

materials = material['Road Material'].values.tolist()


usable = []

for i in range(30):
    for j in range(30):
        flag = False
        for k in range(20):
            if i != j:
                x1 = loc_x_coordinates[i]
                x2 = loc_x_coordinates[j]
                y1 = loc_y_coordinates[i]
                y2 = loc_y_coordinates[j]
                sx = st_x_coordinates[k]
                sy = st_y_coordinates[k]
                r = st_radius[k]
                if(intersect(x1, y1, x2, y2, sx, sy, r)):
                    flag = True
                    break
        if flag:
            usable.append(0)
        else:
            usable.append(1)

'''for x in range(len(usable)):
    print(usable[x], end=' ')
    if x % 30 == 29:
        print()
'''

materials_int = []

for m in materials:
    if m =='Asphalt':
        materials_int.append(100)
    elif m == 'Concrete':
        materials_int.append(65)
    else:
        materials_int.append(35)

for x in range(len(materials_int)):
    if x % 30 != 29:
        print(materials_int[x], end=', ')
    else:
        print()
