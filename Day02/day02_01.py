if __name__ == '__main__':
    safe_records = 0

    with open("input.txt", "r") as f:
        lines = f.readlines()
        # 1. Check if the levels are decreasing or increasing
        for level in lines:
            level_items = level.split()
            level_items = list(map(int,level_items))
            level_sorted = level_items.copy()
            level_sorted.sort()
            level_reversed = level_items.copy()
            level_reversed.sort(reverse=True)

            if level_items in (level_sorted, level_reversed):
                safety_flag = False
                # 2. Ensure that the increase/decrease is only by 1, 2 or 3
                for index in range(len(level_items)-1):
                    if abs(int(level_items[index+1]) - int(level_items[index])) in (1, 2, 3):
                        safety_flag = True
                    else:
                        safety_flag = False
                        break
                if safety_flag:
                    safe_records+=1
    print(safe_records)