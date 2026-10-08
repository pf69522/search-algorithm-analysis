def recursive_binary_search(values, target, low, high):
    if low > high:
        return -1

    middle = (low + high) // 2

    if values[middle] == target:
        return middle
    elif target < values[middle]:
        return recursive_binary_search(
            values, target, low, middle - 1
        )
    else:
        return recursive_binary_search(
            values, target, middle + 1, high
        )


def iterative_binary_search(values, target):
    low = 0
    high = len(values) - 1

    while low <= high:
        middle = (low + high) // 2

        if values[middle] == target:
            return middle
        elif target < values[middle]:
            high = middle - 1
        else:
            low = middle + 1

    return -1


def sequential_search(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index

    return -1
