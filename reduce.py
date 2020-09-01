from functools import reduce
# reduce() function and it's not Python built in function: We habe to import it!

my_list = [1, 2, 3, 4, 5]
my_scores = [73, 20, 65, 19, 76, 100, 88]


def accumulator(acc, item):
    return acc + item


print(reduce(accumulator, my_list, 0))  # Getting sum of my_list

# Getting sum of 2 lists -> my_list + my_scores
print(reduce(accumulator, (my_list + my_scores)))

# lambda function example with reduce
print(reduce(lambda x, y: x + y, (my_scores + my_list)))
