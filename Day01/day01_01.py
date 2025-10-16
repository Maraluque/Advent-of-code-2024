
if __name__ == '__main__':
    distance = 0
    separator = "   "
    list_a = []
    list_b = []

    with open("custom_input.txt", "r") as f:
        lines = f.readlines()
        # 1. Split the input in two separate lists of numbers
        for line in lines:
            a_item, b_item = line.split(separator)[0], line.split(separator)[1]
            list_a.append(int(a_item))
            list_b.append(int(b_item.replace("\n","")))

        # 2. Sort the lists from small to bigger numbers
        list_a = sorted(list_a)
        list_b = sorted(list_b)

        # 3. Iterate into both lists comparing its "i" number and subtract the distance
        for i in range(len(list_a)):
            distance += abs(list_a[i] - list_b[i])

        print(distance)

