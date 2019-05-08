import make_all_list
import re
import os
from tqdm import tqdm
from word2url2html import get_html_from_url
from html2txt import get_root_txt_from_etymonline_html_text
from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED


def thread_process(word, from_web, to_dir):
    to_txt = to_dir + word + '.txt'
    if not os.path.exists(to_txt):
        print('get html and save txt: ', word)
        url = from_web + word
        html_text = get_html_from_url(url)
        with open(to_txt, 'w', encoding='utf-8') as f:
            f.write(html_text)


def one_thread_check_and_save(word_list):
    [thread_process(word, 'https://www.etymonline.com/search?q=', 'etymonline_html_text/',) for word in word_list]


def multi_thread_check_and_save(word_list):
    executor = ThreadPoolExecutor(max_workers=100)
    all_task = [executor.submit(thread_process, word, 'https://www.etymonline.com/search?q=', 'etymonline_html_text/')
                for word in tqdm(word_list)]
    wait(all_task, return_when=ALL_COMPLETED)


if __name__ == '__main__':
    from_html_text_dir = 'D:\github_project\make_anki_word_list\etymonline_html_text'
    save_to_txt = 'D:\github_project\make_anki_word_list\etymonline_root\etymonline_root.txt'

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
    # one_thread_check_and_save(word_list)

    # update txt ##################################################################################################
    # root_line_list = list()
    # for word in tqdm(word_list, desc='decoding'):
    #     html_text_path = from_html_text_dir + '\\' + word + '.txt'
    #     with open(html_text_path, 'r', encoding='utf-8') as f:
    #         html_txt = f.read()
    #     root_txt = get_root_txt_from_etymonline_html_text(html_txt)
    #     root_line_list.append(word+'\\'+root_txt)
    #
    # with open(save_to_txt, 'w', encoding='utf-8') as f:
    #     for line in root_line_list:
    #         f.write(line)
    #         f.write('\n')



