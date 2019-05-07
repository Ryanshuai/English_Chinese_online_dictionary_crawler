from tqdm import tqdm
from url2html2txt import get_root_txt, get_mem_txt


def find_from_which_word_from_youdict_root_str(root_str: str):
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


if __name__ == '__main__':
    html_txt_dir = 'D:\github_project\make_anki_word_list\youdict_word_html'
    image_dir = 'D:\github_project\make_anki_word_list\youdict_word_images'

    all_word_txt = 'D:/github_project/make_anki_word_list/word_list/all_word_list.txt'
    with open(all_word_txt, 'r', encoding='utf-8') as f:
        word_list = f.read().splitlines()

    word_list = filter(is_longer_than_one, word_list)
    word_list = map(str.strip, word_list)
    word_list = sorted(word_list, key=str.lower)

    # check ###########################################################################################################
    check_list = list()
    for word in tqdm(word_list, desc='checking'):
        # print(word)
        if word == 'con':
            continue
        html_txt_path = html_txt_dir + '\\' + word + '.txt'
        with open(html_txt_path, 'r', encoding='utf-8') as f:
            html_txt = f.read()
        if not html_txt.startswith('<!DOCTYPE html>'):
            check_list.append(word)
    if len(check_list) > 0:
        raise Exception('wrong html list:', check_list)


    # # ###########################################################################################################
    root_line_list = list()
    mem_line_list = list()
    for word in tqdm(word_list, desc='decoding'):
        if word == 'con':
            continue
        html_txt_path = html_txt_dir + '\\' + word + '.txt'
        with open(html_txt_path, 'r', encoding='utf-8') as f:
            html_txt = f.read()
        root_txt = get_root_txt(html_txt)
        from_word = find_from_which_word_from_youdict_root_str(root_txt)
        word_list.append(from_word)
        mem_txt = get_mem_txt(html_txt)
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


