import copy
def has_any_loop(guard_map, guard_position): #NOSONAR #no-qa
    actual_char = guard_map[guard_position[0]][guard_position[1]]
    dir_char = None
    for d in ("^", ">", "v", "<"):
        if d in actual_char:
            dir_char = d
            break
    if dir_char is None:
        return False # To avoid false positives

    turn_right = {"^": ">", ">": "v", "v": "<", "<": "^"}

    r, c = guard_position
    direction = dir_char
    seen_states = set()

    # To avoid checking too many times if there's a loop
    step_limit = MAP_LIMIT * MAP_LIMIT * 4

    steps = 0
    while True:
        steps += 1
        if steps > step_limit:
            return True

        state = (r, c, direction)
        if state in seen_states:
            return True
        seen_states.add(state)

        # Move the guard
        if direction == "^":
            nr, nc = r - 1, c
        elif direction == ">":
            nr, nc = r, c + 1
        elif direction == "v":
            nr, nc = r + 1, c
        else:
            nr, nc = r, c - 1

        if nr < 0 or nr >= MAP_LIMIT or nc < 0 or nc >= MAP_LIMIT:
            return False

        if guard_map[nr][nc] == "#":
            direction = turn_right[direction]
            continue

        r, c = nr, nc


if __name__ == '__main__':
    positions_visited = []
    number_of_loops_by_obstructions = 0
    guard_map = []

    with open("input.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            guard_map.append(list(line.strip()))
        MAP_LIMIT = len(guard_map)

        # Retrieve guard position
        guard_initial_position = None
        for i in range(MAP_LIMIT):
            if not guard_initial_position:
                for j in range(MAP_LIMIT):
                    if "^" in guard_map[i][j]:
                        guard_initial_position = (i,j)
                        break
            else:
                break

        # Obtain the number of loops made by obstructions
        guard_position = guard_initial_position
        for i in range(MAP_LIMIT):
            for j in range(MAP_LIMIT):
                guard_copy_map = copy.deepcopy(guard_map)
                if guard_copy_map[i][j] == ".":
                    guard_copy_map[i][j] = "#"
                    if has_any_loop(guard_copy_map,guard_position):
                        number_of_loops_by_obstructions+=1

    print(number_of_loops_by_obstructions)
