import random

def generate_maze(rows, cols):
    maze = [[1] * cols for _ in range(rows)]
    stack = [(0, 0)]
    maze[0][0] = 0

    while stack:
        current_cell = stack[-1]
        neighbors = [(current_cell[0] + 2, current_cell[1]), 
                     (current_cell[0] - 2, current_cell[1]), 
                     (current_cell[0], current_cell[1] + 2), 
                     (current_cell[0], current_cell[1] - 2)]
        unvisited_neighbors = [neighbor for neighbor in neighbors if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and maze[neighbor[0]][neighbor[1]] == 1]
        
        if unvisited_neighbors:
            chosen_neighbor = random.choice(unvisited_neighbors)
            wall = ((current_cell[0] + chosen_neighbor[0]) // 2, (current_cell[1] + chosen_neighbor[1]) // 2)
            maze[wall[0]][wall[1]] = 0
            maze[chosen_neighbor[0]][chosen_neighbor[1]] = 0
            stack.append(chosen_neighbor)
        else:
            stack.pop()

    return maze

def display_maze(maze):
    for row in maze:
        for cell in row:
            if cell == 1:
                print("#", end=" ")
            else:
                print(" ", end=" ")
        print()

def main():
    rows = int(input("Enter the number of rows in the maze: "))
    cols = int(input("Enter the number of columns in the maze: "))

    if rows % 2 == 0 or cols % 2 == 0:
        print("Please enter odd numbers for rows and columns.")
        return

    maze = generate_maze(rows, cols)
    display_maze(maze)

if __name__ == "__main__":
    main()
