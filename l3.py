def binary_search(lst, item):
    low = 0
    high = len(lst) - 1
    while high > low:
        mid = (low + high) // 2
        guess = lst[mid]
        if guess == item:
            return mid
        if item > guess:
            low = mid + 1
        else:
            high = mid - 1
    return None


my_list = [i for i in range(1, 10)]
#print(binary_search(my_list, 9))
#print(binary_search(my_list, 4))

