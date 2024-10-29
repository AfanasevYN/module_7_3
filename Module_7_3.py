import string

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                words = []
                for line in file:
                    line = line.lower()
                    line = line.translate(str.maketrans('','', string.punctuation))
                    words += line.split()
                all_words[file_name] = words
        return all_words

    def find_(self, word):
        results = {}
        all_words = self.get_all_words()
        word = word.lower()  # Приводим слово к нижнему регистру для поиска
        for file_name, words in all_words.items():
            if word in words:
                results[file_name] = words.index(word)  # Получаем индекс слова в списке
        return results

    def count_(self, word):
        results = {}
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            results[file_name] = words.count(word)
        return results

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find_('TEXT')) # 3 слово по счёту
print(finder2.count_('teXT')) # 4 слова teXT в тексте всего
