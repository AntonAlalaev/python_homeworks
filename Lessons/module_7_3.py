class FileOps:

    @staticmethod
    def clear_punctuation(raw_data):
        symbols_to_remove = [',', '.', '=', '!', '?', ';', ':', '-']
        for symbol in symbols_to_remove:
            raw_data = raw_data.replace(symbol, "")
        return raw_data

    def __init__(self, file_name):
        self.file_name = file_name

    # Возвращает перечень слов
    def get_words(self):
        with open(self.file_name, "r", encoding="utf-8") as file:
            raw_data = file.read()
            raw_data = self.clear_punctuation(raw_data)
            raw_data = raw_data.lower()
            word_list = raw_data.split()
        return word_list

    def find(self, word):
        word_list = self.get_words()
        for index, string in enumerate(word_list, start=1):
            if string == word.lower():
                return index
        return None

    def count(self, word):
        word_list = self.get_words()
        count = 0
        for item in word_list:
            if item == word.lower():
                count += 1
        return count


class WordsFinder:

    # Конструктор
    def __init__(self, *args):
        self.file_names = args
        # print(self.filenames)

    # Возвращает все слова в файлах
    def get_all_words(self):
        all_words = {}
        for item in self.file_names:
            f = FileOps(item)
            all_words[item] = f.get_words()
        return all_words

    def find(self, word):
        found_word = {}
        for item in self.file_names:
            f = FileOps(item)
            fin = f.find(word)
            if fin is None:
                continue
            found_word[item] = fin
        return found_word

    def count(self, word):
        count_word = {}
        for item in self.file_names:
            f = FileOps(item)
            cnt = f.count(word)
            if cnt == 0:
                continue
            count_word[item] = cnt
        return count_word


pt = WordsFinder("Mother Goose - Monday’s Child.txt", "test.txt")
fop = FileOps("Mother Goose - Monday’s Child.txt")

print(fop.get_words())
print(fop.find("Child"))
print(fop.count("Child"))
print(pt.get_all_words())
print(pt.count("there"))
print(pt.find("there"))
