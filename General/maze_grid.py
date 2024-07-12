import matplotlib.pyplot as plt
import numpy as np
import random

# Maze size
width, height = 10, 10

# Create grid with walls (1) and passages (0)
maze = np.ones((height, width), dtype=int)

# Directions (up, right, down, left)
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def in_bounds(x, y):
    return 0 <= x < width and 0 <= y < height

def carve_passages_from(cx, cy):
    directions_shuffled = directions[:]
    random.shuffle(directions_shuffled)
    
    for direction in directions_shuffled:
        nx, ny = cx + direction[0] * 2, cy + direction[1] * 2
        if in_bounds(nx, ny) and maze[ny][nx] == 1:
            maze[cy + direction[1]][cx + direction[0]] = 0
            maze[ny][nx] = 0
            carve_passages_from(nx, ny)

# Start carving from (1, 1)
maze[1][1] = 0
carve_passages_from(1, 1)

# Plotting the maze
fig, ax = plt.subplots(figsize=(10, 10))
ax.imshow(maze, cmap=plt.cm.binary, interpolation='nearest')
ax.set_xticks([])
ax.set_yticks([])
plt.show()
