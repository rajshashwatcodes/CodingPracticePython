import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
g = 9.81  # Acceleration due to gravity (m/s^2)
l1 = 1.0  # Length of the first pendulum (m)
l2 = 1.0  # Length of the second pendulum (m)
m1 = 1.0  # Mass of the first pendulum (kg)
m2 = 1.0  # Mass of the second pendulum (kg)

# Initial conditions
theta1 = np.pi / 2  # Initial angle for the first pendulum (radians)
theta2 = np.pi / 4  # Initial angle for the second pendulum (radians)
omega1 = 0.0  # Initial angular velocity for the first pendulum (rad/s)
omega2 = 0.0  # Initial angular velocity for the second pendulum (rad/s)

# Time parameters
dt = 0.05  # Time step (s)
t_max = 20.0  # Maximum time (s)

# Function to calculate the derivatives
def derivatives(state, t):
    theta1, omega1, theta2, omega2 = state
    delta_theta = theta2 - theta1
    
    denominator1 = (m1 + m2) * l1 - m2 * l1 * np.cos(delta_theta) * np.cos(delta_theta)
    denominator2 = (l2 / l1) * denominator1

    dtheta1_dt = omega1
    domega1_dt = (m2 * l1 * omega1 * omega1 * np.sin(delta_theta) * np.cos(delta_theta) +
                  m2 * g * np.sin(theta2) * np.cos(delta_theta) +
                  m2 * l2 * omega2 * omega2 * np.sin(delta_theta) -
                  (m1 + m2) * g * np.sin(theta1)) / denominator1

    dtheta2_dt = omega2
    domega2_dt = (-m2 * l2 * omega2 * omega2 * np.sin(delta_theta) * np.cos(delta_theta) +
                  (m1 + m2) * g * np.sin(theta1) * np.cos(delta_theta) -
                  (m1 + m2) * l1 * omega1 * omega1 * np.sin(delta_theta) -
                  (m1 + m2) * g * np.sin(theta2)) / denominator2
    
    return dtheta1_dt, domega1_dt, dtheta2_dt, domega2_dt

# Initial state
state = np.array([theta1, omega1, theta2, omega2])

# Time array
t = np.arange(0, t_max, dt)

# Arrays to store the positions of the pendulums
x1_data, y1_data = [], []
x2_data, y2_data = [], []

# Solve the differential equations
for ti in t:
    dstate_dt = derivatives(state, ti)
    state += np.array(dstate_dt) * dt
    x1 = l1 * np.sin(state[0])
    y1 = -l1 * np.cos(state[0])
    x2 = x1 + l2 * np.sin(state[2])
    y2 = y1 - l2 * np.cos(state[2])
    x1_data.append(x1)
    y1_data.append(y1)
    x2_data.append(x2)
    y2_data.append(y2)

# Create the animation
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
line, = ax.plot([], [], 'o-', lw=2)

def init():
    line.set_data([], [])
    return line,

def update(frame):
    line.set_data([0, x1_data[frame], x2_data[frame]], [0, y1_data[frame], y2_data[frame]])
    return line,

ani = FuncAnimation(fig, update, frames=len(t), init_func=init, blit=True, interval=dt*1000)
plt.show()
