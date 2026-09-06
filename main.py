from puzzle import get_legal_moves, is_solvable
from astar import a_star
from heuristics import misplaced_tiles, manhattan_distance

def print_board(state):
    """Display a state as a 3×3 board."""
    for row in range(3):
        start = row * 3
        print(*state[start:start + 3])
    print()


def read_board(label):
    """Read a board containing each number from 0 to 8 exactly once."""
    while True:
        print(f"Enter {label} (use 0 for the blank):")
        board = []

        for row in range(3):
            while True:
                try:
                    values = [
                        int(value)
                        for value in input(f"Row {row + 1}: ").split()
                    ]
                except ValueError:
                    print("Enter integers only.")
                    continue

                if len(values) != 3:
                    print("Enter exactly 3 numbers.")
                    continue

                if any(value < 0 or value > 8 for value in values):
                    print("Numbers must be between 0 and 8.")
                    continue

                board.extend(values)
                break

        if sorted(board) == list(range(9)):
            return tuple(board)

        print("Use each number from 0 to 8 exactly once. Try again.\n")

def get_neighbors(state):
    """Give A* just the boards from each legal move."""
    return [board for direction, board in get_legal_moves(state)]

def main():
    initial_state = read_board("initial state")
    goal_state = read_board("goal state")

    print("\nInitial state:")
    print_board(initial_state)

    print("Goal state:")
    print_board(goal_state)

    if not is_solvable(initial_state, goal_state):
        print("No solution: the initial state cannot reach this goal.")
        return

    print("This puzzle is solvable.\n")

    for name, heuristic in (
        ("Misplaced Tiles", misplaced_tiles),
        ("Manhattan Distance", manhattan_distance),
    ):
        print(f"\nA* using {name}")
        result = a_star(
            initial_state,
            goal_state,
            heuristic,
            get_neighbors
        )

        if result is None:
            print("No solution found.")
            continue

        for step, board in enumerate(result["path"]):
            print(f"Step {step}:")
            print_board(board)

        print("Solution moves:", result["cost"])
        print("Nodes generated:", result["nodes_generated"])
        print("Nodes expanded:", result["nodes_expanded"])

if __name__ == "__main__":
    main()