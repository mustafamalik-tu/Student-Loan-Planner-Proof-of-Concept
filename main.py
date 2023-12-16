import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def plot_graph():
    x_values = [1, 2, 3, 4, 5]
    y_values = [2, 4, 6, 8, 10]

    fig = Figure(figsize=(5, 4), dpi=100)

    plot = fig.add_subplot(1, 1, 1)

    plot.plot(x_values, y_values, label='Data')

    plot.set_xlabel('X-axis')
    plot.set_ylabel('Y-axis')
    plot.set_title('Matplotlib in Tkinter')

    plot.legend()

    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.grid(row=2, column=0, columnspan=3)

window = tk.Tk()
window.title("Matplotlib and Tkinter Example")

plot_button = ttk.Button(window, text="Plot Graph", command=plot_graph)
plot_button.grid(row=1, column=1)

window.mainloop()
