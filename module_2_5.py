def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    return matrix
print(get_matrix(int(input('Введите количство строк: ')), int(input('Введите количество стобцов: ')), int(input('Введите значение: '))))