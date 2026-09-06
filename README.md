# Programming Project 1: 8-Puzzle Using A*

This Python program solves the 8-puzzle using A* search with two heuristics:
- Misplaced Tiles
- Manhattan Distance

## Requirements

Python 3. No additional packages are required.

## Files

- `main.py`: User input, validation, board display, and running both heuristics.
- `puzzle.py`: Legal moves and solvability checking.
- `astar.py`: A* search, solution-path reconstruction, and node counters.
- `heuristics.py`: Misplaced Tiles and Manhattan Distance.
- `test_cases.py`: Runs eight cases with both heuristics.
- `all_results.txt`: Saved solution paths and results for all eight cases.

## Run an Interactive Puzzle

From the project folder, run:

```bash
python3 main.py
```

Enter the initial and goal boards, three numbers per row separated by spaces.
Use `0` for the blank. Each board must contain every number from `0` to `8`
exactly once.

Example initial board:

```text
1 2 3
4 5 6
7 0 8
```

Example goal board:

```text
1 2 3
4 5 6
7 8 0
```

The program checks solvability, then prints the solution path, move count,
nodes generated, and nodes expanded for each heuristic.

## Run All Eight Cases

```bash
python3 test_cases.py
```

To display and save the output on macOS/Linux:

```bash
python3 test_cases.py | tee all_results.txt
```

Cases 1–3 are the supplied assignment samples.
Cases 4–8 are student-created cases.

## Search Details

Each move costs 1. A* prioritizes states using `f(n) = g(n) + h(n)`,
where `g(n)` is the number of moves taken so far.

Both heuristics exclude the blank:
- Misplaced Tiles counts numbered tiles outside their goal positions.
- Manhattan Distance sums each numbered tile's row and column distances
  from its goal position.

Generated nodes count the initial state and each priority-queue insertion.
Expanded nodes count states whose successors are examined, excluding the goal.

For a 3×3 board, solvability requires matching inversion parity between
the initial and goal states.