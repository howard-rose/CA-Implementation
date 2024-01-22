from cellular_automata import GameOfLife
from gui import GUI


class Controller:
    def __init__(self):
        self.rows, self.cols = 30, 60
        self.size = 24

        self.gui = GUI(self.rows, self.cols, self.size)
        self.ca = GameOfLife(self.rows, self.cols)

        # Button callbacks
        self.gui.control_frame.reset_btn.configure(command=self.reset)
        self.gui.control_frame.step_btn.configure(command=self.step)
        self.gui.control_frame.clear_btn.configure(command=self.clear)

        # Canvas rectangle callbacks
        for r in range(self.rows):
            for c in range(self.cols):
                callback = lambda event, y=r, x=c: self.clicked_cell(y, x)
                self.gui.game_frame.canvas.tag_bind(self.gui.game_frame.cell_ids[r][c], "<Button-1>", callback)

        self.reset()

    def clear(self):
        for r in range(self.rows):
            for c in range(self.cols):
                self.ca.cells[r][c].alive = False
        self.refresh()

    def clicked_cell(self, r, c):
        self.ca.cells[r][c].alive = not self.ca.cells[r][c].alive
        self.refresh()

    def step(self):
        self.ca.step()
        self.refresh()

    def reset(self):
        self.clear()
        self.initialize_default()
        self.refresh()

    def initialize_default(self):
        default_pattern = [
            [False, True, False],
            [False, False, True],
            [True, True, True]
        ]
        default_r, default_c = self.rows // 2, self.cols // 2

        for r in range(default_r, default_r + len(default_pattern)):
            for c in range(default_c, default_c + len(default_pattern[0])):
                self.ca.cells[r][c].alive = default_pattern[r - default_r][c - default_c]

    def refresh(self):
        for r in range(self.rows):
            for c in range(self.cols):
                fill = "yellow" if self.ca.cells[r][c].alive else "grey"
                self.gui.game_frame.itemconfigure(r, c, fill=fill)


if __name__ == "__main__":
    controller = Controller()
    controller.gui.mainloop()