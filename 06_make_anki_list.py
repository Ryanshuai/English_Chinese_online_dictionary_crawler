
from word_root import Cigencizhui_Root


high_school_txt = 'D:/github_project/make_anki_word_list/word_list/high_school.txt'
college_cet4_txt = 'D:/github_project/make_anki_word_list/word_list/college_cet_4.txt'
college_cet6_txt = 'D:/github_project/make_anki_word_list/word_list/college_cet_6.txt'
college_post_txt = 'D:/github_project/make_anki_word_list/word_list/college_考研词汇表.txt'
toefl_qu_txt = 'D:/github_project/make_anki_word_list/word_list/qu_10000.txt'
toefl_red_txt = 'D:/github_project/make_anki_word_list/word_list/TOEFL_红宝书.txt'
toefl_class_txt = 'D:/github_project/make_anki_word_list/word_list/TOEFL_分类词汇.txt'
toefl_frequency_txt = 'D:/github_project/make_anki_word_list/word_list/TOEFL_frequency_filtered.txt'
gre_3000_txt = 'D:/github_project/make_anki_word_list/word_list/GRE_3000.txt'
gre_foot_txt = 'D:/github_project/make_anki_word_list/word_list/GRE_foot.txt'
gre_red_txt = 'D:/github_project/make_anki_word_list/word_list/GRE_red.txt'
gre_synonym_txt = 'D:/github_project/make_anki_word_list/word_list/GRE_synonym.txt'
gre_kmf_6_2_txt = 'D:/github_project/make_anki_word_list/word_list/GRE_kmf_6_2.txt'
gre_frequency_txt = 'D:/github_project/make_anki_word_list/word_list/GRE_frequency.txt'

internal_txt = 'D:/github_project/make_anki_word_list/word_list/internal_word.txt'
all_txt = 'D:/github_project/make_anki_word_list/word_list/all.txt'


input_txt_list = list()
# input_txt_list.append(tst_txt)
# input_txt_list.append(high_school_txt)
# input_txt_list.append(college_cet4_txt)
# input_txt_list.append(college_cet6_txt)
# input_txt_list.append(college_post_txt)
# input_txt_list.append(toefl_red_txt)
input_txt_list.append(toefl_frequency_txt)
# input_txt_list.append(toefl_class_txt)
# input_txt_list.append(toefl_qu_txt)
# input_txt_list.append(gre_3000_txt)
# input_txt_list.append(gre_foot_txt)
# input_txt_list.append(gre_red_txt)
# input_txt_list.append(gre_synonym_txt)

input_word_set = set()
for file in input_txt_list:
    with open(file,encoding='utf-8') as f:
        word_list = f.read().splitlines()
        input_word_set |= set(word_list)
print('len of input_word_set: ', len(input_word_set))
print('input_txt_list: ', list(map(lambda x: x.split('/')[-1][:-4], input_txt_list)))
print('-----------------------------------------------------')

input_txt_list_2 = list()
# input_txt_list_2.append(tst_txt)
# input_txt_list_2.append(high_school_txt)
# input_txt_list_2.append(college_cet4_txt)
# input_txt_list_2.append(college_cet6_txt)
# input_txt_list_2.append(college_post_txt)
# input_txt_list_2.append(toefl_qu_txt)
# input_txt_list_2.append(toefl_red_txt)
# input_txt_list_2.append(toefl_class_txt)
# input_txt_list_2.append(gre_3000_txt)
# input_txt_list_2.append(gre_foot_txt)
# input_txt_list_2.append(gre_red_txt)
# input_txt_list_2.append(gre_synonym_txt)
# input_txt_list_2.append(gre_kmf_6_2_txt)
# input_txt_list_2.append(internal_txt)

input_word_set_2 = set()
for file in input_txt_list_2:
    with open(file, 'r', encoding='utf-8') as f:
        word_list_2 = f.read().splitlines()
        input_word_set_2 |= set(word_list_2)
print('len of input_word_set_2: ', len(input_word_set_2))
print('input_txt_list_2: ', list(map(lambda x: x.split('/')[-1][:-4], input_txt_list_2)))
print('-----------------------------------------------------')

final_word_list = list(input_word_set_2 - input_word_set)
print('input_word_set_2-input_word_set', len(final_word_list))


def make_pure_word_list():
    cigencizhui_root = Cigencizhui_Root()
    with open('pure_word_list.txt', 'w', encoding='utf-8') as f:
        ordered_input_word_list = cigencizhui_root.put_word_list_in_order(final_word_list)
        for word in ordered_input_word_list:
            print(word)
            f.write(word)
            f.write('\n')


def make_anki_word_image_list():
    cigencizhui_root = Cigencizhui_Root()
    with open('output/anki_word_image_list.txt', 'w', encoding='utf-8') as f:
        # final_word_list = cigencizhui_root.put_word_list_in_order(final_word_list)
        final_word_list = word_list
        print('ordered_input_word_list: ', len(final_word_list))
        for word in final_word_list:
            word = word.strip()
            line = word
            for i in range(1, 11):
                line += "\\<img src=\"{}.jpg\" />".format(word+str(i))
            f.write(line)
            f.write('\n')


def make_gre_synonym_image_list():
    with open(gre_synonym_txt, 'r', encoding='utf-8') as f:
        word_list = f.read().splitlines()

    with open('output/GRE_anki_same.txt', 'w', encoding='utf-8') as f:
        for word in word_list:
            word = word.strip()
            if len(word) == 0:
                continue
            print(word)
            if '\u4e00' <= word[0] <= '\u9fff':
                now_class = word
            else:
                line = word
                for i in range(1, 11):
                    line += "\\<img src=\"{}.jpg\" />".format(word + str(i))
                line += "\\"+now_class
                f.write(line)
                f.write('\n')


def make_anki_delete_list():
    with open('output/anki_delete_list.txt', 'w', encoding='utf-8') as f:
        for word in final_word_list:
            word = word.strip()
            line = word
            line += '\\_____'
            f.write(line)
            f.write('\n')


if __name__ == '__main__':
    # make_anki_delete_list()
    make_anki_word_image_list()


