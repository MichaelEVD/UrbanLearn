class WordsFinder:
    def __init__(self,*names):
        self.name = names

    def get_all_words(self):
        all_words = dict()
        file_names = tuple()
        file_names += self.name
        chars_to_remove = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for i in file_names:
            words_list = []
            with open(i, encoding='UTF=8') as file:
                file_list = file.readlines()
            for j in range(len(file_list)):
                file_list[j] = file_list[j].lower()
                file_list[j] = file_list[j].split()
                words_list.extend(file_list[j])
            for t in range(len(words_list)):
                for p in chars_to_remove:
                    words_list[t] = ''.join(words_list[t].split(p))
            all_words.update({i: words_list})
        return all_words

    def find(self, word):
        self.word = word
        find_word = {}
        word = word.lower()
        for name, words in self.get_all_words().items():
            for i,v in enumerate(words,1):
                if v == word:
                    find_word.update({name: i})
                    break
            else:
                continue
        return find_word

    def count(self, word):
        self.word = word
        count_word = {}
        word = word.lower()
        for name, words in self.get_all_words().items():
            coun_t = 0
            for i, v in enumerate(words, 1):
                if v == word:
                    coun_t += 1
                    count_word.update({name: coun_t})
                else:
                    continue
        return count_word


# finder2 = WordsFinder('test_file.txt')
# print(finder2.get_all_words())
# print(finder2.find('TEXT'))
# print(finder2.count('teXT'))

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt','Rudyard Kipling - If.txt',
                           'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))
