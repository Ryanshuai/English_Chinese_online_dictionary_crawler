import Levenshtein


class Distance_Similar:
    def __init__(self):
        all_word_txt = 'D:/github_project/make_anki_word_list/word_list/all.txt'
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

    def get_similar_word_str(self, word1):
        similar_words_str = ''
        for word2 in self.all_word_set:
            if self.is_word_similar(word1, word2):
                if similar_words_str != '':
                    similar_words_str += '<br>'
                similar_words_str += word2

        return similar_words_str


class No_Prefix_Similar:
    def __init__(self):
        self.for_s_begin_root_list = ['ex']
        self.a_prefix_list = ['a']
        self.co_prefix_list = ['co']
        self.prefix_list = ['com', 'con', 'dis', 'sub', 'pro', 'mis', 'per', 'pre', 'co', 'in', 'ex', 'im', 'en', 'ex', 're', 'di', 'ob', 'ab', 'ad', 'de', 'un', 'se', 'e', 'a']

        all_word_txt = 'D:/github_project/make_anki_word_list/word_list/all.txt'
        with open(all_word_txt, 'r', encoding='utf-8') as f:
            word_list = f.read().splitlines()
        self.all_word_set = set(word_list)

        self.word_root_suffix_dict = dict()
        for word in self.all_word_set:
            self.word_root_suffix_dict[word] = self.get_remove_prefix_set(word)

    def get_remove_prefix_set(self, word: str):
        possible_word_without_prefix_set = {word}
        for prefix in self.a_prefix_list:
            if word.startswith(prefix) and len(word) > 3 and word[1] == word[2]:
                possible_word_without_prefix_set.add(word[len(prefix)+1:])
        for prefix in self.for_s_begin_root_list:
            if word.startswith(prefix):
                possible_word_without_prefix_set.add(word[len(prefix):])
                possible_word_without_prefix_set.add('s'+word[len(prefix):])
        for prefix in self.co_prefix_list:
            if word.startswith(prefix) and len(word) > 4 and word[2] == word[3]:
                possible_word_without_prefix_set.add(word[3:])
        for prefix in self.prefix_list:
            if word.startswith(prefix):
                possible_word_without_prefix_set.add(word[len(prefix):])
        return possible_word_without_prefix_set

    def is_word_similar(self, word1, word2):
        if word1.lower() == word2.lower():
            return False
        root1_set = self.word_root_suffix_dict[word1]
        root2_set = self.word_root_suffix_dict[word2]

        if len(root1_set & root2_set) > 0:
            return True
        return False

    def get_similar_word_list(self, word1):
        similar_list = list()
        for word2 in self.all_word_set:
            if self.is_word_similar(word1, word2):
                similar_list.append(word2)
        return similar_list

    def get_similar_word_str(self, word1):
        similar_words_str = ''
        for word2 in self.all_word_set:
            if self.is_word_similar(word1, word2):
                if similar_words_str != '':
                    similar_words_str += '<br>'
                similar_words_str += word2
        return similar_words_str


class No_Suffix_Similar:
    def __init__(self):
        self.suffix_change_dict = {'i': ['y'], 's': ['t', 'd'], 't': ['d'], 'e': ['i']}
        self.a_suffix_list = []
        self.co_suffix_list = []
        self.suffix_list = ['ability', 'action', 'ative', 'acity', 'ation', 'atory', 'able', 'ably', 'acle', 'ance', 'ence', 'ency', 'eous', 'less', 'like', 'ment', 'ness', 'ship', 'tion', 'ture', 'ate', 'ant', 'ent', 'ful', 'ial', 'ian', 'ics', 'ine', 'ing', 'ion', 'ism', 'ish', 'ist', 'ite', 'ity', 'ive', 'ize', 'tic', 'ter', 'ed', 'en', 'er', 'ia', 'al', 'ic', 'ly', 'ty', 'fy', 'on', 'or', 'o', 'y', 'e']

        all_word_txt = 'D:/github_project/make_anki_word_list/word_list/all.txt'
        with open(all_word_txt, 'r', encoding='utf-8') as f:
            word_list = f.read().splitlines()
        self.all_word_set = set(word_list)

        self.word_prefix_root_dict = dict()
        for word in self.all_word_set:
            self.word_prefix_root_dict[word] = self.get_remove_suffix_set(word)

    def get_remove_suffix_set(self, word: str):
        possible_word_without_suffix_set = {word}
        for suffix in self.suffix_list:
            prefix_root = word[:-len(suffix)]
            if word.endswith(suffix) and len(prefix_root) >= 4:
                possible_word_without_suffix_set.add(word[:-len(suffix)])
                if prefix_root[-1] in self.suffix_change_dict:
                    for change_c in self.suffix_change_dict[prefix_root[-1]]:
                        i2y_word = prefix_root[:-1] + change_c
                        possible_word_without_suffix_set.add(i2y_word)
        return possible_word_without_suffix_set

    def is_word_similar(self, word1, word2):
        if word1.lower() == word2.lower():
            return False
        root1_set = self.word_prefix_root_dict[word1]
        root2_set = self.word_prefix_root_dict[word2]

        if len(root1_set & root2_set) > 0:
            return True
        return False

    def get_similar_word_list(self, word1):
        similar_list = list()
        for word2 in self.all_word_set:
            if self.is_word_similar(word1, word2):
                similar_list.append(word2)
        return similar_list

    def get_similar_word_str(self, word1):
        similar_words_str = ''
        for word2 in self.all_word_set:
            if self.is_word_similar(word1, word2):
                if similar_words_str != '':
                    similar_words_str += '<br>'
                similar_words_str += word2
        return similar_words_str


if __name__ == '__main__':
    # ds = Distance_Similar()
    # # print(ds.is_word_similar('expect', 'respect'))
    # print(ds.get_similar_word_str('inevitable'))

    nrs = No_Prefix_Similar()
    print(nrs.is_word_similar('impervious', 'pervious'))
    print(nrs.get_similar_word_str('expect'))
    print('-------------------------')

    # nrs = No_Suffix_Similar()
    # print('-------------------------')
    # print(nrs.is_word_similar('alliance', 'ally'))
    # print(nrs.get_similar_word_str('retentive'))


