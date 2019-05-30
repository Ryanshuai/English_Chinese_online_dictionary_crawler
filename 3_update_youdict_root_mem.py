
import os
from os.path import normpath, join, exists
from tqdm import tqdm
from word2url2html import multi_thread, save_if_not_exist_for_youdict, one_thread_check_and_save
from html2txt import get_mem_txt_from_youdict_html_text, get_root_txt_from_youdict_html_text


if __name__ == '__main__':
    html_text_dir = 'D:/github_project/make_anki_word_list/youdict_html_text'

    all_word_list = 'D:/github_project/make_anki_word_list/word_list/all.txt'
    with open(all_word_list, encoding='utf-8') as f:
        word_list = f.read().splitlines()
    word_set = set(word_list)
    word_set.discard('con')

    # check and save html #########################################################################################
    # multi_thread(save_if_not_exist_for_youdict, word_set, 'https://www.youdict.com/w/', 'youdict_html_text/')
    one_thread_check_and_save(save_if_not_exist_for_youdict, word_set, 'https://www.youdict.com/w/', 'youdict_html_text/')

    # update txt ###################################################################################################
    root_line_list = list()
    mem_line_list = list()
    for word_txt in tqdm(os.listdir(html_text_dir), desc='decoding'):
        print(word_txt)
        html_text_path = normpath(join(html_text_dir, word_txt))
        with open(html_text_path, encoding='utf-8') as f:
            html_txt = f.read()
        if not html_txt.startswith('<!DOCTYPE html>'):
            os.remove(html_text_path)
            continue
        root_txt = get_root_txt_from_youdict_html_text(html_txt)
        mem_txt = get_mem_txt_from_youdict_html_text(html_txt)
        root_line_list.append(word_txt.split('.')[0]+'\\'+root_txt)
        mem_line_list.append(word_txt.split('.')[0]+'\\'+mem_txt)
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
    #
    #
