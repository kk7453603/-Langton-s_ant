import numpy as np
from PIL import Image

size = 1024

field = np.zeros((size, size), dtype=np.uint8)

x, y = size // 2, size // 2

# Начальное направление муравья (0 - вверх, 1 - вправо, 2 - вниз, 3 - влево)
direction = 0

while True:
    if field[x, y] == 0:
        direction = (direction + 1) % 4
    else:
        direction = (direction - 1) % 4

    field[x, y] = 255 - field[x, y]

    if direction == 0:
        x -= 1
    elif direction == 1:
        y += 1
    elif direction == 2:
        x += 1
    else:
        y -= 1

    if x < 0 or x >= size or y < 0 or y >= size:
        break

image = Image.fromarray(field, mode='L')

image.save('ant_path.png')

image.show()

num_black_cells = np.sum(field == 0)
print("Число черных клеток:", num_black_cells)
