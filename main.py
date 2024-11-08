'🔥', '🟩', '🟥', '🌊', '🌲', '❤️', '🏆', '🏬', '🚑', '🚁'

from map import Map
import time
import os

TICK_SLEEP = 0.03
TREE_UPDATE = 30
FIRE_UPDATE = 150
MAP_WIDTH, MAP_HEIGHT = 20, 10


m = Map(MAP_WIDTH, MAP_HEIGHT)
# m.print_map()
# m.generate_river(5)
m.generate_river(10)
m.generate_forest(2, 10)
# m.generate_river(10)
# m.add_free()

m.print_map()


tick = 1
while True:
    os.system("cls")
    print('TICK ', tick)
    m.print_map()
    tick += 1
    time.sleep(TICK_SLEEP)
    if tick % TREE_UPDATE == 0:
        m.generate_tree()
    if tick % FIRE_UPDATE == 0:
        m.update_fires()

