import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

def main():
    excel = sys.argv[1]
    f = open(sys.argv[2])
    roads = []
    line = f.readline()
    while line:
        points = line.split(",")
        s, d = int(points[0]), int(points[1])
        roads.append([s, d])
        line = f.readline()
    f.close()
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    # Import location info
    locations = pd.read_excel(sys.argv[1], sheet_name='Locations')
    loc_x_coordinates = locations['X Coordinate'].values.tolist()
    loc_y_coordinates = locations['Y Coordinate'].values.tolist()

    # Import road material info
    material = pd.read_excel(sys.argv[1], sheet_name='Road Material')
    materials = material['Road Material'].values.tolist()
    for i in range(len(materials)):
        if materials[i] =='Asphalt':
            materials[i] = '#2f2a2a'
        elif materials[i] == 'Concrete':
            materials[i] = '#d87b2d'
        elif materials[i] == "Gravel":
            materials[i] = '#c7bdbd'
        else:
            materials[i] = 'yellow'

    # Import storm info
    storms = pd.read_excel(sys.argv[1], sheet_name='Storms')
    st_x_coordinates = storms['X Coordinate'].values.tolist()
    st_y_coordinates = storms['Y Coordinate'].values.tolist()
    st_radius = storms['Radius'].values.tolist()

    # Write location indices
    count = 1
    for i,j in zip(loc_x_coordinates,loc_y_coordinates):
        ax.annotate(count,xy=(i + 1,j + 1))
        count += 1

    # Draw storms
    for i in range(len(st_radius)):
        a_circle = plt.Circle((st_x_coordinates[i], st_y_coordinates[i]), st_radius[i], color='red')
        ax.add_artist(a_circle)

    # Draw used roads 
    for i in range(len(roads)):
        x1, y1 = [loc_x_coordinates[roads[i][0] - 1], loc_x_coordinates[roads[i][1] - 1] ], [loc_y_coordinates[roads[i][0] - 1], loc_y_coordinates[roads[i][1] - 1] ]
        plt.plot(x1, y1, color=materials[(roads[i][0] - 1) * 30 + roads[i][1] - 1], marker = 'o')

    # Major ticks every 20, minor ticks every 5
    x_major_ticks = np.arange(min(loc_x_coordinates) - 30, max(loc_x_coordinates) + 30, 100)
    x_minor_ticks = np.arange(min(loc_x_coordinates) - 30, max(loc_x_coordinates) + 30, 10)
    # Major ticks every 20, minor ticks every 5
    y_major_ticks = np.arange(min(loc_y_coordinates) - 30, max(loc_y_coordinates) + 30, 100)
    y_minor_ticks = np.arange(min(loc_y_coordinates) - 30, max(loc_y_coordinates) + 30, 10)

    ax.set_xticks(x_major_ticks)
    ax.set_xticks(x_minor_ticks, minor=True)
    ax.set_yticks(y_major_ticks)
    ax.set_yticks(y_minor_ticks, minor=True)

    # And a corresponding grid
    ax.grid(which='both')

    # Or if you want different settings for the grids:
    ax.grid(which='minor', alpha=0.2)
    ax.grid(which='major', alpha=0.5)

    plt.scatter(loc_x_coordinates, loc_y_coordinates, s=10)

    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()