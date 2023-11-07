# Implement a program that can solve Sudoku puzzles. You can input a Sudoku puzzle, and the program should find the solution.
from collections import Counter

grid = [[1, 0, 6, 9, 0, 0, 0, 0, 0],
        [0, 3, 0, 0, 5, 0, 0, 2, 8],
        [0, 0, 0, 0, 0, 0, 4, 0, 0],
        [8, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 2, 0, 0, 8, 0, 0, 1, 3],
        [0, 4, 0, 0, 0, 0, 5, 0, 0],
        [0, 0, 0, 0, 1, 0, 7, 0, 0],
        [0, 0, 3, 0, 0, 6, 0, 4, 1]]

possible_solutions_matrix_dict = {'0/0': {}, '0/3': {}, '0/6': {}, '3/0': {}, '3/3': {}, '3/6': {}, '6/0': {},
                                  '6/3': {}, '6/6': {}}
possible_solutions_vertical = {'0': {}, '1': {}, '2': {}, '3': {}, '4': {}, '5': {}, '6': {}, '7': {}, '8': {}}
possible_solutions_horizontal = {'0': {}, '1': {}, '2': {}, '3': {}, '4': {}, '5': {}, '6': {}, '7': {}, '8': {}}
remove_positions = {}
possibility_list = []


def solve(matrix):
    run = 1
    while True:
        previous_matrix = [row[:] for row in matrix]
        for row, a in enumerate(matrix):
            for column, b in enumerate(a):
                if b == 0:
                    possible_solution = list(range(1, 10))
                    # subtract entries in row from possible solution
                    for i in matrix[row]:
                        try:
                            possible_solution.remove(i)
                        except ValueError:
                            pass
                    # subtract entries in column from possible solution
                    column_list = [matrix[j][column] for j in range(9)]
                    for k in column_list:
                        try:
                            possible_solution.remove(k)
                        except ValueError:
                            pass
                    # subtract entries in 3by3 from possible solution
                    row_start_3by3 = (row // 3) * 3
                    column_start_3by3 = (column // 3) * 3
                    square_list = create_3by3(matrix, row_start_3by3, column_start_3by3)
                    for m in square_list:
                        try:
                            possible_solution.remove(m)
                        except ValueError:
                            pass

                    # if possible solution == 1 enter it into sudoku matrix
                    if len(possible_solution) == 1:
                        matrix[row][column] = possible_solution[0]

                    # create dict of dict with possibilities for each 3by3
                    temp_possible_solutions_3by3 = possible_solutions_matrix_dict[
                        str(row_start_3by3) + '/' + str(column_start_3by3)]
                    temp_possible_solutions_3by3.update({str(row) + ':' + str(column): possible_solution.copy()})
                    possible_solutions_matrix_dict.update(
                        {str(row_start_3by3) + '/' + str(column_start_3by3): temp_possible_solutions_3by3})
                    # create dict of dict with possibilities for each row
                    temp_possible_solutions_vertical = possible_solutions_vertical[str(column)]
                    temp_possible_solutions_vertical.update({str(row) + ':' + str(column): possible_solution.copy()})
                    possible_solutions_vertical.update({str(column): temp_possible_solutions_vertical})
                    # create dict of dict with possibilities for each column
                    temp_possible_solutions_horizontal = possible_solutions_horizontal[str(column)]
                    temp_possible_solutions_horizontal.update({str(row) + ':' + str(column): possible_solution.copy()})
                    possible_solutions_horizontal.update({str(column): temp_possible_solutions_horizontal})
                    # clear possible solution for this field
                    possible_solution.clear()

        for box in possible_solutions_matrix_dict:
            for position, possibility in possible_solutions_matrix_dict[box].items():
                # identify and clean len = 1 possibilities (valid solutions) from dict and clean the possibility from
                # other positions within the same 3by3 matrix
                if len(possibility) == 1:
                    remove_value = possibility[0]
                    remove_positions.update({box: position})
                    for value in possible_solutions_matrix_dict[box].values():
                        try:
                            value.remove(remove_value)
                        except ValueError:
                            pass

        for box in possible_solutions_matrix_dict:
            for to_remove_position in remove_positions.values():
                try:
                    possible_solutions_matrix_dict[box].pop(to_remove_position)
                except KeyError:
                    pass

        # check for non duplicates within a 3by3 and set
        non_duplicates(matrix, possible_solutions_matrix_dict)
        non_duplicates(matrix, possible_solutions_horizontal)
        non_duplicates(matrix, possible_solutions_vertical)

        print_grid(matrix, run)
        for g in possible_solutions_matrix_dict:
            print(g + ':' + str(possible_solutions_matrix_dict[g]))
        for g in possible_solutions_horizontal:
            print(g + ':' + str(possible_solutions_horizontal[g]))
        for g in possible_solutions_vertical:
            print(g + ':' + str(possible_solutions_vertical[g]))

        run += 1
        if matrix == previous_matrix:
            break


def create_3by3(matrix, i, j):
    square_3by3 = []
    for m in range(i, i + 3):
        for n in range(j, j + 3):
            square_3by3.append(matrix[m][n])
    return square_3by3


def non_duplicates(matrix, dictionary):
    # identify and clean len = 1 possibilities (valid solutions) from dict and clean the possibility from
    # other positions within the same dict of dict
    for box in dictionary:
        for position, possibility in dictionary[box].items():
            if len(possibility) == 1:
                remove_value = possibility[0]
                remove_positions.update({box: position})
                for value in dictionary[box].values():
                    try:
                        value.remove(remove_value)
                    except ValueError:
                        pass

    for box in dictionary:
        for position, possibility in dictionary[box].items():
            for poss in possibility:
                possibility_list.append(poss)
        count_possibilities = Counter(possibility_list)
        # Counter returns a dictionary ({possibility, count})
        for number, count in count_possibilities.items():
            if count == 1:
                for position, possibility in dictionary[box].items():
                    if number in possibility:
                        matrix[int(position[0])][int(position[2])] = number
                        remove_positions.update({box: position})
        possibility_list.clear()
        count_possibilities.clear()

    for box in dictionary:
        for to_remove_position in remove_positions.values():
            try:
                dictionary[box].pop(to_remove_position)
            except KeyError:
                pass


# print Sudoku and nth iteration
def print_grid(matrix, iteration):
    print('Sudoku ' + str(iteration))
    for i in matrix:
        print(i)


solve(grid)
