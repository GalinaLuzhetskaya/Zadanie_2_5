def get_matrix (n, m, value):       # Объявляем функцию get_matrix и записываем в нее параметры n, m и value
    matrix =[]                      # Создаем пустой список matrix
    for i in range(n):              # Организуем цикл по кол-ву строк n
        matrix.append([])           # Добавляем в список matrix пустой список
        for j in range(m):          # Организуем цикл по кол-ву столбцов m
            matrix[i].append(value) # В каждый элемент столбца записываем значение value
    return matrix                   # Возвращаем значение переменной matrix.
print(get_matrix (2, 2, 10)) # Выводим на экран результат работы функции get_matrix
print(get_matrix (3,5,42))
print(get_matrix (4,2,13))

