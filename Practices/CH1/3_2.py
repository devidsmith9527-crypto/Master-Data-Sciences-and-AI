def print_matrix(n):
    for i in range(1, n + 1):
        row = []
        for j in range(1, n + 1):
            row.append(i * j)
        print(row)


print_matrix(3)
