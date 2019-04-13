def ant(grid, column, row, n, direction=0):
    print("[init] grid : %s" % grid)
    print("[init] column : %s" % column)
    print("[init] row : %s" % row)
    print("[init] n : %s" % n)
    print("[init] direction : %s" % direction)
    for i in range(0, n):
        if (grid[row][column]) == 1:
            # WHITE
            grid[row][column] = 0
            direction = (direction + 1) % 4
            print("[white] direction : %s" % direction)
        else:
            # BLACK
            grid[row][column] = 1
            direction = abs((direction - 1) % 4)
            print("[black] direction : %s" % direction)
        column, row = forward(grid, column, row, direction)
        print(grid)
    return grid


def forward(grid, column, row, direction):
    if direction == 0:
        # NORTH
        if row == 0:
            # grid = [0] * len(grid[0]) + grid
            grid.insert(0, [0] * len(grid[0]))
        else:
            row -= 1
    if direction == 1:
        # EAST
        if column == len(grid[0]) - 1:
            for i in range(0, len(grid)):
                grid[i].append(0)
        column += 1
    if direction == 2:
        # SOUTH
        if row == len(grid) - 1:
            grid.append([0] * (len(grid[0])))
        row += 1
    if direction == 3:
        # WEST
        if column == 0:
            for i in range(0, len(grid)):
                # grid[i] = [0] + grid[i]
                grid[i].insert(0, 0)
        else:
            column -= 1
    return column, row


import unittest


class TestStringMethods(unittest.TestCase):
    def test_runner(self):
        self.assertEqual(ant([[1]], 0, 0, 1, 0), [[0, 0]])
        self.assertEqual(ant([[0]], 0, 0, 1, 0), [[0, 1]])
        self.assertEqual(ant([[1]], 0, 0, 3, 0), [[0, 1], [0, 1]])
        self.assertEqual(
            ant([[0, 0, 0], [0, 0, 0], [0, 0, 0]], 2, 2, 10, 1),
            [[0, 0, 0, 0], [0, 1, 1, 0], [0, 1, 1, 1], [0, 0, 0, 1]],
        )

        # [
        #     [0, 0, 1, 1, 0],
        #     [0, 0, 1, 0, 1],
        #     [1, 0, 0, 0, 0],
        #     [1, 1, 1, 1],
        #     [1, 1, 0, 0],
        # ]
        # [
        #     [0, 0, 1, 1, 0],
        #     [0, 0, 1, 0, 1],
        #     [1, 0, 0, 0, 0],
        #     [1, 1, 1, 0, 1],
        #     [0, 1, 1, 0, 0],
        # ]
        self.assertEqual(
            ant([[1, 0, 1], [0, 1, 0], [1, 0, 1]], 0, 0, 20, 0),
            [
                [0, 0, 1, 1, 0],
                [0, 0, 1, 0, 1],
                [1, 0, 0, 0, 0],
                [1, 1, 1, 0, 1],
                [0, 1, 1, 0, 0],
            ],
        )


if __name__ == "__main__":
    unittest.main()
