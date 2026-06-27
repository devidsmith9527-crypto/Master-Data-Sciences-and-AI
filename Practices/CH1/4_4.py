def fast_power(base, exp):
    res = 1
    while exp > 0:
        if exp % 2 == 1:  # បើស្វ័យគុណសេស
            res *= base
        base *= base  # ការ៉េខ្លួនឯង
        exp //= 2  # កាត់បន្ថយពាក់កណ្តាល
    return res


print("2 ស្វ័យគុណ 10 គឺ:", fast_power(2, 10))
