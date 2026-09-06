import heapq


def make_path(parent, goal):
    path = []
    current = goal

    while current is not None:
        path.append(current)
        current = parent[current]

    path.reverse()
    return path


def a_star(initial, goal, heuristic, get_neighbors):
    # The priority queue stores:
    # (f value, tie breaker, g value, state)
    open_list = []

    counter = 0
    starting_g = 0
    starting_h = heuristic(initial, goal)
    starting_f = starting_g + starting_h

    heapq.heappush(
        open_list,
        (starting_f, counter, starting_g, initial)
    )

    g_cost = {initial: 0}

    parent = {initial: None}

    nodes_generated = 1
    nodes_expanded = 0

    while open_list:
        f, _, current_g, current_state = heapq.heappop(open_list)

        if current_g != g_cost[current_state]:
            continue

        if current_state == goal:
            solution_path = make_path(parent, goal)

            return {
                "path": solution_path,
                "cost": current_g,
                "nodes_generated": nodes_generated,
                "nodes_expanded": nodes_expanded
            }

        nodes_expanded += 1

        for neighbor in get_neighbors(current_state):
            if (
                isinstance(neighbor, tuple)
                and len(neighbor) == 2
                and isinstance(neighbor[1], str)
            ):
                neighbor = neighbor[0]

            new_g = current_g + 1

            if neighbor not in g_cost or new_g < g_cost[neighbor]:
                g_cost[neighbor] = new_g
                parent[neighbor] = current_state

                h = heuristic(neighbor, goal)
                new_f = new_g + h

                counter += 1

                heapq.heappush(
                    open_list,
                    (new_f, counter, new_g, neighbor)
                )

                nodes_generated += 1

    return None