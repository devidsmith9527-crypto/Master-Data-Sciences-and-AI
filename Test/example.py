import bisect

# ១. តម្រៀបទិន្នន័យដោយប្រើ Timsort
data = [38, 27, 43, 30, 9]
data.sort()  # data ក្លាយជា [9, 27, 30, 38, 43]

# ២. ស្វែងរកទីតាំងស៊កបញ្ចូលដោយប្រើ bisect
idx = bisect.bisect_left(data, 27)
print(idx)  # Output: 1
