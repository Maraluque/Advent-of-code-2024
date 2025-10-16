
if __name__ == '__main__':
    similarity = 0
    separator = "   "
    list_a = []
    list_b = []

    with open("input.txt", "r") as f:
        lines = f.readlines()
        # 1. Split the input in two separate lists of numbers
        for line in lines:
            a_item, b_item = line.split(separator)[0], line.split(separator)[1]
            list_a.append(int(a_item))
            list_b.append(int(b_item.replace("\n","")))

        # 2. Iterate into both lists searching the list_a[i] number in list_b, count the times that
        # appear and multiply to obtain the similarity
        for item in list_a:
            similarity += item * list_b.count(item)

        print(similarity)

