
from word_list.all_word_list import *


t = 'march'
t = t.strip()
for key, v_set in word_set_dict.items():
    for word in v_set:
        if t in word:
            print(word, '\tis in list: ',key)

print('=====================================================================')
root = 'archaeo'
word = word.strip()
with open(all_txt, 'r', encoding='utf-8') as f:
    word_list = f.read().splitlines()
for word in word_list:
    if root in word:
        print(word, '\thas root:\t', root)

print('=====================================================================')
suffix = 'ssss'
with open(all_txt, 'r', encoding='utf-8') as f:
    word_list = f.read().splitlines()
for word in word_list:
    if word.endswith(suffix):
        print(word, '\thas suffix:\t', suffix)
