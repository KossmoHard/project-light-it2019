def even_elements(arr):

    new_arr = list(map(lambda x: x.lower() if isinstance(x, str) else x, arr))

    for i in new_arr:
        if new_arr.count(i) % 2 == 0:
            return True
    return False


print(even_elements([3, 2, 'two', 'aPple', 'ApplE', 1]))
print(even_elements([3, '3', 2, 'two', 'apple', 'apple', 'apple']))
