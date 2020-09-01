def find_duplicates(list):
    duplicates = []
    for item in list:
        if list.count(item) > 1:
            if item not in duplicates:
                duplicates.append(item)
    return duplicates


print(find_duplicates(['a', 'b', 'c', 'a', 'd', 'd', 'e', 'f', 'g', 'f']))

# or without function()


list = ['a', 'b', 'c', 'a', 'd', 'd', 'e', 'f', 'g', 'f']

duplicates = []

for items in list:
    if list.count(items) > 1:
        if items not in duplicates:
            duplicates.append(items)
print(duplicates)
