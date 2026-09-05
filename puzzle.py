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
