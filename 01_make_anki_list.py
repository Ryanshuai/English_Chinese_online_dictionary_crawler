import yaml
from similar_word import Distance_Similar
from youdict_root import Youdict_Root
from youdict_memrorise import Youdict_Mem


# ####################################################### build filter list
cet4_txt = 'D:/github_project/make_anki_word_list/kinds_of_word_list/4-cet.txt'
cet6_txt = 'D:/github_project/make_anki_word_list/kinds_of_word_list/6-cet.txt'
post_txt = 'D:/github_project/make_anki_word_list/kinds_of_word_list/考研词汇表.txt'
toefl_qu_txt = 'D:/github_project/make_anki_word_list/kinds_of_word_list/曲根10000词汇表.txt'
toefl_red_txt = 'D:/github_project/make_anki_word_list/kinds_of_word_list/托福红宝书.txt'
toefl_class = 'D:/github_project/make_anki_word_list/kinds_of_word_list/分类词汇.txt'
gre300_txt = 'D:/github_project/make_anki_word_list/kinds_of_word_list/3000.txt'
gre_foot_txt = 'D:/github_project/make_anki_word_list/kinds_of_word_list/佛脚词.txt'
gre_red_txt = 'D:/github_project/make_anki_word_list/kinds_of_word_list/gre红宝书.txt'

input_txt_list = list()
# input_txt_list.append(tst_txt)
# input_txt_list.append(cet4_txt)
# input_txt_list.append(cet6_txt)
# input_txt_list.append(post_txt)
# input_txt_list.append(tofle_qu_txt)
# input_txt_list.append(tofle_red_txt)
# input_txt_list.append(gre300_txt)
# input_txt_list.append(gre_foot_txt)
# input_txt_list.append(gre_red_txt)


input_word_set = set()
for file in input_txt_list:
    with open(file, 'r') as f:
        word_list = f.read().splitlines()
        input_word_set |= set(word_list)


input_txt_list_2 = list()
# input_txt_list_2.append(tst_txt)
# input_txt_list_2.append(cet4_txt)
# input_txt_list_2.append(cet6_txt)
# input_txt_list_2.append(post_txt)
input_txt_list_2.append(toefl_qu_txt)
input_txt_list_2.append(toefl_red_txt)
# input_txt_list_2.append(gre300_txt)
# input_txt_list_2.append(gre_foot_txt)
# input_txt_list_2.append(gre_red_txt)

input_word_set_2 = set()
for file in input_txt_list_2:
    with open(file, 'r') as f:
        word_list = f.read().splitlines()
        input_word_set_2 |= set(word_list)

input_word_list = list(input_word_set_2-input_word_set)
print('all:'+str(len(input_word_list)))

# ####################################################### build word list in root
root_affix = Youdict_Root()

# edit_distance = Edit_Distance()
# youdict_mem = Youdict_Mem()

# with open('anki_word_list.txt', 'w', encoding='utf-8') as f:
#     ordered_input_word_list = root_affix.put_word_list_in_order(input_word_list)
#     for word in ordered_input_word_list:
#         root = root_affix.get_root(word)
#         similar_list = edit_distance.get_distance_word_list(word)
#         mem_str = youdict_mem.get_mem(word)
#         line = word + '\\' + root + '\\'
#         for similar in similar_list:
#             line += similar + '\t'
#         line += '\\' + mem_str
#         print(line)
#         f.write(line)
#         f.write('\n')


with open('pure_word_list.txt', 'w', encoding='utf-8') as f:
    ordered_input_word_list = root_affix.put_word_list_in_order(input_word_list)
    for word in ordered_input_word_list:
        print(word)
        f.write(word)
        f.write('\n')