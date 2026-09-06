def misplaced_tiles(state, goal):
    count = 0

    for i in range(9):
        if state[i] != 0 and state[i] != goal[i]:
            count += 1

    return count


def manhattan_distance(state, goal):
    distance = 0

    for tile in range(1, 9):
        current = state.index(tile)
        target = goal.index(tile)

        current_row = current // 3
        current_column = current % 3

        target_row = target // 3
        target_column = target % 3

        distance += abs(current_row - target_row)
        distance += abs(current_column - target_column)

    return distance