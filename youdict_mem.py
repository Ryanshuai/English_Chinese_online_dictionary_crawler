
class Youdict_Mem:
    def __init__(self):
        self.w_r_dict = dict()
        with open('D:/github_project/make_anki_word_list/youdict_mem/youdict_mem.txt', encoding='utf-8') as f:
            line_list = f.readlines()
            for line in line_list:
                line = line.strip()
                line = line.replace('\\', '*****', 1)
                w, r = line.split('*****')
                self.w_r_dict[w] = r

    def get_mem(self, word):
        return self.w_r_dict.get(word, '')

    def get_mem_html(self, word):
        root = self.w_r_dict.get(word, '')
        root = root.replace('\\', '<br>')
        return root


if __name__ == '__main__':
    ym = Youdict_Mem()
    print(ym.get_mem('indict'))
    # line = '13213123\\adasdasd\\fsadfasf\\123412'
    # line = line.replace('\\', '***', 1)
    # print(line)