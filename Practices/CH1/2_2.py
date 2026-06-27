def find_max(arr):
    max_val = arr[0]
    for x in arr:
        if x > max_val:
            max_val = x
    return max_val


print("លេខធំបំផុតគឺ:", find_max([3, 1, 4, 8, 2]))
