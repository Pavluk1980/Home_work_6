'''Task 1. 5 points
сложить словари в один.
использовать for и dict methods.

first = {1: 10, 2: 20}
second = {3: 30, 4: 40}
third = {5: 50, 6: 60}
fourth = {7: 70, 8: 80}
fifth = {9: 90, 10: 100}'''


first = {1: 10, 2: 20}
second = {3: 30, 4: 40}
third = {5: 50, 6: 60}
fourth = {7: 70, 8: 80}
fifth = {9: 90, 10: 100}

sum_all = {**first, **second, **third, **fourth, **fifth} # сложение словарей
print(sum_all)

first.update(second) # сложение словарей методом .update
first.update(third)
first.update(fourth)
first.update(fifth)
print(first)

