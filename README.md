# A_star_algorithm
Starting with a simple grid-based A* implementation. Will progress to more complex implementations...

The simple_grid_based_aStar works based on the assumptions that only up,down,left,right movements are allowed and the cost for moving from one cell to the other is 1.
The heuristic function used to calculate the distance to the goal node is the Euclidean Distance function ("h")
The Cost function "g" of a node, is the total cost to that node from start node
So the total cost function "f" will be f = g + h
### Instructions
NOTE: The simple_grid_based_aStar doesn't use any additional libraries
1. Import the simple_grid_based_aStar.py file
2. Call the do_a_star function
3. Pass 3 parameters
   - nxm grid of 1s and 0s
   (0 is considered as obstacle)
   - start position in grid
   - goal position in grid
