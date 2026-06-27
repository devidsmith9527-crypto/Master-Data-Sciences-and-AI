def count_halves(n):
    count = 0
    while n > 1:
        n = n // 2  # ចែកពាក់កណ្តាលរហូត
        count += 1
    return count


print("ចំនួនដងដែល 16 អាចចែកនឹង 2 បានគឺ:", count_halves(16))
