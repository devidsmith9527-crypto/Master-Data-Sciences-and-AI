def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            # ប្រៀបធៀបអ្នកនៅក្បែរគ្នា បើអ្នកមុខធំជាង ដូរទីតាំង
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


print("តម្រៀប:", bubble_sort([5, 7, 4, 2]))
