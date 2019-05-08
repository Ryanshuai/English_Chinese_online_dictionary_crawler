import make_all_list
import re
import os
from tqdm import tqdm
from word2url2html import get_html_from_url
from concurrent.futures import ThreadPoolExecutor


def is_longer_than_one(x):
    return len(x) > 2


def thread_process(word, to_dir='etymonline_html_text/'):
    to_txt = to_dir + word + '.txt'
    if not os.path.exists(to_txt):
        print('get html and save txt', word)
        url = 'https://www.youdict.com/w/' + word
        html_text = get_html_from_url(url)
        with open(to_txt, 'w', encoding='utf-8') as f:
            f.write(html_text)


def multi_thread_check_and_save(word_list):
    pool = ThreadPoolExecutor(100)
    for word in tqdm(word_list, desc='checking absent word'):
        if word == 'con':
            continue
        a = pool.submit(thread_process, word)


if __name__ == '__main__':
    html_text_dir = 'D:\github_project\make_anki_word_list\youdict_word_html'
    image_dir = 'D:\github_project\make_anki_word_list\youdict_word_images'

    all_word_txt = 'D:/github_project/make_anki_word_list/word_list/all_word_list.txt'
    with open(all_word_txt, 'r', encoding='utf-8') as f:
        word_list = f.read().splitlines()

    def is_longer_than_one(x):
        return len(x) > 2 and x != 'con'

    word_list = filter(is_longer_than_one, word_list)
    word_list = map(str.strip, word_list)
    word_list = sorted(word_list, key=str.lower)

    # check and save html #########################################################################################
    multi_thread_check_and_save(word_list)

    # update txt ##################################################################################################
    # root_line_list = list()
    # mem_line_list = list()
    # for word in tqdm(word_list, desc='decoding'):
    #     if word == 'con':
    #         continue
    #     html_text_path = html_text_dir + '\\' + word + '.txt'
    #     with open(html_text_path, 'r', encoding='utf-8') as f:
    #         html_txt = f.read()
    #     root_txt = get_root_txt_from_html_text(html_txt)
    #     mem_txt = get_mem_txt_from_html_text(html_txt)
    #     root_line_list.append(word+'\\'+root_txt)
    #     mem_line_list.append(word+'\\'+mem_txt)
    #     # print('----------------------')
    #     # print(word)
    #     # print(word+'\\'+root_txt)
    #     # print(word+'\\'+mem_txt)
    #
    #
    # to_txt = 'D:\github_project\make_anki_word_list\youdict_root\youdict_root.txt'
    # with open(to_txt, 'w', encoding='utf-8') as f:
    #     for line in root_line_list:
    #         f.write(line)
    #         f.write('\n')
    #
    # to_txt = 'D:\github_project\make_anki_word_list\youdict_mem\youdict_mem.txt'
    # with open(to_txt, 'w', encoding='utf-8') as f:
    #     for line in mem_line_list:
    #         f.write(line)
    #         f.write('\n')
    #

