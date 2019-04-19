
class Cigencizhui_Root:
    def __init__(self):
        self.w_r_dict = dict()
        with open('D:/github_project/make_anki_word_list/affix/root_affix.txt', encoding='utf-8') as f:
            self.ordered_root_word_list = f.read().splitlines()
        with open('D:/github_project/make_anki_word_list/affix/root_affix_with_root_cleared.txt', encoding='utf-8') as f:
            line_list = f.readlines()
            for line in line_list:
                line = line.strip()
                w, r = line.split('\\')
                self.w_r_dict[w] = r

    def get_root(self, word):
        if word in self.w_r_dict:
            return self.w_r_dict[word]
        else:
             return ''

    def put_word_list_in_order(self, filter_word_list):
        not_seen_word_list = filter_word_list.copy()
        res_word_list = list()
        for root_word in self.ordered_root_word_list:
            if root_word in filter_word_list:
                res_word_list.append(root_word)
                if root_word in not_seen_word_list:
                    not_seen_word_list.remove(root_word)
        print(len(not_seen_word_list))
        return res_word_list


if __name__ == '__main__':
    ra = Youdict_Root()
    print()