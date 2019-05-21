import venn


high_school_txt = 'D:/github_project/make_anki_word_list/word_list/high_school.txt'
college_cet4_txt = 'D:/github_project/make_anki_word_list/word_list/college_cet_4.txt'
college_cet6_txt = 'D:/github_project/make_anki_word_list/word_list/college_cet_6.txt'
college_post_txt = 'D:/github_project/make_anki_word_list/word_list/college_考研词汇表.txt'
toefl_qu_txt = 'D:/github_project/make_anki_word_list/word_list/qu_10000.txt'
toefl_red_txt = 'D:/github_project/make_anki_word_list/word_list/TOEFL_红宝书.txt'
toefl_class_txt = 'D:/github_project/make_anki_word_list/word_list/TOEFL_分类词汇.txt'
gre_3000_txt = 'D:/github_project/make_anki_word_list/word_list/GRE_3000.txt'
gre_foot_txt = 'D:/github_project/make_anki_word_list/word_list/GRE_foot.txt'
gre_red_txt = 'D:/github_project/make_anki_word_list/word_list/GRE_red.txt'
gre_synonym_txt = 'D:/github_project/make_anki_word_list/word_list/GRE_synonym.txt'
gre_kmf_6_2 = 'D:/github_project/make_anki_word_list/word_list/GRE_kmf_6_2.txt'
internal_txt = 'D:/github_project/make_anki_word_list/word_list/internal_word.txt'
all_txt = 'D:/github_project/make_anki_word_list/word_list/all.txt'

with open(high_school_txt, 'r', encoding='utf-8') as f:
    high_school_set = set(f.read().splitlines())
with open(college_cet4_txt, 'r', encoding='utf-8') as f:
    college_cet4_set = set(f.read().splitlines())
with open(college_cet6_txt, 'r', encoding='utf-8') as f:
    college_cet6_set = set(f.read().splitlines())
with open(college_post_txt, 'r', encoding='utf-8') as f:
    college_post_set = set(f.read().splitlines())
with open(toefl_qu_txt, 'r', encoding='utf-8') as f:
    toefl_qu_set = set(f.read().splitlines())
with open(toefl_red_txt, 'r', encoding='utf-8') as f:
    toefl_red_set = set(f.read().splitlines())
with open(toefl_class_txt, 'r', encoding='utf-8') as f:
    toefl_class_set = set(f.read().splitlines())
with open(gre_3000_txt, 'r', encoding='utf-8') as f:
    gre_3000_set = set(f.read().splitlines())
with open(gre_foot_txt, 'r', encoding='utf-8') as f:
    gre_foot_set = set(f.read().splitlines())
with open(gre_red_txt, 'r', encoding='utf-8') as f:
    gre_red_set = set(f.read().splitlines())
with open(gre_synonym_txt, 'r', encoding='utf-8') as f:
    gre_synonym_set = set(f.read().splitlines())
college_set = college_cet4_set | college_cet6_set | college_post_set
toefl_set = toefl_red_set
gre_set = gre_3000_set #| gre_foot_set

# set_list = [college_set, toefl_set, gre_set, gre_red_set]
# name_list = ['c', 't', 'g', 'gr']
# set_list = [gre_3000_set, gre_foot_set, gre_red_set, toefl_set]
# name_list = ['3000', 'foot', 'gre_red', 'toefl']
# set_list = [gre_3000_set, gre_synonym_set, gre_red_set|college_set|toefl_set]
# name_list = ['3000', 'synonym', 'all']

set_list = [college_set, toefl_set, gre_set]
name_list = ['college_set', 'toefl_set', 'gre_set']

num = len(set_list)
assert 2 <= num <= 6
if num == 2:
    venn_venn = venn.venn2
if num == 3:
    venn_venn = venn.venn3
if num == 4:
    venn_venn = venn.venn4
if num == 5:
    venn_venn = venn.venn5
if num == 6:
    venn_venn = venn.venn6

labels = venn.get_labels(set_list, fill=['number', 'logic'])
fig, ax = venn_venn(labels, names=name_list)
fig.show()
