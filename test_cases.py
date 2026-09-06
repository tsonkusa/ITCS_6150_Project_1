"""Run the three supplied sample puzzles with both A* heuristics."""

from astar import a_star
from heuristics import misplaced_tiles, manhattan_distance
from main import get_neighbors, print_board
from puzzle import is_solvable


CASES = [
    (
        (1, 2, 3, 7, 4, 5, 6, 8, 0),
        (1, 2, 3, 8, 6, 4, 7, 5, 0),
    ),
    (
        (2, 8, 1, 3, 4, 6, 7, 5, 0),
        (3, 2, 1, 8, 0, 4, 7, 5, 6),
    ),
    (
        (7, 2, 4, 5, 0, 6, 8, 3, 1),
        (1, 2, 3, 4, 5, 6, 7, 8, 0),
    ),

    # Case 4: Already at the goal
    (
        (1, 2, 3, 4, 5, 6, 7, 8, 0),
        (1, 2, 3, 4, 5, 6, 7, 8, 0),
    ),

    # Case 5: One move from the goal
    (
        (1, 2, 3, 4, 5, 6, 7, 0, 8),
        (1, 2, 3, 4, 5, 6, 7, 8, 0),
    ),

    # Case 6: Two moves from the goal
    (
        (1, 2, 3, 4, 5, 6, 0, 7, 8),
        (1, 2, 3, 4, 5, 6, 7, 8, 0),
    ),

    # Case 7: Four moves from the goal
    (
        (1, 2, 3, 5, 0, 6, 4, 7, 8),
        (1, 2, 3, 4, 5, 6, 7, 8, 0),
    ),

    # Case 8: Nonstandard goal with the blank in the center
    (
        (1, 2, 3, 4, 5, 6, 7, 8, 0),
        (1, 2, 3, 4, 0, 5, 7, 8, 6),
    ),
]


def main():
    summary = []

    for case_number, (initial, goal) in enumerate(CASES, start=1):
        print(f"\n========== Case {case_number} ==========")
        print("Initial:")
        print_board(initial)
        print("Goal:")
        print_board(goal)

        for name, heuristic in (
            ("Misplaced Tiles", misplaced_tiles),
            ("Manhattan Distance", manhattan_distance),
        ):
            print(f"\n{name}")
            if not is_solvable(initial, goal):
                print("No solution: inversion parity does not match.")
                summary.append((case_number, name, "Unsolvable", "N/A", "N/A"))
                continue

            result = a_star(initial, goal, heuristic, get_neighbors)
            if result is None:
                print("No solution found.")
                summary.append((case_number, name, "No solution", "N/A", "N/A"))
                continue

            path = result["path"]
            assert path[0] == initial and path[-1] == goal
            assert len(path) - 1 == result["cost"]
            for current, following in zip(path, path[1:]):
                assert following in get_neighbors(current), "Illegal solution move"

            for step, board in enumerate(path):
                print(f"Step {step}:")
                print_board(board)

            summary.append((
                case_number,
                name,
                result["cost"],
                result["nodes_generated"],
                result["nodes_expanded"],
            ))

    print("\nRESULTS SUMMARY")
    print("Case | Heuristic | Moves | Generated | Expanded")
    for row in summary:
        print(" | ".join(str(value) for value in row))
    print("\nGenerated counts the initial state and each priority-queue insertion.")
    print("Expanded counts states whose successors are examined; excludes the goal.")


if __name__ == "__main__":
    main()
