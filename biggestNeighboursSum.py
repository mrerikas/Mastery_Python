list = [1, 5, 2, 7, 2, 9, 7, 5, 1]

max_sum = 0
for num in range(len(list)-1):
    if list[num]*list[num+1] > max_sum:
        max_sum = list[num]*list[num+1]
print(max_sum)

a = [1, 2, 3, 642, 457, 48, 276, 38]
