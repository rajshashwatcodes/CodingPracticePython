import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1
    return n

def mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    n3 = np.empty((width, height))
    for i in range(width):
        for j in range(height):
            n3[i, j] = mandelbrot(r1[i] + 1j*r2[j], max_iter)
    return (r1, r2, n3)

def display(xmin, xmax, ymin, ymax, width=10, height=10, max_iter=256):
    dpi = 80
    img_width = dpi * width
    img_height = dpi * height

    x, y, z = mandelbrot_set(xmin, xmax, ymin, ymax, img_width, img_height, max_iter)
    
    fig, ax = plt.subplots(figsize=(width, height), dpi=dpi)
    ticks = np.arange(0, img_width, 3*dpi)
    x_ticks = xmin + (xmax - xmin) * ticks / img_width
    ax.set_xticks(ticks)
    ax.set_xticklabels(x_ticks)

    ticks = np.arange(0, img_height, 3*dpi)
    y_ticks = ymin + (ymax - ymin) * ticks / img_height
    ax.set_yticks(ticks)
    ax.set_yticklabels(y_ticks)

    ax.imshow(z.T, origin='lower', cmap='hot', extent=[xmin, xmax, ymin, ymax])
    plt.show()

# Set the parameters for the Mandelbrot set
xmin, xmax, ymin, ymax = -2.0, 1.0, -1.5, 1.5
display(xmin, xmax, ymin, ymax)
