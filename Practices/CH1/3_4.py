def has_duplicates(arr):
    n = len(arr)
    for i in range(n):
        # ប្រៀបធៀប i ជាមួយធាតុបន្ទាប់ៗទាំងអស់
        for j in range(i + 1, n):
            if arr[i] == arr[j]:
                return True
    return False


print("មានស្ទួនទេ?", has_duplicates([1, 2, 3, 9]))
