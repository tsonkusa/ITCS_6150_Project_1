def get_legal_moves(state):
    """Return (direction, new_state) pairs for legal moves of the blank."""
    blank = state.index(0)
    row, col = divmod(blank, 3)
    moves = []

    for direction, dr, dc in (
        ("UP", -1, 0),
        ("DOWN", 1, 0),
        ("LEFT", 0, -1),
        ("RIGHT", 0, 1),
    ):
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            target = new_row * 3 + new_col
            new_state = list(state)
            new_state[blank], new_state[target] = new_state[target], new_state[blank]
            moves.append((direction, tuple(new_state)))

    return moves

def count_inversions(state):
    """Count out-of-order tile pairs, ignoring the blank."""
    tiles = [tile for tile in state if tile != 0]
    inversions = 0

    for i in range(len(tiles)):
        for j in range(i + 1, len(tiles)):
            if tiles[i] > tiles[j]:
                inversions += 1

    return inversions


def is_solvable(initial, goal):
    """For a 3×3 puzzle, both boards must have matching inversion parity."""
    return count_inversions(initial) % 2 == count_inversions(goal) % 2