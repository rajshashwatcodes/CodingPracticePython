import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Constants for the Lorenz system
sigma = 10.0
beta = 8.0 / 3.0
rho = 28.0

# Time parameters
dt = 0.01
num_steps = 10000

# Function to compute the Lorenz system
def lorenz(x, y, z, sigma=sigma, beta=beta, rho=rho):
    dx_dt = sigma * (y - x)
    dy_dt = x * (rho - z) - y
    dz_dt = x * y - beta * z
    return dx_dt, dy_dt, dz_dt

# Initial conditions
x = np.zeros(num_steps)
y = np.zeros(num_steps)
z = np.zeros(num_steps)

# Starting point
x[0], y[0], z[0] = 0.0, 1.0, 1.05

# Solving the Lorenz system using the Euler method
for i in range(1, num_steps):
    dx_dt, dy_dt, dz_dt = lorenz(x[i-1], y[i-1], z[i-1])
    x[i] = x[i-1] + dx_dt * dt
    y[i] = y[i-1] + dy_dt * dt
    z[i] = z[i-1] + dz_dt * dt

# Plotting the Lorenz Attractor
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot(x, y, z, lw=0.5)
ax.set_title("Lorenz Attractor")
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")

plt.show()
