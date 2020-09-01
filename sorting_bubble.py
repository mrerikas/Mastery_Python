def bubble(unsorted):
    index_lenght = len(unsorted) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, index_lenght):
            if unsorted[i] > unsorted[i+1]:
                sorted = False
                unsorted[i], unsorted[i+1] = unsorted[i+1], unsorted[i]
    return unsorted


print(bubble([1, 3, 2, 6, 4, 5, 7, 9, 8]))
