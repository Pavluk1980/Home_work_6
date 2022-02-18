'''Task 4. 15
Удалить дубликаты из dictionary
пример

Before :

{'id1':{'name': 'Ruslan','class': 1,'subjects' : {'Math', 'Algorithms', 'English'}},
'id2':{'name': 'Mark','class': 2,'subjects' : {'Geometry', 'Java', 'Cooking'}},
'id3':{'name': 'Ruslan','class': 1,'subjects' : {'Math', 'Algorithms', 'English'}}}

After:

{'id1':{'name': 'Ruslan','class': 1,'subjects' : {'Math', 'Algorithms', 'English'}},
'id2':{'name': 'Mark','class': 2,'subjects' : {'Geometry', 'Java', 'Cooking'}}'''


import copy
dict_1 = {'id1':{'name': 'Ruslan','class': 1,'subjects' : {'Math', 'Algorithms', 'English'}},
          'id2':{'name': 'Mark','class': 2,'subjects' : {'Geometry', 'Java', 'Cooking'}},
          'id3':{'name': 'Ruslan','class': 1,'subjects' : {'Math', 'Algorithms', 'English'}}}
dict_l = list(dict_1) # создаем список ключей 1го уровня от заданного словаря
dict_2 = copy.deepcopy(dict_1) # создаем глубокую копию заданного словаря
for k in range(len(dict_l)): # задаем 2х уровневый цикл по длине списка ключей, для взаимного перекрестного сравнения элементов словаря
    for i in range(len(dict_l)):
        if k == i: continue # исключаем сравнения равно адресных элементов словаря
        if dict_1[dict_l[k]] == dict_1[dict_l[i]]: # сравниваем элементы словаря
           dict_1[dict_l[i]] = {} # в случае равенства элементов, заменяем текущее значение на "пустое"
for a in range(len(dict_l)):
    if dict_1[dict_l[a]] == {}: # проверка всех элементов списка на "пустые" значения
        dict_2.pop(dict_l[a]) # удаляем совпавшие по значениям объекты словаря 1 из словаря 2
print(dict_2)
