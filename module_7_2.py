from idlelib.iomenu import encoding


def custom_write(file_name, strings):
    strings_position = {}
    for string in strings:

        file = open(file_name, 'a+', encoding = 'utf8')
        file.write(string + '\n')
        file.close()

    file = open(file_name, 'r', encoding = 'utf8')
    st = 1
    b_line = 0
    while True:
        line = file.readline()
        if not line:
            break
        else:
            strings_position[st, b_line] = line
            #print(st, b_line)
            st += 1
            b_line = file.tell()

    #print(strings_position)
    for key, volue in strings_position.items():
        print(key, volue)



info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)

