from random import randrange
import enum

NUM_COLS = 12
NUM_ROWS = 19

NUM_WORDS = 5


class Direction(enum.Enum):
    N = 1
    NE = 2
    E = 3
    SE = 4
    S = 5
    SW = 6
    W = 7
    NW = 8


def printGrid(cells):
    # print out grid
    for row in cells:
        for char in row:
            print(char, end=" ")
        print()  # new line


def printBorder():
    equal_str = "="
    print(equal_str * (NUM_COLS * 2 + 2))


def printSearch():
    cells = []

    # Populate / Create 2d array with random values
    # note: equal weighting for different values, no cumulative probability distribution
    for row in range(NUM_ROWS):
        templist = []
        for char in range(NUM_COLS):
            char = '#'
            templist.append(char)
        cells.append(templist)

    # CURRENTLY, GATHERS WORDS FROM USER, could be set to pull from a source
    words = []
    printBorder()
    print("Enter {} words below".format(NUM_WORDS))
    printBorder()

    for i in range(NUM_WORDS):
        words.append(input("Enter word:").upper())
        if len(words[i]) > max(NUM_ROWS, NUM_COLS):
            print("Word too long, start over, FAIL")
            exit(2)

    for word in words:
        placed = False
        while not placed:
            rand_row = randrange(NUM_ROWS)
            rand_col = randrange(NUM_COLS)
            length = len(word)
            random_direction = Direction(randrange(7) + 1)

            step_x = 0
            step_y = 0
            if random_direction == Direction.N:
                step_x = 0
                step_y = -1
            elif random_direction == Direction.NE:
                step_x = 1
                step_y = -1
            elif random_direction == Direction.E:
                step_x = 1
                step_y = 0
            elif random_direction == Direction.SE:
                step_x = 1
                step_y = 1
            elif random_direction == Direction.S:
                step_x = 0
                step_y = 1
            elif random_direction == Direction.SW:
                step_x = -1
                step_y = 1
            elif random_direction == Direction.W:
                step_x = -1
                step_y = 0
            elif random_direction == Direction.NW:
                step_x = -1
                step_y = -1

            end_x = rand_col + length * step_x
            end_y = rand_row + length * step_y

            if end_x < 0 or end_x >= NUM_COLS: continue
            if end_y < 0 or end_y >= NUM_ROWS: continue

            # check to see if we can place word, if not break out and pick new position
            failed = False
            for i in range(length):
                new_x = rand_col + i * step_x
                new_y = rand_row + i * step_y

                char_at_pos = cells[new_y][new_x]
                if char_at_pos != '#':
                    failed = True
                    break

            if failed:
                continue
            # place word and mark placed so next word can be placed
            for i in range(length):
                new_x = rand_col + i * step_x
                new_y = rand_row + i * step_y
                cells[new_y][new_x] = word[i]
            placed = True

    # print out grid (solution)
    printBorder()
    printGrid(cells)
    printBorder()

    # Fill other stuff with random letters
    for row in range(NUM_ROWS):
        for char in range(NUM_COLS):
            if cells[row][char] == '#':
                cells[row][char] = chr(randrange(26) + 65)

    # print out populated word search
    printGrid(cells)


printSearch()
