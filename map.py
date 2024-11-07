from utils import randbool, randcell, randneighbour

# CELL_TYPES ->
# 0 - поле
# 1 - дерево
# 2 - река
# 3 - госпиталь
# 4 - апгрейд - шоп
# 5 - огонь


CELL_TYPES = "🟩🌲🌊🚑🏬🔥"

class Map:

    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.cells = [[0 for i in range(width)] for j in range(height)]


    def generate_forest(self, cutoff: int, limiter: int) -> None:  # cutoff - отсечка
        for row in range(self.height):
            for column in range(self.width):
                if randbool(cutoff, limiter):  # import from utils.py
                    self.cells[row][column] = 1

    def generate_tree(self):
        cell = randcell(self.width, self.height)
        cell_x, cell_y = cell[0], cell[1]
        if self.check_bounds(cell_x, cell_y) and self.cells[cell_x][cell_y] == 0:
            self.cells[cell_x][cell_y] = 1


    def generate_river(self, length: int) -> None: # length - максимальная длина реки
        x_axis, y_axis = randcell(self.width, self.height)  # -> tuple
        if self.check_bounds(x_axis, y_axis):
            self.cells[x_axis][y_axis] = 2
        while length > 0:
            gencell_neig = randneighbour(x_axis, y_axis)
            rand_x, rand_y = gencell_neig[0], gencell_neig[1]
            if self.check_bounds(rand_x, rand_y) and self.cells[rand_x][rand_y] != 2:
                self.cells[rand_x][rand_y] = 2
                x_axis, y_axis = rand_x, rand_y
                length -= 1
            else:
                continue


    def add_free(self):
        cell = randcell(self.width, self.height)
        cell_x, cell_y = cell[0], cell[1]
        if self.cells[cell_x][cell_y] == 1:
            self.cells[cell_x][cell_y] = 5

    def update_fires(self):
        for row in range(self.height):
            for column in range(self.width):
                cell = self.cells[row][column]
                if cell == 5:
                    self.cells[row][column] = 0
        for _ in range(2):
            self.add_free()
            

    def print_map(self) -> None:
        print('⬛' * (self.width + 2))
        for row in self.cells:
            print('⬛', end="")
            for cell in row:
                if cell >= 0 and cell < len(CELL_TYPES):
                    print(CELL_TYPES[cell], end="")
            print('⬛')
        print('⬛' * (self.width + 2))    


    def check_bounds(self, x: int, y: int) -> bool:
        if (x < 0 or y < 0 or x >= self.width or y >= self.height):
            return False
        return True 

    
# m = Map(20, 10)
# print(m.check_bounds(19, 9))
