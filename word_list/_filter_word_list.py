

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
gre_kmf_6_2_txt = 'D:/github_project/make_anki_word_list/word_list/GRE_kmf_6_2.txt'
gre_frequency_txt = 'D:/github_project/make_anki_word_list/word_list/GRE_frequency.txt'

internal_txt = 'D:/github_project/make_anki_word_list/word_list/internal_word.txt'
all_txt = 'D:/github_project/make_anki_word_list/word_list/all.txt'

input_txt = all_txt
with open(input_txt, 'r', encoding='utf-8') as f:
    lines = f.read().splitlines()

# prepotion_list =['in', 'on', 'with', 'by', 'at', 'for', 'about', 'under', 'of', 'to', 'into', 'about', 'after']
#
# new_lines = list()
# for line in lines:
#     for prep in prepotion_list:
#         if ' '+prep+' ' in line:
#             line = line.replace(' '+prep+' ', '_'+prep+' ')
#
#     new_lines.append(line)
#     print(line)


new_lines = list()
for line in lines:
    fre, word = line.split(' ')
    new_line = word + '\\' + fre
    new_lines.append(new_line)
    print(new_line)

output = input_txt.split('.')[0] + '___.txt'
with open(output, 'w', encoding='utf-8') as f:
    for line in new_lines:
        f.write(line)
        f.write('\n')
