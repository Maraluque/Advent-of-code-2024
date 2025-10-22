if __name__ == '__main__':
    middle_numbers_addition = 0

    with open("input.txt", "r") as f:
        lines = f.readlines()
        page_ordering_rules = []
        page_numbers_to_update = []
        ordering_rules_by_number = {}
        for line in lines:
            if "|" in line:
                line = line.strip()
                numbers = list(line.split(sep="|"))
                page_ordering_rules.append([int(numbers[0]),int(numbers[1])])
                ordering_rules_by_number[int(numbers[0])] = []
            elif "," in line:
                line = line.strip()
                numbers = list(line.split(sep=","))
                page_numbers_to_update.append([int(page) for page in numbers])
            elif line == "\n":
                continue
        # Dict for ordering rules by number creation
        for ordering_rule in page_ordering_rules:
            ordering_rules_by_number[ordering_rule[0]] = [number[1] for number in page_ordering_rules if number[0] == ordering_rule[0]]
        for update in page_numbers_to_update:
            correct_order = True
            for it in range(len(update)):
                try:
                    rule = ordering_rules_by_number[update[it]]
                    for item in range(len(update)):
                        if update[it] != update[item]:
                            if update[item] in rule and it > item:
                                correct_order = False
                            else:
                                continue
                except KeyError: # If the page is not on the dict, then no rule need to be applied
                    continue
            if correct_order:
                # Find the middle number and add it to the final sum
                middle_numbers_addition += update[int(len(update)/2)]

    print(middle_numbers_addition)
