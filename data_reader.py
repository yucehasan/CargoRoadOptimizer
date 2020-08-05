import pandas as pd
import math
import sys

def intersection(p1x, p1y, p2x, p2y, cx, cy, circle_radius, full_line=False, tangent_tol=1e-9):

    (x1, y1), (x2, y2) = (p1x - cx, p1y - cy), (p2x - cx, p2y - cy)
    dx, dy = (x2 - x1), (y2 - y1)
    dr = (dx ** 2 + dy ** 2)**.5
    big_d = x1 * y2 - x2 * y1
    discriminant = circle_radius ** 2 * dr ** 2 - big_d ** 2

    if discriminant < 0:  # No intersection between circle and line
        return []
    else:  # There may be 0, 1, or 2 intersections with the segment
        intersections = [
            (cx + (big_d * dy + sign * (-1 if dy < 0 else 1) * dx * discriminant**.5) / dr ** 2,
             cy + (-big_d * dx + sign * abs(dy) * discriminant**.5) / dr ** 2)
            for sign in ((1, -1) if dy < 0 else (-1, 1))]  # This makes sure the order along the segment is correct
        if not full_line:  # If only considering the segment, filter out intersections that do not fall within the segment
            fraction_along_segment = [(xi - p1x) / dx if abs(dx) > abs(dy) else (yi - p1y) / dy for xi, yi in intersections]
            intersections = [pt for pt, frac in zip(intersections, fraction_along_segment) if 0 <= frac <= 1]
        if len(intersections) == 2 and abs(discriminant) <= tangent_tol:  # If line is tangent to circle, return just one point (as both intersections have same location)
            return [intersections[0]]
        else:
            return intersections

def main():

    f = open("distances.txt", "w")
    locations = pd.read_excel(sys.argv[1], sheet_name='Locations')
    loc_x_coordinates = locations['X Coordinate'].values.tolist()
    loc_y_coordinates = locations['Y Coordinate'].values.tolist()
    distances = []
    for i in range(30):
        for j in range(30):
            if i != j:
                x1 = loc_x_coordinates[i]
                x2 = loc_x_coordinates[j]
                y1 = loc_y_coordinates[i]
                y2 = loc_y_coordinates[j]
                d = math.sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))
                distances.append(d)
            else:
                distances.append(0)
    f.write("----------Distances----------\n")
    for i in range(30):
        for j in range(30):
            f.write(str(distances[i*30+j]))
            f.write(", ")
        f.write("\n")
    f.close()

    f = open("availability.txt", "w")
    storms = pd.read_excel(sys.argv[1], sheet_name='Storms')
    st_x_coordinates = storms['X Coordinate'].values.tolist()
    st_y_coordinates = storms['Y Coordinate'].values.tolist()
    st_radius = storms['Radius'].values.tolist()

    usable = []

    for i in range(len(loc_x_coordinates)):
        for j in range(len(loc_x_coordinates)):
            flag = False
            for k in range(len(st_radius)):
                x1 = loc_x_coordinates[i]
                x2 = loc_x_coordinates[j]
                y1 = loc_y_coordinates[i]
                y2 = loc_y_coordinates[j]
                sx = st_x_coordinates[k]
                sy = st_y_coordinates[k]
                r = st_radius[k]
                if(i == j or intersection(x1, y1, x2, y2, sx, sy, r) != []):
                    flag = True
                    break
            if flag:
                usable.append(0)
            else:
                usable.append(1)

    f.write("----------Availability----------\n")
    for x in range(len(usable)):
        f.write(str(usable[x]))
        f.write(", ")
        if x % 30 == 29:
            f.write("\n")
    f.close()

    f = open("material.txt", "w")
    material = pd.read_excel(sys.argv[1], sheet_name='Road Material')
    materials = material['Road Material'].values.tolist()
    materials_int = []

    for m in materials:
        if m =='Asphalt':
            materials_int.append(100)
        elif m == 'Concrete':
            materials_int.append(65)
        elif m == "Gravel":
            materials_int.append(35)
        else:
            materials_int.append(0)
    count = 0
    f.write("----------Speed----------\n")
    for x in range(len(materials_int)):
        if(count % 30 == 0):
            f.write("\n")
            count = 0
        f.write(str(materials_int[x]))
        f.write(", ")
        count += 1
    f.close()

if __name__ == "__main__":
    main()