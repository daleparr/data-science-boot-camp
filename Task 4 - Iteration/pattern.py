total_height = 9

midpoint = (total_height + 1) //2

for i in range(1, total_height + 1):

    if i <=midpoint:
        num_asterisks = i

    else:
        num_asterisks = total_height - i + 1

    print("*" * num_asterisks)