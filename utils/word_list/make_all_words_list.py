import os

txt_dir = "./word_list_txt"

all_set = set()
for txt in os.listdir(txt_dir):
    file = os.path.join(txt_dir, txt)
    with open(file, encoding='utf-8') as f:
        file_set = set(f.read().splitlines())
        all_set |= file_set


def make_all_list():
    with open('all_words_list.py', 'w', encoding='utf-8') as f:
        f.write('all_words_list = [')
        for word in all_set:
            if len(word) <= 1:
                continue
            f.write('"')
            f.write(word)
            f.write('",\n')
        f.write(']')


if __name__ == '__main__':
    make_all_list()
