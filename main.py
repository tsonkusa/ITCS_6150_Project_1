from puzzle import get_legal_moves


# Each tuple represents a 3×3 board.
# 0 represents the blank space.
initial_state = (
    1, 2, 3,
    7, 4, 5,
    6, 8, 0
)

goal_state = (
    1, 2, 3,
    8, 6, 4,
    7, 5, 0
)


def print_board(state):
    for row in range(3):
        start = row * 3
        print(*state[start:start + 3])
    print()


print("Initial state:")
print_board(initial_state)

print("Goal state:")
print_board(goal_state)

print("Legal moves from the initial state:")
for direction, next_state in get_legal_moves(initial_state):
    print(direction)
    print_board(next_state)
