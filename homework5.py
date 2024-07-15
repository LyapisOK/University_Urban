immutable_var = (1, 2, 'Sasha', [True, 11])
print('Immutable var:', immutable_var)

#immutable_var[0] = 3 в кортеже нельзя изменить неизменяемые типы данных (числа, строки)
#print(immutable_var)

mutable_list = ([1, 2, 'Student', True], [9, 8, 'Teacher', False])
print('Mutable list:', mutable_list)
mutable_list[0][1] = 2024
mutable_list[1][3] = 'Ложь'
print('New Mutable list:', mutable_list)