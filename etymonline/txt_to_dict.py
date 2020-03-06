import tqdm
from utils.writemdict.writemdict import MDictWriter


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

    def get_root(self, word):
        return self.w_r_dict.get(word, '')

    def get_root_html(self, word):
        root = self.w_r_dict.get(word, '')
        root = root.replace('\\', '<br>')
        return root

    def generate_dict(self, word_set):
        dictionary = dict()
        for word in tqdm(word_set, desc='Etymonline_Root.mdx'):
            mem_str = self.get_root_html(word)
            if len(mem_str) > 0:
                dictionary[word] = mem_str

        writer = MDictWriter(dictionary, title="Memory Dictionary",
                             description="Memory Dictionary from www.youdict.com")
        outfile = open("output/youdict_mem.mdx", "wb")
        writer.write(outfile)
        outfile.close()


if __name__ == '__main__':
    from utils.word_list.all_word_list import all_word_set

    dict_class = Etymonline_Root()
    dict_class.generate_dict(all_word_set)
