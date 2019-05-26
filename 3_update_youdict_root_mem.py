from make_all_internal_list import make_all_list
from tqdm import tqdm
from word2url2html import multi_thread, save_if_not_exist
from html2txt import get_mem_txt_from_youdict_html_text, get_root_txt_from_youdict_html_text


if __name__ == '__main__':
    html_text_dir = 'D:/github_project/make_anki_word_list/youdict_word_html'

    all_word_list = 'D:/github_project/make_anki_word_list/word_list/all.txt'
    with open(all_word_list, 'r', encoding='utf-8') as f:
        word_list = f.read().splitlines()
    word_set = set(word_list)
    word_set.discard('con')

    # check and save html #########################################################################################
    multi_thread(save_if_not_exist, word_set, 'https://www.youdict.com/w/', 'youdict_html_text/')

    # # update txt ###################################################################################################
    # root_line_list = list()
    # mem_line_list = list()
    # for word in tqdm(word_set, desc='decoding'):
    #     html_text_path = html_text_dir + '/' + word + '.txt'
    #     with open(html_text_path, encoding='utf-8') as f:
    #         html_txt = f.read()
    #     root_txt = get_root_txt_from_youdict_html_text(html_txt)
    #     mem_txt = get_mem_txt_from_youdict_html_text(html_txt)
    #     root_line_list.append(word+'\\'+root_txt)
    #     mem_line_list.append(word+'\\'+mem_txt)
    #     # print('----------------------')
    #     # print(word)
    #     # print(word+'\\'+root_txt)
    #     # print(word+'\\'+mem_txt)
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


