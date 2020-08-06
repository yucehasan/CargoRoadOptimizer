# CargoRoadOptimizer

This project aims to define a route for a truck on an island which will deliver its cargo. There are 30 locations on the island including the one that truck starts at. There are roads between each location. Roads can be made of three materials: asphalt, gravel and concrete. Each material allows the truck to move in certain speed. Also, there are storms on the island which are in circular shape. Storms may obstruct the roads and make them unavailable for the truck. Truck needs to travel each location exactly once and return back to the starting location. Route optimization is an example of the Travelling Salesman Problem (TSP). Considering that, this problem is modelled as a TSP.

##Dependencies:
    -Xpress Workbench 3.3
    -xlrd
    -pandas
    -matplotlib
    -Python 3.x

##How to use:

    Put data.xlsx into the source file containing Python scripts. 
    Then run data_reader.py. This will create three files containing parameters for model.
    After that run IE400Project.mos. This will create selected route as location pairs
    Lastly, run plot.py. This will create an image with name route.png. This is the representation of locations, storms and selected route