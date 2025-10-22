if __name__ == '__main__':
    distinct_positions_visited = 0
    positions_visited = []
    map = []

    with open("input.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            map.append(list(line.strip()))
        map_limit = len(map)

        # Retrieve guard position
        guard_initial_position = None
        for i in range(map_limit):
            if not guard_initial_position:
                for j in range(map_limit):
                    if "^" in map[i][j]:
                        guard_initial_position = (i,j)
                        break
            else:
                break

        guard_position = guard_initial_position

        # Make the guard movements along the matrix
        on_limits = True
        while on_limits:
            if map[guard_position[0]][guard_position[1]] == "^": # Facing up
                new_row = guard_position[0]-1
                new_column = guard_position[1]
                if new_row < 0:
                    distinct_positions_visited += 1
                    map[guard_position[0]][guard_position[1]] = "X" # Mark as visited
                    on_limits = False
                else:
                    if map[new_row][new_column] == "#": # Obstacle found
                        map[guard_position[0]][guard_position[1]] = ">"
                        new_row = guard_position[0]
                        new_column = guard_position[1]
                    else: # Move guard
                        if map[new_row][new_column] == ".":
                            distinct_positions_visited += 1
                            map[guard_position[0]][guard_position[1]] = "X" # Mark as visited
                            map[new_row][new_column] = "^"
                        elif map[new_row][new_column] == "X":
                            map[guard_position[0]][guard_position[1]] = "X" # Mark as visited
                            map[new_row][new_column] = "^"
            elif map[guard_position[0]][guard_position[1]] == ">": # Facing right
                new_row = guard_position[0]
                new_column = guard_position[1]+1
                if new_column >= map_limit:
                    distinct_positions_visited += 1
                    map[guard_position[0]][guard_position[1]] = "X" # Mark as visited
                    on_limits = False
                else:
                    if map[new_row][new_column] == "#": # Obstacle found
                        map[guard_position[0]][guard_position[1]] = "v"
                        new_row = guard_position[0]
                        new_column = guard_position[1]
                    else: # Move guard
                        if map[new_row][new_column] == ".":
                            distinct_positions_visited += 1
                            map[guard_position[0]][guard_position[1]] = "X" # Mark as visited
                            map[new_row][new_column] = ">"
                        elif map[new_row][new_column] == "X":
                            map[guard_position[0]][guard_position[1]] = "X" # Mark as visited
                            map[new_row][new_column] = ">"
            elif map[guard_position[0]][guard_position[1]] == "<": # Facing left
                new_row = guard_position[0]
                new_column = guard_position[1]-1
                if new_column < 0:
                    distinct_positions_visited += 1
                    map[guard_position[0]][guard_position[1]] = "X" # Mark as visited
                    on_limits = False
                else:
                    if map[new_row][new_column] == "#": # Obstacle found
                        map[guard_position[0]][guard_position[1]] = "^"
                        new_row = guard_position[0]
                        new_column = guard_position[1]
                    else: # Move guard
                        if map[new_row][new_column] == ".":
                            distinct_positions_visited += 1
                            map[guard_position[0]][guard_position[1]] = "X" # Mark as visited
                            map[new_row][new_column] = "<"
                        elif map[new_row][new_column] == "X":
                            map[guard_position[0]][guard_position[1]] = "X" # Mark as visited
                            map[new_row][new_column] = "<"
            elif map[guard_position[0]][guard_position[1]] == "v": # Facing down
                new_row = guard_position[0]+1
                new_column = guard_position[1]
                if new_row >= map_limit:
                    distinct_positions_visited += 1
                    map[guard_position[0]][guard_position[1]] = "X" # Mark as visited
                    on_limits = False
                else:
                    if map[new_row][new_column] == "#": # Obstacle found
                        map[guard_position[0]][guard_position[1]] = "<"
                        new_row = guard_position[0]
                        new_column = guard_position[1]
                    else: # Move guard
                        if map[new_row][new_column] == ".":
                            distinct_positions_visited += 1
                            map[guard_position[0]][guard_position[1]] = "X" # Mark as visited
                            map[new_row][new_column] = "v"
                        elif map[new_row][new_column] == "X":
                            map[guard_position[0]][guard_position[1]] = "X" # Mark as visited
                            map[new_row][new_column] = "v"
            guard_position = (new_row,new_column)

    # Count how many X are in the visited guard_map
    print(distinct_positions_visited)
