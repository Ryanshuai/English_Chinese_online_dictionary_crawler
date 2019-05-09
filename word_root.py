import yaml
import re


class Cigencizhui_Root:
    def __init__(self):
        with open('D:/github_project/make_anki_word_list/cigencizhui_root/root_affix.txt', encoding='utf-8') as f:
            self.ordered_root_word_list = f.read().splitlines()

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


class Etymonline_Root:
    def __init__(self):
        self.w_r_dict = dict()
        with open('D:\github_project\make_anki_word_list\etymonline_root\etymonline_root.txt', encoding='utf-8') as f:
            line_list = f.readlines()
            for line in line_list:
                line = line.strip()
                line = line.replace('\\', '*****', 1)
                w, r = line.split('*****')
                self.w_r_dict[w] = r

    def get_internal_word_list(self, root_str: str):
        pattern = re.compile(r'\(see[^-]*?\)')
        internal_word_list = pattern.findall(root_str)

        def map_fun(s):
            s = s[5:]
            w = re.findall(r'\w+', s)
            if len(w) > 0:
                return w[0]
            return []
        internal_word_list = list(map(map_fun, internal_word_list))
        return internal_word_list

    def get_root(self, word):
        return self.w_r_dict.get(word, '')

    def get_root_html(self, word):
        root = self.w_r_dict.get(word, '')
        root = root.replace('\\', '<br>')
        return root


class Youdict_Root:
    def __init__(self):
        self.w_r_dict = dict()
        with open('D:\github_project\make_anki_word_list\youdict_root\youdict_root.txt', encoding='utf-8') as f:
            line_list = f.readlines()
            for line in line_list:
                line = line.strip()
                w, r = line.split('\\')
                self.w_r_dict[w] = r

    def get_internal_word_list(self, root_str: str):
        if root_str.startswith('来自') and root_str[2:6] != 'PIE*' and ord(root_str[2]) < 128:
            temp_root = root_str[2:].split(',')[0].split('，')[0].strip()
            if '*' in temp_root:
                return ['']
            for c in temp_root:
                if ord(c) > 128:
                    return ['']
            if temp_root.endswith('-'):
                return ['']
            return [root_str[2:].split(',')[0].split('，')[0].strip()]
        else:
            return ['']

    def get_root_html(self, word):
        root = self.w_r_dict.get(word, '')
        if len(root) == 0:
            return root
        internal_word_list = self.get_internal_word_list(root)
        internal_word = internal_word_list[0]
        if len(internal_word) == 0:
            return root
        internal_word_root = self.w_r_dict.get(internal_word, '')
        return root + '<br>' + internal_word + ' ' + internal_word_root


class Yaml_Root:
    def __init__(self):
        with open('D:/github_project/make_anki_word_list/yaml_root/1 词缀词根.yaml', encoding='utf-8') as f:
            self.root_content = yaml.load(f, Loader=yaml.FullLoader)
        with open('D:/github_project/make_anki_word_list/yaml_root/2 单词列表.yaml', encoding='utf-8') as f:
            word_content = yaml.load(f, Loader=yaml.FullLoader)
            self.w_r_dict = dict()
            for word_context in word_content:
                word = word_context[0]
                root = word_context[1][0][2]
                self.w_r_dict[word] = root

    def get_root(self, word):
        return self.w_r_dict.get(word, '')

    def get_root_html(self, word):
        return self.get_root(word)


if __name__ == '__main__':
    # yr = Yaml_Root()
    # print(yr.get_root('abandon'))
    #
    # ra = Youdict_Root()
    # print(ra.get_root_html('agency'))

    all_word_list = 'D:/github_project/make_anki_word_list/word_list/all_word_list.txt'
    with open(all_word_list, 'r', encoding='utf-8') as f:
        word_list = f.read().splitlines()

    er = Etymonline_Root()
    for word in word_list:
        root_text = er.get_root(word)
        internal_word_list = er.get_internal_word_list(root_text)
        if len(internal_word_list) > 0:
            print(word, internal_word_list)