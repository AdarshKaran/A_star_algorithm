# Grid Based A* Algorithm

### Key Components:

- **Binary Heap:** A custom binary heap implementation is used to efficiently store nodes in a priority queue-like structure, ensuring nodes with lower total cost (f) are given higher priority.
- **Node Representation:** Each cell in the grid is represented as a node containing information about its position, cost from the start (g), heuristic cost to the goal (h), and parent node.
- **Heuristic:** Euclidean distance is used as the heuristic function to estimate the cost from each node to the goal, guiding the search towards the target efficiently.
- **Valid Movement:** The algorithm considers four possible movements - up, down, left, and right, with diagonal movements omitted for simplicity.
- **Obstacle Avoidance:** Obstacles in the grid are represented as blocked cells, and the algorithm avoids expanding nodes that correspond to obstacles.
- **Path Reconstruction:** Once the goal node is reached, the algorithm reconstructs the shortest path by tracing back through the parent nodes from the goal to the start.

### Usage:
The algorithm takes as input a grid representing the environment, start and end points, and returns a list of coordinates representing the shortest path from the start to the end. It employs a systematic exploration strategy, expanding nodes with the lowest estimated total cost until the goal is reached or all possible paths are explored.

### Benefits:
- Efficiently finds the shortest path in a grid-based environment.
- Suitable for applications requiring path planning in robotics, video games, and navigation systems.

### Limitations:
- Assumes movement is restricted to four cardinal directions.
- Performance may degrade in large-scale grids or environments with complex obstacles.

### Applications:
- Robotic navigation in warehouses, factories, and outdoor environments.
- Video game AI for character movement and navigation.
- Routing algorithms in transportation and logistics systems.

### Test Results:
<p align="center">
  <img src="https://github.com/AdarshKaran/A_star_algorithm/blob/main/Test%20Cases/A*test_case_1.png?raw=true" alt="Test Case 1" width="600">
  <br>
  <em>Test Case 1</em>
</p>

<p align="center">
  <img src="https://github.com/AdarshKaran/A_star_algorithm/blob/main/Test%20Cases/A*test_case_2.png?raw=true" alt="Test Case 2" width="600">
  <br>
  <em>Test Case 2</em>
</p>

<p align="center">
  <img src="https://github.com/AdarshKaran/A_star_algorithm/blob/main/Test%20Cases/A*test_case_3.png?raw=true" alt="Test Case 3" width="600">
  <br>
  <em>Test Case 3</em>
</p>

<p align="center">
  <img src="https://github.com/AdarshKaran/A_star_algorithm/blob/main/Test%20Cases/A*test_case_4.png?raw=true" alt="Test Case 4" width="600">
  <br>
  <em>Test Case 4</em>
</p>

<p align="center">
  <img src="https://github.com/AdarshKaran/A_star_algorithm/blob/main/Test%20Cases/A*test_case_5.png?raw=true" alt="Test Case 5" width="900">
  <br>
  <em>Test Case 5</em>
</p>
