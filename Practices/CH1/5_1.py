def sum_O1_space(n):
    total = 0  # បង្កើតអថេរតែមួយគត់
    for i in range(1, n + 1):
        total += i
    return total


print("ផលបូក (Space O(1)):", sum_O1_space(6))
