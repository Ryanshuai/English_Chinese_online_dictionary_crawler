from tqdm import tqdm
from utils.writemdict.writemdict import MDictWriter


class Youdict_Mem:
    def __init__(self):
        self.w_r_dict = dict()
        with open('/quword/youdict_mem/quword_mem.txt', encoding='utf-8') as f:
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


youdict_mem = Youdict_Mem()
dictionary = dict()
for word in tqdm(word_set, desc='youdict_mem.mdx'):
    mem_str = youdict_mem.get_mem_html(word)
    if len(mem_str) > 0:
        dictionary[word] = mem_str

writer = MDictWriter(dictionary, title="Memory Dictionary", description="Memory Dictionary from www.youdict.com")
outfile = open("output/youdict_mem.mdx", "wb")
writer.write(outfile)
outfile.close()
