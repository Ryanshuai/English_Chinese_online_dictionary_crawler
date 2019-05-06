import Levenshtein


class Distance_Similar:
    def __init__(self):
        cet4_txt = 'D:/github_project/make_anki_word_list/word_list/4-cet.txt'
        cet6_txt = 'D:/github_project/make_anki_word_list/word_list/6-cet.txt'
        post_txt = 'D:/github_project/make_anki_word_list/word_list/考研词汇表.txt'
        toefl_qu_txt = 'D:/github_project/make_anki_word_list/word_list/曲根10000词汇表.txt'
        toefl_red_txt = 'D:/github_project/make_anki_word_list/word_list/托福红宝书.txt'
        toefl_class = 'D:/github_project/make_anki_word_list/word_list/分类词汇.txt'
        gre300_txt = 'D:/github_project/make_anki_word_list/word_list/3000.txt'
        gre_foot_txt = 'D:/github_project/make_anki_word_list/word_list/佛脚词.txt'
        gre_red_txt = 'D:/github_project/make_anki_word_list/word_list/gre红宝书.txt'

        input_txt_list = list()
        input_txt_list.append(cet4_txt)
        input_txt_list.append(cet6_txt)
        input_txt_list.append(post_txt)
        input_txt_list.append(toefl_qu_txt)
        input_txt_list.append(toefl_red_txt)
        input_txt_list.append(toefl_class)
        input_txt_list.append(gre300_txt)
        input_txt_list.append(gre_foot_txt)
        input_txt_list.append(gre_red_txt)

        input_word_set = set()
        for file in input_txt_list:
            with open(file, 'r',encoding='utf-8') as f:
                word_list = f.read().splitlines()
                input_word_set |= set(word_list)

        self.all_word_set = input_word_set

    def is_word_similar(self, word1, word2):
        if word1.lower() == word2.lower():
            return False
        if len(word1) <= 4 or len(word2) <= 4:
            return False
        dis = Levenshtein.distance(word1.lower(), word2.lower())
        if dis == 1:
            return True
        if word1 in word2 or word2 in word1:
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


class No_Root_Similar:
    def __init__(self):
        self.s_end_prefix_list = ['ex']
        self.a_prefix_list = ['a']
        self.co_prefix_list = ['co']
        self.prefix_list = ['com','con','dis','sub','pro','mis','per','pre','co','in','ex','im','en','ex','re','di','ob','ab','ad','de','un','e','a']

        cet4_txt = 'D:/github_project/make_anki_word_list/word_list/4-cet.txt'
        cet6_txt = 'D:/github_project/make_anki_word_list/word_list/6-cet.txt'
        post_txt = 'D:/github_project/make_anki_word_list/word_list/考研词汇表.txt'
        toefl_qu_txt = 'D:/github_project/make_anki_word_list/word_list/曲根10000词汇表.txt'
        toefl_red_txt = 'D:/github_project/make_anki_word_list/word_list/托福红宝书.txt'
        toefl_class = 'D:/github_project/make_anki_word_list/word_list/分类词汇.txt'
        gre300_txt = 'D:/github_project/make_anki_word_list/word_list/3000.txt'
        gre_foot_txt = 'D:/github_project/make_anki_word_list/word_list/佛脚词.txt'
        gre_red_txt = 'D:/github_project/make_anki_word_list/word_list/gre红宝书.txt'

        input_txt_list = list()
        input_txt_list.append(cet4_txt)
        input_txt_list.append(cet6_txt)
        input_txt_list.append(post_txt)
        input_txt_list.append(toefl_qu_txt)
        input_txt_list.append(toefl_red_txt)
        input_txt_list.append(toefl_class)
        input_txt_list.append(gre300_txt)
        input_txt_list.append(gre_foot_txt)
        input_txt_list.append(gre_red_txt)

        input_word_set = set()
        for file in input_txt_list:
            with open(file, 'r',encoding='utf-8') as f:
                word_list = f.read().splitlines()
                input_word_set |= set(word_list)

        self.all_word_set = input_word_set

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

    def get_similar_word_list(self, word):
        similar_list = list()
        for s in self.all_word_set:
            if self.is_word_similar(s.lower(), word.lower()) and s.lower() != word.lower():
                similar_list.append(s)
        return similar_list

    def get_similar_word_str(self, word):
        similar_words_str = ''
        for s in self.all_word_set:
            if self.is_word_similar(s.lower(), word.lower()) and s.lower() != word.lower():
                if similar_words_str != '':
                    similar_words_str += '<br>'
                similar_words_str += s
        return similar_words_str


if __name__ == '__main__':
    nrs = No_Root_Similar()
    print(nrs.is_word_similar('ascend', 'descend'))
    print(nrs.get_similar_word_str('collapse'))
    print('-------------------------')
    ds = Distance_Similar()
    # print(ds.is_word_similar('expect', 'respect'))
    print(ds.get_similar_word_str('agree'))
