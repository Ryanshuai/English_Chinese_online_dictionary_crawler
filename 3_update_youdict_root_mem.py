import make_all_internal_list
import re
import os
from tqdm import tqdm
from word2url2html import get_html_from_url
from html2txt import get_mem_txt_from_youdict_html_text, get_root_txt_from_youdict_html_text
from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED


def find_internal_word_from_youdict_root_str(root_str: str):
    if root_str.startswith('来自') and root_str[2:6] != 'PIE*' and ord(root_str[2]) < 128:
        temp_root = root_str[2:].split(',')[0].split('，')[0].strip()
        if '*' in temp_root:
            return ''
        for c in temp_root:
            if ord(c) > 128:
                return ''
        if temp_root.endswith('-'):
            return ''
        return root_str[2:].split(',')[0].split('，')[0].strip()
    else:
        return ''


def thread_process(word, from_web, to_dir):
    to_txt = to_dir + word + '.txt'
    if not os.path.exists(to_txt):
        print(word)
        url = from_web + word
        html_text = get_html_from_url(url)
        with open(to_txt, 'w', encoding='utf-8') as f:
            f.write(html_text)


def multi_thread_check_and_save(word_set):
    executor = ThreadPoolExecutor(max_workers=100)
    all_task = [executor.submit(thread_process, word, 'https://www.youdict.com/w/', 'youdict_html_text/',)
                for word in word_set]
    wait(all_task, return_when=ALL_COMPLETED)


if __name__ == '__main__':
    html_text_dir = 'D:\github_project\make_anki_word_list\youdict_word_html'

    all_word_list = 'D:/github_project/make_anki_word_list/word_list/all.txt'
    with open(all_word_list, 'r', encoding='utf-8') as f:
        word_list = f.read().splitlines()
    word_set = set(word_list)
    word_set.remove('con')

    # check and save html #########################################################################################
    multi_thread_check_and_save(word_set)

    # update txt ###################################################################################################
    root_line_list = list()
    mem_line_list = list()
    for word in tqdm(word_set, desc='decoding'):
        html_text_path = html_text_dir + '\\' + word + '.txt'
        with open(html_text_path, 'r', encoding='utf-8') as f:
            html_txt = f.read()
        root_txt = get_root_txt_from_youdict_html_text(html_txt)
        mem_txt = get_mem_txt_from_youdict_html_text(html_txt)
        root_line_list.append(word+'\\'+root_txt)
        mem_line_list.append(word+'\\'+mem_txt)
        # print('----------------------')
        # print(word)
        # print(word+'\\'+root_txt)
        # print(word+'\\'+mem_txt)


    to_txt = 'D:\github_project\make_anki_word_list\youdict_root\youdict_root.txt'
    with open(to_txt, 'w', encoding='utf-8') as f:
        for line in root_line_list:
            f.write(line)
            f.write('\n')

    to_txt = 'D:\github_project\make_anki_word_list\youdict_mem\youdict_mem.txt'
    with open(to_txt, 'w', encoding='utf-8') as f:
        for line in mem_line_list:
            f.write(line)
            f.write('\n')


