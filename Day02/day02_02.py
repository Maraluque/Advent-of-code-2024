if __name__ == '__main__':
    safe_records = 0

    with open("input.txt", "r") as f:
        lines = f.readlines()
        for level in lines:
            level_items = level.split()
            level_items = list(map(int,level_items))
            level_sorted = level_items.copy()
            level_sorted.sort()
            level_reversed = level_items.copy()
            level_reversed.sort(reverse=True)

            safety_flag = False
            if level_items in (level_sorted, level_reversed):
                for index in range(len(level_items)-1):
                    if abs(int(level_items[index+1]) - int(level_items[index])) in (1, 2, 3):
                        safety_flag = True
                    else:
                        safety_flag = False
                        break
            # Second check to ensure which are correct removing one level
            if not safety_flag:
                for i in range(len(level_items)):
                    temp_list = level_items.copy()
                    del temp_list[i]
                    temp_sorted = temp_list.copy()
                    temp_sorted.sort()
                    tem_reversed = temp_list.copy()
                    tem_reversed.sort(reverse=True)

                    if temp_list in (temp_sorted, tem_reversed):
                        safety_flag = False
                        for index in range(len(temp_list)-1):
                            if abs(int(temp_list[index+1]) - int(temp_list[index])) in (1, 2, 3):
                                safety_flag = True
                            else:
                                safety_flag = False
                                break
                        if safety_flag:
                            break
            if safety_flag:
                safe_records+=1
    print(safe_records)
