import re


class Etymonline_Root:
    def __init__(self):
        self.w_r_dict = dict()
        with open('etymonline/etymonline_root.txt', encoding='utf-8') as f:
            line_list = f.readlines()
            for line in line_list:
                line = line.strip()
                line = line.replace('\\', '*****', 1)
                w, r = line.split('*****')
                self.w_r_dict[w] = r

    def get_internal_word_set(self, root_str: str):
        pattern = re.compile(r'\(see [^-]*?\)')
        internal_word_list = pattern.findall(root_str)

        pattern = re.compile(r'[^(]see \w+')
        internal_word_list2 = pattern.findall(root_str)

        # pattern = re.compile(r'from \w+')
        # internal_word_list3 = pattern.findall(root_str)
        # if len(internal_word_list3):
        #     print(internal_word_list3)

        def map_fun(s):
            s = s[5:]
            w = re.findall(r'\w+', s)
            if len(w) > 0:
                return w[0]
            return []

        internal_word_set = set(map(map_fun, internal_word_list + internal_word_list2))
        return internal_word_set

    def get_root(self, word):
        return self.w_r_dict.get(word, '')

    def get_root_html(self, word):
        root = self.w_r_dict.get(word, '')
        root = root.replace('\\', '<br>')
        return root
