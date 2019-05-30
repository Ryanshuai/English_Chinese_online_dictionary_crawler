
# ####################################################### build filter list
high_school_txt = 'D:/github_project/make_anki_word_list/word_list/high_school.txt'
college_cet4_txt = 'D:/github_project/make_anki_word_list/word_list/college_cet_4.txt'
college_cet6_txt = 'D:/github_project/make_anki_word_list/word_list/college_cet_6.txt'
college_post_txt = 'D:/github_project/make_anki_word_list/word_list/college_考研词汇表.txt'
toefl_qu_txt = 'D:/github_project/make_anki_word_list/word_list/qu_10000.txt'
toefl_red_txt = 'D:/github_project/make_anki_word_list/word_list/TOEFL_红宝书.txt'
toefl_class_txt = 'D:/github_project/make_anki_word_list/word_list/TOEFL_分类词汇.txt'
toefl_frequency_txt = 'D:/github_project/make_anki_word_list/word_list/TOEFL_frequency_export.txt'
gre_3000_txt = 'D:/github_project/make_anki_word_list/word_list/GRE_3000.txt'
gre_foot_txt = 'D:/github_project/make_anki_word_list/word_list/GRE_foot.txt'
gre_red_txt = 'D:/github_project/make_anki_word_list/word_list/GRE_red.txt'
gre_synonym_txt = 'D:/github_project/make_anki_word_list/word_list/GRE_synonym.txt'
gre_kmf_6_2_txt = 'D:/github_project/make_anki_word_list/word_list/GRE_kmf_6_2.txt'
gre_frequency_txt = 'D:/github_project/make_anki_word_list/word_list/GRE_frequency.txt'

internal_txt = 'D:/github_project/make_anki_word_list/word_list/internal_word.txt'
all_txt = 'D:/github_project/make_anki_word_list/word_list/all.txt'

input_txt_list = list()
input_txt_list.append(high_school_txt)
input_txt_list.append(college_cet4_txt)
input_txt_list.append(college_cet6_txt)
input_txt_list.append(college_post_txt)
input_txt_list.append(toefl_qu_txt)
input_txt_list.append(toefl_red_txt)
input_txt_list.append(toefl_class_txt)
input_txt_list.append(toefl_frequency_txt)
input_txt_list.append(gre_3000_txt)
input_txt_list.append(gre_foot_txt)
input_txt_list.append(gre_red_txt)
input_txt_list.append(gre_synonym_txt)
input_txt_list.append(gre_kmf_6_2_txt)
input_txt_list.append(gre_frequency_txt)

t = 'ceramics'
t = t.strip()
for file in input_txt_list:
    with open(file, 'r', encoding='utf-8') as f:
        word_list = f.read().splitlines()
    for word in word_list:
        if t in word:
            print(word, '\tis in list: ',file)

print('=====================================================================')
root = 'ceramics'
word = word.strip()
with open(all_txt, 'r', encoding='utf-8') as f:
    word_list = f.read().splitlines()
for word in word_list:
    if root in word:
        print(word, '\thas root:\t', root)

print('=====================================================================')
suffix = 'illo'
with open(all_txt, 'r', encoding='utf-8') as f:
    word_list = f.read().splitlines()
for word in word_list:
    if word.endswith(suffix):
        print(word, '\thas suffix:\t', suffix)
