first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']
first_result = [len(name_first) for name_first in first_strings if len(name_first) > 5]
second_result = [(name_first, name_second)
                 for name_first in first_strings
                 for name_second in second_strings
                 if len(name_second) == len(name_first)]
new_strings = first_strings + second_strings
print(new_strings)
third_result = {name_new_string: len(name_new_string)
                for name_new_string in new_strings
                if len(name_new_string) % 2 == 0 }
print(first_result)
print(second_result)
print(third_result)