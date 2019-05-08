
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
internal_txt = 'D:/github_project/make_anki_word_list/word_list/internal_word.txt'

input_txt_list = list()
input_txt_list.append(cet4_txt)
input_txt_list.append(cet6_txt)
input_txt_list.append(post_txt)
input_txt_list.append(toefl_qu_txt)
input_txt_list.append(toefl_red_txt)
input_txt_list.append(toefl_class)
input_txt_list.append(gre3000_txt)
input_txt_list.append(gre_foot_txt)
input_txt_list.append(gre_red_txt)
input_txt_list.append(internal_txt)

word = 'pecuniary'
for file in input_txt_list:
    with open(file, 'r', encoding='utf-8') as f:
        word_list = f.read().splitlines()
        if word in word_list:
            print(file)
