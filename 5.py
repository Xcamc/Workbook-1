for x in range(2):
    for y in range(2):
        if (x or y) and (not (x) or y) and not (x and y):
            print(x, y)
