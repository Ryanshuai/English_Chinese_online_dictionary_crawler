
import venn
from utils.word_list.make_all_words_list import *


new_toefl_class_set = set()
for line in toefl_class_set:
    words = line.split(' ')
    for word in words:
        new_toefl_class_set.add(word)

# set_list = [college_set, toefl_set, gre_set, gre_red_set]
# name_list = ['c', 't', 'g', 'gr']
# set_list = [gre_3000_set, gre_foot_set, gre_red_set, toefl_set]
# name_list = ['3000', 'foot', 'gre_red', 'toefl']
# set_list = [gre_3000_set, gre_synonym_set, gre_red_set|college_set|toefl_set]
# name_list = ['3000', 'synonym', 'all']

# set_list = [gre_red_set, gre_frequency_set, gre_set]
# name_list = ['gre_red_set', 'gre_frequency_set', 'gre_set']

set_list = [toefl_frequency_6_set, toefl_frequency_7_set]
name_list = ['toefl_frequency_6_set', 'toefl_frequency_7_set']

num = len(set_list)
assert 2 <= num <= 6
if num == 2:
    venn_venn = venn.venn2
elif num == 3:
    venn_venn = venn.venn3
elif num == 4:
    venn_venn = venn.venn4
elif num == 5:
    venn_venn = venn.venn5
elif num == 6:
    venn_venn = venn.venn6
else:
    def raise_exception(*args): raise Exception(num, 'wrong')
    venn_venn = raise_exception

labels = venn.get_labels(set_list, fill=['number', 'logic'])
fig, ax = venn_venn(labels, names=name_list)
fig.show()
