calls = 0
def count_calls(n):
    global calls
    calls += n

def string_info(str1):
    length = len(str1)
    U = str1.upper()
    L = str1.lower()
    answer2 = length, U, L
    count_calls(1)
    return answer2

def is_contains(string, list_to_search):
    presence = False
    list_to_search_new = []
    string = string.lower()
    for i in list_to_search:
        list_to_search_new.append(i.lower())
    if string in list_to_search_new:
        presence = True
    count_calls(1)
    return presence


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)




