'''Task3. 5 points

отсортировать словарь по ключам'''


a = {'b' : "two", 'c' : "three", 'a' : "one"} # задаем словарь
b_sort = {} # создаем пустой словарь для конечного списка
c_sort = {} # создаем пустой словарь для временного списка
b_sort = {x: a[x] for x in sorted(a)} # используем dict comprehension для создания отсортированного по ключам словаря

            # вариант создания словаря с сортировкой с помощью обычного цикла
# c_sort = {} # создаем пустой словарь для временного списка
# for x in sorted(a): # задаем цикл по отсортированным значениям ключей списка
#     c_sort = {x: a[x]} # временный список для хранения текущей пары "ключ : значение"
#     b_sort.update(c_sort) # конечный список в который мы поочредно добавляем временный список каждую итерацию цикла

print(b_sort) # выводим на экран отсортированный список
