from utils import randbool
from utils import randcell
from utils import randneighbour


# CELL_TYPES ->
# 0 - поле
# 1 - дерево
# 2 - река
# 3 - госпиталь
# 4 - апгрейд - шоп
# 5 - огонь
# 6 - рамка карты


CELL_TYPES = "🟩🌲🌊🚑🏬🔥⬛"

class Map:

    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.cells = [[0 for i in range(width)] for j in range(height)]


    # def generate_tree(self):  # Генерация одного дерева, в одной клеточке.
    #     cell = randcell(self.width, self.height)
    #     cell_x, cell_y = cell[0], cell[1]
    #     if self.cells[cell_x][cell_y] != 1:
    #         self.cells[cell_x][cell_y] = 1    

    def generate_forest(self, cutoff: int, limiter: int) -> None:  # cutoff - отсечка
        for row in range(self.height):
            for column in range(self.width):
                if randbool(cutoff, limiter):  # import from utils.py
                    self.cells[row][column] = 1  # replacing value with 1 in main list


    def generate_river(self, length: int) -> None: # length - максимальная длина реки.
        h_axis, w_axis = randcell(self.height, self.width)  # -> tuple(num, num)
        self.cells[h_axis][w_axis] = 2
        while length > 0:
            rand_h, rand_w = randneighbour(h_axis, w_axis, self.height, self.width)
            if self.cells[rand_h][rand_w] != 2:
                self.cells[rand_h][rand_w] = 2
                h_axis, w_axis = rand_h, rand_w
                length -= 1


    def add_fire(self):
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
            self.add_fire()
            

    def print_map(self) -> None:
        print(CELL_TYPES[6] * (self.width + 2))
        for row in self.cells:
            print(CELL_TYPES[6], end="")
            for cell in row:
                if cell >= 0 and cell < len(CELL_TYPES):
                    print(CELL_TYPES[cell], end="")
            print(CELL_TYPES[6])
        print(CELL_TYPES[6] * (self.width + 2))    


    def check_bounds(self, x: int, y: int) -> bool:
        if 0 <= x < self.width and 0 <= y < self.height:
            return True
        return False

    
m = Map(20, 10)

# m.generate_tree()
# m.generate_forest(3, 10)
# m.add_fire()
m.generate_river(10)
# m.update_fires()



# m.generate_river(10)
m.print_map()

# print(m.check_bounds(19, 9))

# while True:
#     os.system('cls')
#     print('⬛' * (m.width + 2))
#     for row in m.cells:
#         print('⬛', end="")
#         for cell in row:
#             if cell >= 0 and cell < len(CELL_TYPES):
#                 # print('', end="")
#                 print(CELL_TYPES[cell], end="")
#         print('⬛')
#     print('⬛' * (m.width + 2))
    
#     time.sleep(0.05)
#     print()
