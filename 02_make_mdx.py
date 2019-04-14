import yaml
from tqdm import tqdm
from similar_word import Distance_Similar, No_Root_Similar
from yaml_root import Yaml_Root
from youdict_root import Youdict_Root
from youdict_memrorise import Youdict_Mem
from writemdict.writemdict import MDictWriter


# ####################################################### build filter list
tst_txt = 'D:/github_project/make_anki_word_list/kinds_of_word_list/tst.txt'
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
input_txt_list.append(tst_txt)
input_txt_list.append(cet4_txt)
input_txt_list.append(cet6_txt)
input_txt_list.append(post_txt)
input_txt_list.append(toefl_qu_txt)
input_txt_list.append(toefl_red_txt)
input_txt_list.append(gre300_txt)
input_txt_list.append(gre_foot_txt)
input_txt_list.append(gre_red_txt)


input_word_set = set()
for file in input_txt_list:
    with open(file, 'r') as f:
        word_list = f.read().splitlines()
        input_word_set |= set(word_list)


# # ##################################################### root youdict yaml
# print('start root_dict.mdx')
# no_root_list = list()
# youdict_root = Youdict_Root()
# yaml_root = Yaml_Root()
# dictionary = dict()
# for word in input_word_set:
#     root = youdict_root.get_root(word)
#     if root == '':
#         root = yaml_root.get_root(word)
#     if len(root) > 0:
#         dictionary[word] = root
#     else:
#         no_root_list.append(word)
#
#
# writer = MDictWriter(dictionary, title="Root and Affix Dictionary", description="Root and Affix Dictionary from www.youdict.com and yaml")
# outfile = open("root_dict.mdx", "wb")
# writer.write(outfile)
# outfile.close()
#
# print(len(no_root_list))
# for word in no_root_list:
#     print(word)


# ##################################################### Levenshtein similar
# print('start distance_similar.mdx')
# edit_distance = Distance_Similar()
# dictionary = dict()
# for word in tqdm(input_word_set):
#     similar_str = edit_distance.get_similar_word_str(word)
#     if len(similar_str) > 0:
#         dictionary[word] = similar_str
#
# writer = MDictWriter(dictionary, title="Distance Similar Dictionary", description="find similar by Levenshtein distance")
# outfile = open("distance_similar.mdx", "wb")
# writer.write(outfile)
# outfile.close()


# ##################################################### no prefix similar
print('start no_prefix_similar.mdx')
no_prefix_similar = No_Root_Similar()
dictionary = dict()
for word in tqdm(input_word_set):
    similar_str = no_prefix_similar.get_similar_word_str(word)
    if len(similar_str) > 0:
        dictionary[word] = similar_str

writer = MDictWriter(dictionary, title="No Prefix Similar Dictionary", description="find similar by no prefix")
outfile = open("no_prefix_similar.mdx", "wb")
writer.write(outfile)
outfile.close()


# ##################################################### youdict mem
# print('start youdict_mem.mdx')
# youdict_mem = Youdict_Mem()
# dictionary = dict()
# for word in input_word_set:
#     mem_str = youdict_mem.get_mem_html(word)
#     if len(mem_str) > 0:
#         dictionary[word] = mem_str
#
# writer = MDictWriter(dictionary, title="Memory Dictionary", description="Memory Dictionary from www.youdict.com")
# outfile = open("youdict_mem.mdx", "wb")
# writer.write(outfile)
# outfile.close()
