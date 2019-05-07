from tqdm import tqdm
from writemdict.writemdict import MDictWriter
from PIL import Image
import io
import os


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
input_txt_list.append(tst_txt)
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
    with open(file, 'r',encoding='utf-8') as f:
        word_list = f.read().splitlines()
        for word in word_list:
            word = word.strip()
            input_word_set.add(word)

word_list = list(input_word_set)
word_list = sorted(word_list, key=str.lower)

with open('D:/github_project/make_anki_word_list/word_list/all_word_list.txt', 'w',encoding='utf-8') as f:
    for word in word_list:
        f.write(word)
        f.write('\n')
