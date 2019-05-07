import os
import eventlet
from concurrent.futures import ThreadPoolExecutor
import requests

eventlet.monkey_patch()


def get_html(url, ip=None):
    if ip is None:
        head = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}  ##浏览器请求头（大部分网站没有这个请求头会报错、请务必加上哦）
        html = requests.get(url, headers=head, verify=False)
        html.encoding = 'utf-8'
        return html
    else:
        proxy = {'http': ip}
        head = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}  ##浏览器请求头（大部分网站没有这个请求头会报错、请务必加上哦）
        html = requests.get(url, headers=head, verify=False, proxies=proxy)
        html.encoding = 'utf-8'
    # p = requests.get('http://icanhazip.com', headers=head, proxies=proxy)
    # print('------------------------')
    # print(p.text)
    return html


def save_word_html_to_dir(word, di='youdict_word_html/'):
    base_url = 'https://www.youdict.com/w/'
    url = base_url + word
    html = get_html(url)
    # print(html.text)

    to_txt = di+word+'.txt'
    with open(to_txt, 'w', encoding='utf-8') as f:
        f.write(html.text)
        f.write('\n')


if __name__ == '__main__':
    # ####################################################### build filter list
    tst_txt = 'D:/github_project/make_anki_word_list/word_list/tst.txt'
    cet4_txt = 'D:/github_project/make_anki_word_list/word_list/4-cet.txt'
    cet6_txt = 'D:/github_project/make_anki_word_list/word_list/6-cet.txt'
    post_txt = 'D:/github_project/make_anki_word_list/word_list/考研词汇表.txt'
    toefl_qu_txt = 'D:/github_project/make_anki_word_list/word_list/曲根10000词汇表.txt'
    toefl_red_txt = 'D:/github_project/make_anki_word_list/word_list/托福红宝书.txt'
    toefl_class = 'D:/github_project/make_anki_word_list/word_list/分类词汇.txt'
    gre3000_txt = 'D:/github_project/make_anki_word_list/word_list/3000.txt'
    gre_foot_txt = 'D:/github_project/make_anki_word_list/word_list/佛脚词.txt'
    gre_red_txt = 'D:/github_project/make_anki_word_list/word_list/gre红宝书.txt'
    gre_class_txt = 'D:/github_project/make_anki_word_list/word_list/GRE_synonym.txt'

    input_txt_list = list()
    # input_txt_list.append(cet4_txt)
    # input_txt_list.append(cet6_txt)
    # input_txt_list.append(post_txt)
    # input_txt_list.append(toefl_qu_txt)
    # input_txt_list.append(toefl_red_txt)
    # input_txt_list.append(gre300_txt)
    # input_txt_list.append(gre_foot_txt)
    # input_txt_list.append(gre_red_txt)
    # input_txt_list.append(gre_class_txt)

    input_word_set = set()
    for file in input_txt_list:
        with open(file, 'r') as f:
            word_list = f.read().splitlines()
            input_word_set |= set(word_list)
    input_word_set = sorted(input_word_set, key=str.lower, reverse=True)

    input_txt_list_2 = list()
    input_txt_list_2.append(cet4_txt)
    input_txt_list_2.append(cet6_txt)
    input_txt_list_2.append(post_txt)
    input_txt_list_2.append(toefl_qu_txt)
    input_txt_list_2.append(toefl_red_txt)
    input_txt_list_2.append(gre3000_txt)
    input_txt_list_2.append(gre_foot_txt)
    input_txt_list_2.append(gre_red_txt)
    input_txt_list_2.append(gre_class_txt)

    input_word_set_2 = set()
    for file in input_txt_list_2:
        with open(file, 'r', encoding='utf-8') as f:
            word_list = f.read().splitlines()
            input_word_set_2 |= set(word_list)
    input_word_set_2 = sorted(input_word_set_2, key=str.lower, reverse=True)

    word_list = list(set(input_word_set_2) - set(input_word_set))
    print('download html for {} word'.format(len(word_list)))

    # word_list = ['copious']
    # for word in word_list:
    #     save_word_html_to_dir(word)

    pool = ThreadPoolExecutor(100)
    for word in word_list:
        word = word.strip()
        to_txt = 'youdict_word_html/'+word+'.txt'
        if not os.path.exists(to_txt):
            print(word)
            a = pool.submit(save_word_html_to_dir, word)
        else:
            with open(to_txt, 'r', encoding='utf-8') as f:
                txt = f.read()
            if not txt.startswith('<!DOCTYPE html>'):
                print(word)
                a = pool.submit(save_word_html_to_dir, word)
