def find_intersection(list1, list2):
    # បំប្លែងទៅជា Set ប្រើ Space O(n)
    set1 = set(list1)

    # ស្វែងរក 'x in set1' ប្រើពេលតែ O(1) លឿនបំផុត
    res = [x for x in list2 if x in set1]
    return res


print("តម្លៃដូចគ្នា:", find_intersection([1, 2, 3], [2, 3, 4]))
