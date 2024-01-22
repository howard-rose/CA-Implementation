class Cell:
    def __init__(self, alive=False):
        self.alive = alive

    def step(self, neighbors):
        alive_neighbors_count = len([n for n in neighbors if n.alive])

        if self.alive:
            if alive_neighbors_count < 2:
                # Underpopulation
                self.alive = False
            elif 2 <= alive_neighbors_count <= 3:
                # Survival
                self.alive = True
            else:
                # Overpopulation
                self.alive = False
        else:
            if alive_neighbors_count == 3:
                # Reproduction
                self.alive = True