import tkinter as tk
from tkinter import colorchooser

class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Amazing Drawing App")
        
        self.color = 'black'
        self.brush_size = 5

        self.canvas = tk.Canvas(self.root, bg='white', width=800, height=600)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(fill=tk.X, side=tk.BOTTOM)

        self.color_button = tk.Button(self.button_frame, text='Select Color', command=self.choose_color)
        self.color_button.pack(side=tk.LEFT)

        self.clear_button = tk.Button(self.button_frame, text='Clear', command=self.clear_canvas)
        self.clear_button.pack(side=tk.LEFT)

        self.size_label = tk.Label(self.button_frame, text='Brush Size:')
        self.size_label.pack(side=tk.LEFT)

        self.size_scale = tk.Scale(self.button_frame, from_=1, to=10, orient=tk.HORIZONTAL, command=self.change_brush_size)
        self.size_scale.set(self.brush_size)
        self.size_scale.pack(side=tk.LEFT)

        self.canvas.bind('<B1-Motion>', self.paint)
        self.canvas.bind('<ButtonRelease-1>', self.reset)

        self.last_x, self.last_y = None, None

    def choose_color(self):
        self.color = colorchooser.askcolor()[1]

    def clear_canvas(self):
        self.canvas.delete('all')

    def change_brush_size(self, value):
        self.brush_size = int(value)

    def paint(self, event):
        if self.last_x and self.last_y:
            self.canvas.create_line(self.last_x, self.last_y, event.x, event.y,
                                    width=self.brush_size, fill=self.color,
                                    capstyle=tk.ROUND, smooth=tk.TRUE)
        self.last_x, self.last_y = event.x, event.y

    def reset(self, event):
        self.last_x, self.last_y = None, None

if __name__ == '__main__':
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()
