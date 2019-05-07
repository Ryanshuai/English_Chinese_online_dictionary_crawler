import requests
from PIL import Image
from io import BytesIO
from concurrent.futures import ThreadPoolExecutor
import urllib.request
import os


def get_image_from_url(url):
    response = requests.get(url)
    image = Image.open(BytesIO(response.content))
    return image


def save_word_image_to_dir(name, di='youdict_word_images/'):

    url = 'http://www.youdict.com/images/words/' + name + '.jpg'
    image_name = name + '.jpg'
    image = get_image_from_url(url)
    # print('saving>>>>>>\t', di+image_name)
    image.convert('RGB').save(di+image_name)


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
    input_txt_list.append(cet4_txt)
    input_txt_list.append(cet6_txt)
    input_txt_list.append(post_txt)
    input_txt_list.append(toefl_qu_txt)
    input_txt_list.append(toefl_red_txt)
    input_txt_list.append(gre3000_txt)
    input_txt_list.append(gre_foot_txt)
    input_txt_list.append(gre_red_txt)

    input_word_set = set()
    for file in input_txt_list:
        with open(file, 'r') as f:
            word_list = f.read().splitlines()
            input_word_set |= set(word_list)

    input_word_set = sorted(input_word_set, key=str.lower, reverse=True)

    input_word_set_2 = set()
    input_txt_list.clear()
    input_txt_list.append(gre_class_txt)
    for file in input_txt_list:
        with open(file, 'r', encoding='utf-8') as f:
            word_list = f.read().splitlines()
            input_word_set_2 |= set(word_list)

    word_list = list(input_word_set_2 - set(input_word_set))
    print('download image for {} word'.format(len(word_list)))

    # for word in word_list:
    #     save_word_image_to_dir(word)
    # save_word_image_to_dir('dictator')

    pool = ThreadPoolExecutor(10000)
    for word in word_list:
        word = word.strip()
        for i in range(1, 11):
            name = word+str(i)
            if not os.path.exists('youdict_word_images/'+name+'.jpg'):
                print(name)
                # save_word_image_to_dir(word)
                a = pool.submit(save_word_image_to_dir, name)

