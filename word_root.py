import yaml


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
        with open('D:\github_project\make_anki_word_list\etymonline_root\etymonline_root.txt', encoding='utf-8') as f:
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


class Youdict_Root:
    def __init__(self):
        self.w_r_dict = dict()
        with open('D:\github_project\make_anki_word_list\youdict_root\youdict_root.txt', encoding='utf-8') as f:
            line_list = f.readlines()
            for line in line_list:
                line = line.strip()
                w, r = line.split('\\')
                self.w_r_dict[w] = r

    def from_which_word(self, root_str: str):
        if root_str.startswith('来自') and root_str[2:6] != 'PIE*' and ord(root_str[2]) < 128:
            temp_root = root_str[2:].split(',')[0].split('，')[0].strip()
            if '*' in temp_root:
                return ''
            for c in temp_root:
                if ord(c) > 128:
                    return ''
            if temp_root.endswith('-'):
                return ''
            return root_str[2:].split(',')[0].split('，')[0].strip()
        else:
            return ''

    def get_root_str_for_mdx(self, word):
        root = self.w_r_dict.get(word, '')
        if len(root) == 0:
            return root
        from_word = self.from_which_word(root)
        if len(from_word) == 0:
            return root
        from_word_root = self.w_r_dict.get(from_word, '')
        return root + '<br>' + from_word + ' ' + from_word_root


class Yaml_Root:
    def __init__(self):
        with open('D:/github_project/make_anki_word_list/yaml_root/1 词缀词根.yaml', encoding='utf-8') as f:
            self.root_content = yaml.load(f, Loader=yaml.FullLoader)
        with open('D:/github_project/make_anki_word_list/yaml_root/2 单词列表.yaml', encoding='utf-8') as f:
            word_content = yaml.load(f, Loader=yaml.FullLoader)
            self.word_dict = dict()
            for word_context in word_content:
                word = word_context[0]
                root = word_context[1][0][2]
                self.word_dict[word] = root

    def get_root(self, word):
        if word in self.word_dict:
            return self.word_dict[word]
        else:
            return ''

    def get_root_str_for_mdx(self, word):
        return self.get_root(word)

if __name__ == '__main__':
    yr = Yaml_Root()
    print(yr.get_root('abandon'))
    ra = Youdict_Root()
    print(ra.get_root_str_for_mdx('agency'))