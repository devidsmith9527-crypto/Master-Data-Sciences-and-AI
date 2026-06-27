def sqrt_bs(n):
    l, r = 0, n
    ans = 0
    while l <= r:
        mid = (l + r) // 2
        if mid * mid <= n:
            ans = mid  # រក្សាទុកតម្លៃដែលទំនងអាចជាចម្លើយ
            l = mid + 1
        else:
            r = mid - 1
    return ans


print("ឫសការ៉េនៃ 25 គឺ:", sqrt_bs(81))
