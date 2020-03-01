from tqdm import tqdm
from utils.writemdict.writemdict import MDictWriter
from ryan_similar.similar_word import Distance_Similar

# ####################################################### build filter list
all_word_list = 'D:/github_project/make_anki_word_list/word_list/all.txt'
with open(all_word_list, encoding='utf-8') as f:
    word_list = f.read().splitlines()
word_set = set(word_list)
word_set.discard('con')


# ##################################################### distance similar
edit_distance = Distance_Similar()
dictionary = dict()
for word in tqdm(word_set, desc='distance_similar.mdx'):
    similar_str = edit_distance.get_similar_word_str(word)
    if len(similar_str) > 0:
        dictionary[word] = similar_str

writer = MDictWriter(dictionary, title="Distance Similar Dictionary", description="find similar by Levenshtein distance")
outfile = open("output/distance_similar.mdx", "wb")
writer.write(outfile)
outfile.close()


# ##################################################### no prefix similar
# no_prefix_similar = No_Prefix_Similar()
# dictionary = dict()
# for word in tqdm(word_set, desc='no_prefix_similar.mdx'):
#     similar_str = no_prefix_similar.get_similar_word_str(word)
#     if len(similar_str) > 0:
#         dictionary[word] = similar_str
#
# writer = MDictWriter(dictionary, title="No Prefix Similar Dictionary", description="find similar by no prefix")
# outfile = open("output/no_prefix_similar.mdx", "wb")
# writer.write(outfile)
# outfile.close()
#
#
# ##################################################### no suffix similar
# no_suffix_similar = No_Suffix_Similar()
# dictionary = dict()
# for word in tqdm(word_set, desc='no_suffix_similar.mdx'):
#     similar_str = no_suffix_similar.get_similar_word_str(word)
#     if len(similar_str) > 0:
#         dictionary[word] = similar_str
#
# writer = MDictWriter(dictionary, title="No suffix Similar Dictionary", description="find similar by no suffix")
# outfile = open("output/no_suffix_similar.mdx", "wb")
# writer.write(outfile)
# outfile.close()
#
#
# # ##################################################### youdict mem
# youdict_mem = Youdict_Mem()
# dictionary = dict()
# for word in tqdm(word_set, desc='youdict_mem.mdx'):
#     mem_str = youdict_mem.get_mem_html(word)
#     if len(mem_str) > 0:
#         dictionary[word] = mem_str
#
# writer = MDictWriter(dictionary, title="Memory Dictionary", description="Memory Dictionary from www.youdict.com")
# outfile = open("output/youdict_mem.mdx", "wb")
# writer.write(outfile)
# outfile.close()
#
#
# # #################################################### root youdict yaml
# assembled_root = Assembled_Root()
#
# dictionary = dict()
# for word in tqdm(word_set, desc='root.mdx'):
#     root = assembled_root.get_root_html(word)
#     if len(root) > 0:
#         dictionary[word] = root
#
# writer = MDictWriter(dictionary, title="Root and Affix Dictionary", description="Root and Affix Dictionary from www.youdict.com or yaml or etymonline")
# outfile = open("output/root.mdx", "wb")
# writer.write(outfile)
# outfile.close()
#
#
# # # #################################################### root youdict yaml
# yaml_root = Yaml_Root()
#
# dictionary = dict()
# for word in tqdm(word_set, desc='possible_prs.mdx'):
#     possible_root = yaml_root.get_possible_prefix_root_suffix_html(word)
#     if len(possible_root) > 0:
#         dictionary[word] = possible_root
#
# writer = MDictWriter(dictionary, title="Root and Affix Dictionary", description="possible root and affix dictionary from yaml")
# outfile = open("output/possible_prs.mdx", "wb")
# writer.write(outfile)
# outfile.close()
#
#
#
# # #################################################### gre frequency
# all_word_list = 'D:/github_project/make_anki_word_list/word_list/GRE_frequency.txt'
# with open(all_word_list, encoding='utf-8') as f:
#     line_list = f.read().splitlines()
#
# dictionary = dict()
# for line in line_list:
#     word, frequency = line.split('\\')
#     dictionary[word] = frequency
#
# writer = MDictWriter(dictionary, title="GRE word frequency", description="")
# with open("output/GRE_word_frequency.mdx", "wb") as f:
#     writer.write(f)
#
# # #################################################### toefl frequency
# all_word_list = 'D:/github_project/make_anki_word_list/word_list/TOEFL_frequency_6.0.txt'
# with open(all_word_list, encoding='utf-8') as f:
#     line_list = f.read().splitlines()
#
# dictionary = dict()
# for line in line_list:
#     word, frequency = line.split('\\')
#     dictionary[word] = frequency
#
# writer = MDictWriter(dictionary, title="TOEFL word frequency", description="")
# with open("output/TOEFL_word_frequency.mdx", "wb") as f:
#     writer.write(f)
#
