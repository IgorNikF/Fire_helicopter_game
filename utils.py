from random import randint as rand

def randbool(cutoff: int, limiter: int) -> bool:  # cutoff - отсечка, limiter - ограничитель
    temp = rand(0, limiter)
    return temp <= cutoff


def randcell(height: int, width: int) -> tuple:
    ran_heig =rand(0, height - 1)
    ran_wid = rand(0, width - 1)
    return ran_heig, ran_wid


# (x, y) -> 0 - вверх(-1, 0), 1 - вправо(0, 1), 2 - вниз(1, 0), 3 - влево(0, -1)
def randneighbour(heig: int, wid: int, height: int, width: int) -> tuple:
    moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    while True:
        temp = rand(0, 3)
        d_heig, d_wid = moves[temp][0], moves[temp][1]
        rand_heig, rand_wid = heig + d_heig, wid + d_wid
        if 0 <= rand_heig < height and 0 <= rand_wid < width:
            return rand_heig, rand_wid

