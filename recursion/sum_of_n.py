# def sum_num(n):
#     sum = 0
#     if n == 0:
#         return
#     if n < sum:
#         sum += n
#         print(sum)
#     sum_num(n+1)
# sum_num(10)


def sum_num(n):
    if n == 0:
        return 0
    return n + sum_num(n-1)
print(sum_num(5))

