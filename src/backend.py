import random
from tkinter.constants import W

height = 100
width = 100


def randomize(height, width):
    result = [[random.randint(0, 1) for i in range(width)]
              for i in range(height)]
    return result


grid_model = [[0] * width for i in range(height)]


def next_gen():
    global grid_model
    height = len(grid_model)
    width = len(grid_model[0])

    next_gen_grid = [[0] * width for i in range(height)]

    for i in range(height):
        for j in range(width):
            cell = 0
            count = count_neighbors(grid_model, i, j)

            if grid_model[i][j] == 0:
                if count == 3:
                    cell = 1
            elif grid_model[i][j] == 1:
                if count == 2 or count == 3:
                    cell = 1

            next_gen_grid[i][j] = cell

    grid_model = next_gen_grid.copy()


def count_neighbors(grid, row, col):
    count = 0
    height = len(grid)
    width = len(grid[0])
    if row-1 >= 0:
        count += grid[row-1][col]

    if (row-1 >= 0) and (col-1 >= 0):
        count += grid[row-1][col-1]

    if (row-1 >= 0) and (col+1 < width):
        count += grid[row-1][col+1]

    if col-1 >= 0:
        count += grid[row][col-1]

    if col+1 < width:
        count += grid[row][col+1]

    if row+1 < height:
        count += grid[row+1][col]

    if (row+1 < height) and (col+1 < width):
        count += grid[row+1][col+1]

    if (row+1 < height) and (col-1 >= 0):
        count += grid[row+1][col-1]

    return count


if __name__ == "__main__":
    next_gen()
