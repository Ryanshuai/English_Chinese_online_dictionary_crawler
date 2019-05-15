import yaml
from similar_word import Distance_Similar
from word_root import Youdict_Root, Cigencizhui_Root
from youdict_mem import Youdict_Mem


# ####################################################### build filter list
tst_txt = 'D:/github_project/make_anki_word_list/word_list/tst.txt'
high_school_txt = 'D:/github_project/make_anki_word_list/word_list/high_school.txt'
college_cet4_txt = 'D:/github_project/make_anki_word_list/word_list/college_cet_4.txt'
college_cet6_txt = 'D:/github_project/make_anki_word_list/word_list/college_cet_6.txt'
college_post_txt = 'D:/github_project/make_anki_word_list/word_list/college_考研词汇表.txt'
toefl_qu_txt = 'D:/github_project/make_anki_word_list/word_list/曲根10000词汇表.txt'
toefl_red_txt = 'D:/github_project/make_anki_word_list/word_list/TOEFL_红宝书.txt'
toefl_class_txt = 'D:/github_project/make_anki_word_list/word_list/TOEFL_分类词汇.txt'
gre_3000_txt = 'D:/github_project/make_anki_word_list/word_list/GRE_3000.txt'
gre_foot_txt = 'D:/github_project/make_anki_word_list/word_list/GRE_佛脚词.txt'
gre_red_txt = 'D:/github_project/make_anki_word_list/word_list/GRE红宝书.txt'
gre_synonym_txt = 'D:/github_project/make_anki_word_list/word_list/GRE_synonym.txt'
internal_txt = 'D:/github_project/make_anki_word_list/word_list/internal_word.txt'
all_txt = 'D:/github_project/make_anki_word_list/word_list/all.txt'

input_txt_list = list()
input_txt_list.append(tst_txt)
input_txt_list.append(high_school_txt)
input_txt_list.append(college_cet4_txt)
input_txt_list.append(college_cet6_txt)
input_txt_list.append(college_post_txt)
input_txt_list.append(toefl_red_txt)
input_txt_list.append(toefl_class_txt)
input_txt_list.append(toefl_qu_txt)
input_txt_list.append(gre_3000_txt)
input_txt_list.append(gre_foot_txt)
input_txt_list.append(gre_red_txt)
# input_txt_list.append(gre_synonym_txt)

input_word_set = set()
for file in input_txt_list:
    with open(file, 'r',encoding='utf-8') as f:
        word_list = f.read().splitlines()
        input_word_set |= set(word_list)
print('len of input_word_set: ', len(input_word_set))

input_txt_list_2 = list()
# input_txt_list_2.append(tst_txt)
input_txt_list_2.append(high_school_txt)
# input_txt_list_2.append(college_cet4_txt)
# input_txt_list_2.append(college_cet6_txt)
# input_txt_list_2.append(college_post_txt)
# input_txt_list_2.append(toefl_qu_txt)
# input_txt_list_2.append(toefl_red_txt)
# input_txt_list_2.append(toefl_class_txt)
input_txt_list.append(gre_3000_txt)
input_txt_list_2.append(gre_foot_txt)
input_txt_list_2.append(gre_red_txt)
# input_txt_list_2.append(gre_synonym_txt)
# input_txt_list_2.append(internal_txt)

input_word_set_2 = set()
for file in input_txt_list_2:
    with open(file, 'r', encoding='utf-8') as f:
        word_list = f.read().splitlines()
        input_word_set_2 |= set(word_list)
print('len of input_word_set_2: ', len(input_word_set_2))


input_word_list = list(input_word_set_2-input_word_set)
print('input_word_set_2-input_word_set', len(input_word_set_2-input_word_set))

# ####################################################### build word list in root
cigencizhui_root = Cigencizhui_Root()
youdict_root = Youdict_Root()
youdict_mem = Youdict_Mem()
edit_distance = Distance_Similar()


# with open('pure_word_list.txt', 'w', encoding='utf-8') as f:
#     ordered_input_word_list = cigencizhui_root.put_word_list_in_order(input_word_list)
#     for word in ordered_input_word_list:
#         print(word)
#         f.write(word)
#         f.write('\n')
#

with open('output/anki_word_image_list.txt', 'w', encoding='utf-8') as f:
    # ordered_input_word_list = cigencizhui_root.put_word_list_in_order(input_word_list)
    # print('ordered_input_word_list: ', len(ordered_input_word_list))
    print('ordered_input_word_list: ', len(input_word_list))
    for word in input_word_list:
        word = word.strip()
        line = word
        for i in range(1, 11):
            line += "\\<img src=\"{}.jpg\" />".format(word+str(i))
        f.write(line)
        f.write('\n')


# with open(gre_synonym_txt, 'r', encoding='utf-8') as f:
#     word_list = f.read().splitlines()
#
# with open('output/GRE_anki_same.txt', 'w', encoding='utf-8') as f:
#     for word in word_list:
#         word = word.strip()
#         if len(word) == 0:
#             continue
#         print(word)
#         if '\u4e00' <= word[0] <= '\u9fff':
#             now_class = word
#         else:
#             line = word
#             for i in range(1, 11):
#                 line += "\\<img src=\"{}.jpg\" />".format(word + str(i))
#             line += "\\"+now_class
#             f.write(line)
#             f.write('\n')
