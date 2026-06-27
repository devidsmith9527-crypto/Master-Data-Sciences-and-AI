def squares_On_space(n):
    res = []  # បង្កើត Array ថ្មី
    for i in range(1, n + 1):
        res.append(i * i)  # ផ្ទុកចូលតាមចំនួន N
    return res


print("តម្លៃការ៉េ (Space O(n)):", squares_On_space(5))
