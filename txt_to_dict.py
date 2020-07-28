from tqdm import tqdm
from utils.writemdict.writemdict import MDictWriter


class Backslash_Txt_Dict:
    def __init__(self, txt_path, dictionary_name, dictionary_description=None):
        self.dictionary_name = dictionary_name
        self.dictionary_description = dictionary_description if dictionary_description else dictionary_name

        self.word_value_dict = dict()
        with open(txt_path, encoding='utf-8') as f:
            line_list = f.readlines()
            for line in line_list:
                line = line.strip()
                line = line.replace('\\', '*****', 1)
                w, r = line.split('*****')
                self.word_value_dict[w] = r

    def get_value(self, word):
        return self.word_value_dict.get(word, '')

    def get_value_html(self, word):
        value = self.word_value_dict.get(word, '')
        value = value.replace('\\', '<br>')
        return value

    def generate_dict(self, word_set):
        dictionary = dict()
        for word in tqdm(word_set, desc=self.dictionary_name):
            mem_str = self.get_value_html(word)
            if len(mem_str) > 0:
                dictionary[word] = mem_str

        writer = MDictWriter(dictionary, title=self.dictionary_name, description=self.dictionary_description)
        with open("../output_mdx/" + self.dictionary_name, "wb") as f:
            writer.write(f)
