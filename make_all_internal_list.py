from word_root import Assembled_Root


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


def make_internal_list():
    assembled_root = Assembled_Root()

    input_txt_list = list()
    input_txt_list.append(tst_txt)
    input_txt_list.append(high_school_txt)
    input_txt_list.append(college_cet4_txt)
    input_txt_list.append(college_cet6_txt)
    input_txt_list.append(college_post_txt)
    input_txt_list.append(toefl_qu_txt)
    input_txt_list.append(toefl_red_txt)
    # input_txt_list.append(toefl_class_txt)
    input_txt_list.append(gre_3000_txt)
    input_txt_list.append(gre_foot_txt)
    input_txt_list.append(gre_red_txt)
    input_txt_list.append(gre_synonym_txt)

    word_set = set()
    for file in input_txt_list:
        with open(file, 'r', encoding='utf-8') as f:
            word_list = f.read().splitlines()
            for word in word_list:
                word = word.strip()
                word_set.add(word)

    internal_word_set = set()
    for word in word_set:
        root_htmls = assembled_root.get_all_kind_root_html(word)
        internal_word = assembled_root.get_internal_word_set(*root_htmls)
        internal_word_set |= internal_word
    internal_word_list = sorted(internal_word_set, key=str.lower)

    print('making internal_word.txt')
    with open(internal_txt, 'w', encoding='utf-8') as f:
        for word in internal_word_list:
            if len(word) <= 1:
                continue
            f.write(word)
            f.write('\n')


def make_all_list():
    input_txt_list = list()
    input_txt_list.append(tst_txt)
    input_txt_list.append(high_school_txt)
    input_txt_list.append(college_cet4_txt)
    input_txt_list.append(college_cet6_txt)
    input_txt_list.append(college_post_txt)
    input_txt_list.append(toefl_qu_txt)
    input_txt_list.append(toefl_red_txt)
    # input_txt_list.append(toefl_class_txt)
    input_txt_list.append(gre_3000_txt)
    input_txt_list.append(gre_foot_txt)
    input_txt_list.append(gre_red_txt)
    input_txt_list.append(gre_synonym_txt)

    word_set = set()
    for file in input_txt_list:
        with open(file, 'r',encoding='utf-8') as f:
            word_list = f.read().splitlines()
            for word in word_list:
                word = word.strip()
                word_set.add(word)
    word_list = sorted(word_set, key=str.lower)

    print('making all.txt')
    with open(all_txt, 'w',encoding='utf-8') as f:
        for word in word_list:
            if len(word) <= 1:
                continue
            f.write(word)
            f.write('\n')


if __name__ == '__main__':
    make_internal_list()
    make_all_list()
