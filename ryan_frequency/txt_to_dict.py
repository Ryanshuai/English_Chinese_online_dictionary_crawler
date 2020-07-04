from tqdm import tqdm
from utils.writemdict.writemdict import MDictWriter


class TOEFL_frequency:
    def __init__(self):
        self.w_r_dict = dict()
        with open('./TOEFL_frequency_7.0.txt', encoding='utf-8') as f:
            line_list = f.readlines()
            for line in line_list:
                line = line.strip()
                line = line.replace('\\', '*****', 1)
                w, r = line.split('*****')
                self.w_r_dict[w] = r

    def get(self, word):
        return self.w_r_dict.get(word, '')


class GRE_frequency:
    def __init__(self):
        self.w_r_dict = dict()
        with open('./GRE_frequency.txt', encoding='utf-8') as f:
            line_list = f.readlines()
            for line in line_list:
                line = line.strip()
                line = line.replace('\\', '*****', 1)
                w, r = line.split('*****')
                self.w_r_dict[w] = r

    def get(self, word):
        return self.w_r_dict.get(word, '')


if __name__ == '__main__':
    from utils.word_list.all_words_list import all_words_list

    txt2dict = TOEFL_frequency()
    dictionary = dict()
    for word in tqdm(all_words_list, desc='TOEFL_frequency.mdx'):
        mem_str = txt2dict.get(word)
        if len(mem_str) > 0:
            dictionary[word] = mem_str

    writer = MDictWriter(dictionary, title="TOEFL_frequency", description="TOEFL_frequency")
    with open("../output_mdx/TOEFL_frequency.mdx", "wb") as f:
        writer.write(f)

    txt2dict = GRE_frequency()
    dictionary = dict()
    for word in tqdm(all_words_list, desc='GRE_frequency.mdx'):
        mem_str = txt2dict.get(word)
        if len(mem_str) > 0:
            dictionary[word] = mem_str

    writer = MDictWriter(dictionary, title="GRE_frequency", description="GRE_frequency")
    with open("../output_mdx/GRE_frequency.mdx", "wb") as f:
        writer.write(f)
