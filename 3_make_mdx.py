import yaml
from tqdm import tqdm
from writemdict.writemdict import MDictWriter
from similar_word import Distance_Similar, No_Root_Similar
from word_root import Yaml_Root, Youdict_Root
from youdict_mem import Youdict_Mem


# ####################################################### build filter list
all_word_list = 'D:/github_project/make_anki_word_list/word_list/all_word_list.txt'


with open(all_word_list, 'r',encoding='utf-8') as f:
    word_list = f.read().splitlines()
input_word_set = set(word_list)


# ##################################################### root youdict yaml
no_root_list = list()
youdict_root = Youdict_Root()
yaml_root = Yaml_Root()
dictionary = dict()
for word in tqdm(input_word_set, desc='root_dict.mdx'):
    root = youdict_root.get_root_str_for_mdx(word)
    if root == '':
        root = yaml_root.get_root(word)
    if len(root) > 0:
        dictionary[word] = root
    else:
        no_root_list.append(word)


writer = MDictWriter(dictionary, title="Root and Affix Dictionary", description="Root and Affix Dictionary from www.youdict.com and yaml")
outfile = open("output/root_dict.mdx", "wb")
writer.write(outfile)
outfile.close()

print(len(no_root_list))
for word in no_root_list:
    print(word)


##################################################### Levenshtein similar
edit_distance = Distance_Similar()
dictionary = dict()
for word in tqdm(input_word_set, desc='distance_similar.mdx'):
    similar_str = edit_distance.get_similar_word_str(word)
    if len(similar_str) > 0:
        dictionary[word] = similar_str

writer = MDictWriter(dictionary, title="Distance Similar Dictionary", description="find similar by Levenshtein distance")
outfile = open("output/distance_similar.mdx", "wb")
writer.write(outfile)
outfile.close()


# ##################################################### no prefix similar
no_prefix_similar = No_Root_Similar()
dictionary = dict()
for word in tqdm(input_word_set, desc='no_prefix_similar.mdx'):
    similar_str = no_prefix_similar.get_similar_word_str(word)
    if len(similar_str) > 0:
        dictionary[word] = similar_str

writer = MDictWriter(dictionary, title="No Prefix Similar Dictionary", description="find similar by no prefix")
outfile = open("output/no_prefix_similar.mdx", "wb")
writer.write(outfile)
outfile.close()


##################################################### youdict mem
youdict_mem = Youdict_Mem()
dictionary = dict()
for word in tqdm(input_word_set, desc='youdict_mem.mdx'):
    mem_str = youdict_mem.get_mem_html(word)
    if len(mem_str) > 0:
        dictionary[word] = mem_str

writer = MDictWriter(dictionary, title="Memory Dictionary", description="Memory Dictionary from www.youdict.com")
outfile = open("output/youdict_mem.mdx", "wb")
writer.write(outfile)
outfile.close()


# # ##################################################### root youdict yaml
no_root_list = list()
youdict_root = Youdict_Root()
dictionary = dict()
yaml_root = Yaml_Root()
for word in tqdm(input_word_set, desc='order_root_dict.mdx'):
    root = youdict_root.get_root(word)
    if root == '':
        root = yaml_root.get_root(word)
    if len(root) > 0:
        dictionary[word] = root
    else:
        no_root_list.append(word)


writer = MDictWriter(dictionary, title="Root and Affix Dictionary", description="Root and Affix Dictionary from www.youdict.com and yaml")
outfile = open("output/root_dict.mdx", "wb")
writer.write(outfile)
outfile.close()

print(len(no_root_list))
for word in no_root_list:
    print(word)
