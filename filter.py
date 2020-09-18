# filter() function
listofnums = [1, 2, 3, 4, 5]
names = ['Erikas', 'Sigita', 'Karolina']


def first_letter_E(item):
    if item[:1] == 'E':
        return item


def only_odd(num):
    return num % 2 != 0


print(list(filter(only_odd, listofnums)))
print(list(filter(first_letter_E, names)))

print(list(filter(lambda item: item[:1] == 'E', names)))

print(list(filter(lambda x: x % 2 == 0, listofnums)))
