from random import randint as rand

def randbool(cutoff: int, limiter: int) -> bool:  # cutoff - отсечка, limiter - ограничитель
    temp = rand(0, limiter)
    return temp <= cutoff


def randcell(width: int, height: int) -> tuple:
    temp_heig =rand(0, height - 1)
    temp_wid = rand(0, width - 1)
    return temp_heig, temp_wid


# (x, y) -> 0 - вверх(-1, 0), 1 - вправо(0, 1), 2 - вниз(1, 0), 3 - влево(0, -1)
def randneighbour(x: int, y: int) -> tuple:
    moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    temp = rand(0, 3)
    dx, dy = moves[temp][0], moves[temp][1]
    return x + dx, y + dy
