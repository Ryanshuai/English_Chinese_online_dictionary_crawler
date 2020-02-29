import yaml
import re


class Etymonline_Root:
    def __init__(self):
        self.w_r_dict = dict()
        with open('/etymonline/etymonline_root\etymonline_root.txt', encoding='utf-8') as f:
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


class Youdict_Root:
    def __init__(self):
        self.w_r_dict = dict()
        with open('/quword/youdict_root\youdict_root.txt', encoding='utf-8') as f:
            line_list = f.readlines()
            for line in line_list:
                line = line.strip()
                w, r = line.split('\\')
                self.w_r_dict[w] = r

    def get_internal_word_set(self, root_str: str):
        if root_str.startswith('来自') and root_str[2:6] != 'PIE*' and ord(root_str[2]) < 128:
            temp_root = root_str[2:].split(',')[0].split('，')[0].strip()
            if '*' in temp_root:
                return set('')
            for c in temp_root:
                if ord(c) > 128:
                    return set('')
            if temp_root.endswith('-'):
                return set('')
            return {temp_root}
        else:
            return set('')

    def get_root_html(self, word):
        root = self.w_r_dict.get(word, '')
        if '词源不详。' in root:
            return ''
        return root


class Yaml_Root:
    def __init__(self):
        self.prefix_explain_dict = dict()
        self.root_explain_dict = dict()
        self.suffix_explain_dict = dict()
        with open('D:/github_project/make_anki_word_list/yaml_root/1 词缀词根.yaml', encoding='utf-8') as f:
            all_prefix_root_suffix = yaml.load(f, Loader=yaml.FullLoader)
            for prs_content in all_prefix_root_suffix:
                cls = prs_content[0]
                prs = prs_content[1]
                explain = prs_content[2]
                if cls == '前缀':
                    self.prefix_explain_dict[prs] = explain
                elif cls == '词根':
                    self.root_explain_dict[prs] = explain
                elif cls == '后缀':
                    self.suffix_explain_dict[prs] = explain
                else:
                    raise Exception(cls)

        with open('D:/github_project/make_anki_word_list/yaml_root/2 单词列表.yaml', encoding='utf-8') as f:
            word_content = yaml.load(f, Loader=yaml.FullLoader)
            self.w_r_dict = dict()
            for word_context in word_content:
                word = word_context[0]
                root = word_context[1][0][2]
                self.w_r_dict[word] = root

    def get_possible_prefix_root_suffix_html(self, word: str):
        html_str = ''
        for prefix in self.prefix_explain_dict:
            if word.startswith(prefix):
                html_str += '前缀: ' + prefix + ': \t' + self.prefix_explain_dict[prefix]
                html_str += '<br>'
        for root in self.root_explain_dict:
            if root in word:
                html_str += '词根: ' + root + ': \t' + self.root_explain_dict[root]
                html_str += '<br>'
        for suffix in self.suffix_explain_dict:
            if word.startswith(suffix):
                html_str += '前缀: ' + suffix + ': \t' + self.suffix_explain_dict[suffix]
                html_str += '<br>'
        return html_str

    def get_root(self, word):
        return self.w_r_dict.get(word, '')

    def get_root_html(self, word):
        return self.get_root(word)


class Assembled_Root:
    def __init__(self):
        self.youdict_root = Youdict_Root()
        self.yaml_root = Yaml_Root()
        self.etymonline_root = Etymonline_Root()
        self.cigencizhui_root = Cigencizhui_Root()

    def get_first_useful(self, a):
        a = list(filter(lambda x: len(x) > 0, a))
        a.append('')
        return a[0]

    def get_all_kind_root_html(self, word):
        youdict_root_html = self.youdict_root.get_root_html(word)
        yaml_root_html = self.yaml_root.get_root_html(word)
        etymonline_root_html = self.etymonline_root.get_root_html(word)
        yaml_possible_root_html = self.yaml_root.get_possible_prefix_root_suffix_html(word)
        return youdict_root_html, yaml_root_html, etymonline_root_html, yaml_possible_root_html

    def get_internal_word_set(self, root_htmls):
        youdict_root_html = root_htmls[0]
        etymonline_root_html = root_htmls[2]
        internal_word_set = self.youdict_root.get_internal_word_set(youdict_root_html)
        internal_word_set |= self.etymonline_root.get_internal_word_set(etymonline_root_html)
        return internal_word_set

    def get_root_html(self, word):
        root_htmls = self.get_all_kind_root_html(word)
        internal_word_set = self.get_internal_word_set(root_htmls)
        internal_word_set.discard(word)
        html_str = ''
        if len(self.get_first_useful(root_htmls)) > 0:
            html_str += word + ': ' + self.get_first_useful(root_htmls)
        for internal_word in internal_word_set:
            root_html = self.get_first_useful(self.get_all_kind_root_html(internal_word))
            html_str += '<br>' + 2*len(word)*'&nbsp;'
            # html_str += '\n' + len(word)*' '
            html_str += '|--- ' + internal_word + ': ' + root_html
        return html_str


if __name__ == '__main__':
    # yr = Yaml_Root()
    # print(yr.get_possible_prefix_root_suffix_html('pleistocene'))
    # print(yr.get_root('abandon'))
    # print(yr.suffix_explain_dict['-sive'])
    #
    # ra = Youdict_Root()
    # print(ra.get_root_html('algae'))
    #
    # all_word_list = 'D:/github_project/make_anki_word_list/word_list/all.txt'
    # with open(all_word_list, 'r', encoding='utf-8') as f:
    #     word_list = f.read().splitlines()
    #
    # er = Etymonline_Root()
    # for word in word_list:
    #     root_text = er.get_root(word)
    #     internal_word_set = er.get_internal_word_set(root_text)
        # if len(internal_word_set) > 0:
        #     print(word, internal_word_set)

    # word_list = ['countermand', 'counterpart', 'zippy']
    word_list = ['pleistocene']
    ar = Assembled_Root()
    for word in word_list:
        root_text = ar.get_root_html(word)
        print(root_text)
        # internal_word_set = ar.get_internal_word_set(*ar.get_all_kind_root_html(word))
        # print(internal_word_set)

