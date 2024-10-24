import threading
from threading import Thread
from time import sleep
from datetime import datetime

def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(f'Какое-то слово № {word_count}')
        sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')

start_functions_time = datetime.now()
write_words(10, 'exampe1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

end_functions_time = datetime.now()
duration_functions_time = end_functions_time - start_functions_time
print(f"Работа функций {duration_functions_time}")

start_thread_time = datetime.now()
thr1 = Thread(target=write_words, args=(10, 'example5.txt'))
thr2 = Thread(target=write_words, args=(30, 'example6.txt'))
thr3 = Thread(target=write_words, args=(200, 'example7.txt'))
thr4 = Thread(target=write_words, args=(100, 'example8.txt'))

thr1.start()
thr2.start()
thr3.start()
thr4.start()

thr1.join()
thr2.join()
thr3.join()
thr4.join()

end_thread_time = datetime.now()
duration_thread_time = end_thread_time - start_thread_time
print(f"Работа функций {duration_thread_time}")