'''Task 6. 15 Посчитать общее количество наименований в списке. И только в списках.
Example:
shedule = {'monday': ['clean house', 'drive car', 'meet with freands'], 'thuesday': None, 'wednesday': ['manicure', 'hammam', 'beer']}
Результат: 6'''


shedule = {'monday': ['clean house', 'drive car', 'meet with freands'], 'thuesday': None, 'wednesday': ['manicure', 'hammam', 'beer']}
l_shedule = list(shedule) # создаем список ключей исходного словаря
count = 0 # задаем счетчик элементов списков
for a in range(len(l_shedule)):
    if shedule[l_shedule[a]] == None: # обход ошибки в случае отсутствия значения у ключа словаря
        continue
    count += len(shedule[l_shedule[a]]) # считаем количество элементов в каждом списке словаря
print(count)