my_dict = {'Denis' : 1999, 'Nikita' : 1998, 'Stas' : 2000}
print('Dict:',  my_dict)
print('Existing value:', my_dict.get('Nikita'))
print('Not existing value:', my_dict.get('Nikit'))
my_dict.update({'Sasha' : 1997,
                'Olya' : 2002})
print('Modified dictionary:', my_dict)
del_ = my_dict.pop('Denis')
print('Deleted value:', del_)

print()
print('Задание 3:')
print()

my_set = {1999, 'Student', 3, 'Student', 1999, True, False, True}
print('Set:', my_set)
my_set.add((1, 2, 3, 4))
my_set.add('Teacher')
my_set.discard('Student')
print('Modified set:', my_set)
