import os
import glob

# for file in "C:\\Users\\eriku\\Desktop\\New folder":
with open('saskaitos.txt', 'r') as f:
    data = f.read().split()
    saskaitos = []
    for elem in data:
        try:
            saskaitos.append(float(elem))
        except ValueError:
            pass
print(saskaitos)
average = sum(saskaitos) / len(saskaitos)
print(round(average, 2))
