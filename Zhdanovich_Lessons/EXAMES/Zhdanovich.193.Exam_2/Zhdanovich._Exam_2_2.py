#2.	Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
# Например, два одинаковых элемента образуют одну пару, 3 элемента образуют 3 пары,
# 4 элемента образуют 6 пар и т.д. Воспользуйтесь формулой:
# Количество пар = (Общее число элементов X Общее число элементов — 1) / 2

c = [1, 2, 2, 2, 3, 4, 4, 5, 6, 6, 6, 6]
c_1 = set(c)
# print(c_1)
for i in c_1:
    n = c.count(i)
    p = int((n*(n-1))/2)
    if p != 0:
        print(f'Количество пар числа {i} в списке равно {p}')