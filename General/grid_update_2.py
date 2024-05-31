import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def update_grid(grid):
    new_grid = grid.copy()
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            # Count the number of live neighbors
            total = (grid[i, (j-1)%grid.shape[1]] + grid[i, (j+1)%grid.shape[1]] +
                     grid[(i-1)%grid.shape[0], j] + grid[(i+1)%grid.shape[0], j] +
                     grid[(i-1)%grid.shape[0], (j-1)%grid.shape[1]] + grid[(i-1)%grid.shape[0], (j+1)%grid.shape[1]] +
                     grid[(i+1)%grid.shape[0], (j-1)%grid.shape[1]] + grid[(i+1)%grid.shape[0], (j+1)%grid.shape[1]])
            
            # Apply Conway's rules
            if grid[i, j] == 1:
                if total < 2 or total > 3:
                    new_grid[i, j] = 0
            else:
                if total == 3:
                    new_grid[i, j] = 1
    return new_grid

def animate(frame, img, grid):
    new_grid = update_grid(grid)
    img.set_data(new_grid)
    grid[:] = new_grid[:]
    return img,

def main():
    grid_size = 100
    grid = np.random.choice([0, 1], size=(grid_size, grid_size))
    
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest', cmap='gray')
    
    ani = animation.FuncAnimation(fig, animate, fargs=(img, grid), frames=10, interval=200, save_count=50)
    plt.show()

if __name__ == "__main__":
    main()
