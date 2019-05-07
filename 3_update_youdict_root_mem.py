import make_all_list
import os
from tqdm import tqdm
from word2url2html2txt import get_root_txt_from_html_text, get_mem_txt_from_html_text, get_word_html_text_from_web
from concurrent.futures import ThreadPoolExecutor


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


def is_longer_than_one(x):
    return len(x) > 2


def multi_thread_check_and_save(word_list):
    pool = ThreadPoolExecutor(100)
    for word in tqdm(word_list, desc='checking absent word'):
        if word == 'con':
            continue
        word = word.strip()
        to_txt = 'youdict_word_html/'+word+'.txt'
        if not os.path.exists(to_txt):
            print(word)
            a = pool.submit(get_word_html_text_from_web, word)
        else:
            with open(to_txt, 'r', encoding='utf-8') as f:
                txt = f.read()
            if not txt.startswith('<!DOCTYPE html>'):
                print(word)
                a = pool.submit(get_word_html_text_from_web, word)


if __name__ == '__main__':
    html_text_dir = 'D:\github_project\make_anki_word_list\youdict_word_html'
    image_dir = 'D:\github_project\make_anki_word_list\youdict_word_images'

    all_word_txt = 'D:/github_project/make_anki_word_list/word_list/all_word_list.txt'
    with open(all_word_txt, 'r', encoding='utf-8') as f:
        word_list = f.read().splitlines()

    word_list = filter(is_longer_than_one, word_list)
    word_list = map(str.strip, word_list)
    word_list = sorted(word_list, key=str.lower)

    # check ###########################################################################################################
    multi_thread_check_and_save(word_list)

    # ###########################################################################################################
    root_line_list = list()
    mem_line_list = list()
    internal_word_set = set()
    for word in tqdm(word_list, desc='decoding'):
        if word == 'con':
            continue
        html_text_path = html_text_dir + '\\' + word + '.txt'
        with open(html_text_path, 'r', encoding='utf-8') as f:
            html_txt = f.read()
        root_txt = get_root_txt_from_html_text(html_txt)
        internal_word = find_internal_word_from_youdict_root_str(root_txt)
        if len(internal_word) > 0:
            if internal_word[-1] == '.':
                internal_word = internal_word[:-1]
            tqdm.write(internal_word)
            internal_word_set.add(internal_word)
        mem_txt = get_mem_txt_from_html_text(html_txt)
        root_line_list.append(word+'\\'+root_txt)
        mem_line_list.append(word+'\\'+mem_txt)
        # print('----------------------')
        # print(word)
        # print(word+'\\'+root_txt)
        # print(word+'\\'+mem_txt)

    internal_word_list = list(internal_word_set)
    with open('D:\github_project\make_anki_word_list\word_list\internal_word.txt', 'w', encoding='utf-8') as f:
        for word in tqdm(internal_word_list, desc='saving internal'):
            if word == 'con':
                continue
            f.write(word)
            f.write('\n')

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


