class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names
        #print(file_names)


    def get_all_words(self):
        all_words = {}
        not_simbol = [',', '.', '=', '!', '?', ';', ':', ' - ']

        for file_name in self.file_names:
            print(file_name)
            with open(file_name, 'r', encoding='utf-8') as file:
                file_str = (file.read().lower())
                for i in not_simbol:
                    if  i in file_str:
                        file_str = file_str.replace(i, '')
                new_str = file_str.split()
                all_words[file_name] = new_str
                #print(new_str)
        return all_words
    def find(self, word):
        self.word = word
        for name, words in get_all_words().items():
    def count(self, word):


finder2 = WordsFinder('test.txt', 'Sample.txt')
print(finder2.get_all_words())