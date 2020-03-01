import yaml


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
