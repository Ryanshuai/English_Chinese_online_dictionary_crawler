class Cigencizhui_Root:
    def __init__(self):
        with open('D:/github_project/make_anki_word_list/cigencizhui_root/root_affix.txt', encoding='utf-8') as f:
            self.ordered_root_word_list = f.read().splitlines()

    def put_word_list_in_order(self, word_list):
        not_seen_word_list = word_list.copy()
        res_word_list = list()
        for root_word in self.ordered_root_word_list:
            if root_word in word_list:
                res_word_list.append(root_word)
                if root_word in not_seen_word_list:
                    not_seen_word_list.remove(root_word)
        # print(len(not_seen_word_list))
        return res_word_list
