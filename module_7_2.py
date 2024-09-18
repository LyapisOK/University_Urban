from pprint import pprint

def custom_write(file_name, strings):
    strings_position = {}
    file = open(file_name, 'a+')
    #pprint(file.read())
    for string in strings:
        file.write(string + '\n')
    #pprint(file.read())
    #file.write(string + '\n')
    file.close()
    
    file = open(file_name, 'r')
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
    return strings_position

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
#print(result)
for key, volue in result.items():
    print(key, volue, end='')
