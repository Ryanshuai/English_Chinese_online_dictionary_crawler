import Levenshtein


class Distance_Similar:
    def __init__(self):
        all_word_txt = 'D:/github_project/make_anki_word_list/word_list/all_word_list.txt'
        with open(all_word_txt, 'r', encoding='utf-8') as f:
            word_list = f.read().splitlines()

        self.all_word_set = set(word_list)

    def is_word_similar(self, word1: str, word2: str):
        if word1.lower() == word2.lower():
            return False
        if len(word1) <= 4 or len(word2) <= 4:
            return False
        dis = Levenshtein.distance(word1.lower(), word2.lower())
        if dis == 1:
            return True
        if word1 in word2 or word2 in word1:
            affix_word_list = ['table', 'cable', 'inter']
            if word1 in affix_word_list or word2 in affix_word_list:
                return False
            return True
        return False

    def get_similar_word_list(self, word):
        similar_list = list()
        for s in self.all_word_set:
            if self.is_word_similar(s, word):
                similar_list.append(s)

        return similar_list

    def get_similar_word_str(self, word):
        similar_words_str = ''
        for s in self.all_word_set:
            if self.is_word_similar(s, word):
                if similar_words_str != '':
                    similar_words_str += '<br>'
                similar_words_str += s

        return similar_words_str


class No_Prefix_Similar:
    def __init__(self):
        self.s_end_prefix_list = ['ex']
        self.a_prefix_list = ['a']
        self.co_prefix_list = ['co']
        self.prefix_list = ['com','con','dis','sub','pro','mis','per','pre','co','in','ex','im','en','ex','re','di','ob','ab','ad','de','un','se','e','a']

        all_word_txt = 'D:/github_project/make_anki_word_list/word_list/all_word_list.txt'
        with open(all_word_txt, 'r', encoding='utf-8') as f:
            word_list = f.read().splitlines()
        self.all_word_set = set(word_list)

    def remove_prefix(self, word: str):
        possible_word_without_prefix_list = list()
        for prefix in self.a_prefix_list:
            if word.startswith(prefix) and len(word) > 3 and word[1] == word[2]:
                possible_word_without_prefix_list.append(word[len(prefix)+1:])
        for prefix in self.s_end_prefix_list:
            if word.startswith(prefix):
                possible_word_without_prefix_list.append(word[len(prefix):])
                possible_word_without_prefix_list.append('s'+word[len(prefix):])
        for prefix in self.co_prefix_list:
            if word.startswith(prefix) and len(word) > 4 and word[2] == word[3]:
                possible_word_without_prefix_list.append(word[3:])
        for prefix in self.prefix_list:
            if word.startswith(prefix):
                possible_word_without_prefix_list.append(word[len(prefix):])
        return possible_word_without_prefix_list

    def is_word_similar(self, word1, word2):
        if word1.lower() == word2.lower():
            return False
        root1_list = self.remove_prefix(word1)
        root2_list = self.remove_prefix(word2)

        if len(set(root1_list).intersection(set(root2_list))) > 0:
            return True
        return False

    def get_similar_word_list(self, word1):
        similar_list = list()
        for word2 in self.all_word_set:
            if self.is_word_similar(word1.lower(), word2.lower()):
                similar_list.append(word2)
        return similar_list

    def get_similar_word_str(self, word):
        similar_words_str = ''
        for s in self.all_word_set:
            if self.is_word_similar(s.lower(), word.lower()):
                if similar_words_str != '':
                    similar_words_str += '<br>'
                similar_words_str += s
        return similar_words_str


class No_Suffix_Similar:
    def __init__(self):
        self.s_end_suffix_list = []
        self.a_suffix_list = []
        self.co_suffix_list = []
        self.suffix_list = ['ability', 'action', 'ative', 'acity', 'ation', 'atory', 'able', 'ably', 'acle', 'ence', 'ency', 'eous', 'less', 'like', 'ment', 'ness', 'ship', 'tion', 'ture', 'ate', 'ent', 'ful', 'ial', 'ian', 'ics', 'ine', 'ing', 'ion', 'ism', 'ish', 'ist', 'ite', 'ity', 'ive', 'ize', 'tic', 'ed', 'en', 'er', 'ia', 'al', 'ic', 'ly', 'on', 'or', 'o', 'y', 'e']

        all_word_txt = 'D:/github_project/make_anki_word_list/word_list/all_word_list.txt'
        with open(all_word_txt, 'r', encoding='utf-8') as f:
            word_list = f.read().splitlines()
        self.all_word_set = set(word_list)

    def remove_suffix(self, word: str):
        possible_word_without_suffix_list = list()
        for suffix in self.a_suffix_list:
            if word.endswith(suffix) and len(word) > 3 and word[1] == word[2]:
                possible_word_without_suffix_list.append(word[len(suffix)+1:])
        for suffix in self.s_end_suffix_list:
            if word.endswith(suffix):
                possible_word_without_suffix_list.append(word[len(suffix):])
                possible_word_without_suffix_list.append('s'+word[len(suffix):])
        for suffix in self.co_suffix_list:
            if word.endswith(suffix) and len(word) > 4 and word[2] == word[3]:
                possible_word_without_suffix_list.append(word[3:])
        for suffix in self.suffix_list:
            if word.endswith(suffix) and len(word[:-len(suffix)]) >= 4:
                possible_word_without_suffix_list.append(word[:-len(suffix)])
        return possible_word_without_suffix_list

    def is_word_similar(self, word1, word2):
        if word1.lower() == word2.lower():
            return False
        root1_list = self.remove_suffix(word1)
        root2_list = self.remove_suffix(word2)

        if len(set(root1_list).intersection(set(root2_list))) > 0:
            return True
        return False

    def get_similar_word_list(self, word1):
        similar_list = list()
        for word2 in self.all_word_set:
            if self.is_word_similar(word1.lower(), word2.lower()):
                similar_list.append(word2)
        return similar_list

    def get_similar_word_str(self, word):
        similar_words_str = ''
        for s in self.all_word_set:
            if self.is_word_similar(s.lower(), word.lower()):
                if similar_words_str != '':
                    similar_words_str += '<br>'
                similar_words_str += s
        return similar_words_str


if __name__ == '__main__':
    # nrs = No_Prefix_Similar()
    # print(nrs.is_word_similar('separate', 'disparate'))
    # print(nrs.get_similar_word_str('inevitable'))
    # print('-------------------------')
    # ds = Distance_Similar()
    # # print(ds.is_word_similar('expect', 'respect'))
    # print(ds.get_similar_word_str('inevitable'))

    nrs = No_Suffix_Similar()
    print('-------------------------')
    print(nrs.is_word_similar('unexceptionable', 'unexceptional'))
    print(nrs.get_similar_word_str('retentive'))


