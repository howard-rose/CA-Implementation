from tkinter import *
from tkinter import ttk


class GUI(Tk):
    def __init__(self, rows, cols, size, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Game of Life")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.minsize(750, 0)

        main_frame = ttk.Frame(self, padding="3 3 12 12")
        main_frame.grid(column=0, row=0, sticky=(N, W, E, S))
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(0, weight=1)

        self.game_frame = GameFrame(rows, cols, size, main_frame, text="Board")
        self.control_frame = ControlFrame(main_frame, text="Controls")

        self.game_frame.grid(column=0, row=0, sticky=(N, W, E, S))
        self.control_frame.grid(column=1, row=0)

        #self.control_frame.reset_btn.configure(command=self.game_frame.refresh)


class GameFrame(ttk.LabelFrame):
    def __init__(self, rows, cols, size, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.rows = rows
        self.cols = cols
        self.size = size

        canvas_width = self.cols * self.size
        canvas_height = self.rows * self.size

        self.canvas = Canvas(self, borderwidth=0, highlightthickness=0,
                             width=canvas_width, height=canvas_height)
        self.canvas.grid(column=0, row=0, sticky=(N, W, E, S))

        self.cell_ids = [[None] * cols for r in range(self.rows)]
        for r in range(self.rows):
            for c in range(self.cols):
                x1, y1 = c * self.size, r * self.size
                x2, y2 = x1 + self.size, y1 + self.size
                self.cell_ids[r][c] = self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill="yellow", width="1")

    def itemconfigure(self, r, c, *args, **kwargs):
        self.canvas.itemconfigure(self.cell_ids[r][c], *args, **kwargs)


class ControlFrame(ttk.Labelframe):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # self.start_btn = ttk.Button(self, text="Start")
        # self.start_btn.grid(column=0, row=0)

        self.step_btn = ttk.Button(self, text="Step")
        self.step_btn.grid(column=0, row=1)

        self.reset_btn = ttk.Button(self, text="Reset")
        self.reset_btn.grid(column=0, row=2)

        self.clear_btn = ttk.Button(self, text="Clear")
        self.clear_btn.grid(column=0, row=3)


if __name__ == "__main__":
    root = GUI(30, 60, 24)
    root.mainloop()
