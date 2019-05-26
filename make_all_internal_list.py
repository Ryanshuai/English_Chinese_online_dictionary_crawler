from word_root import Assembled_Root



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

with open(high_school_txt, encoding='utf-8') as f:
    high_school_set = set(f.read().splitlines())
with open(college_cet4_txt, encoding='utf-8') as f:
    college_cet4_set = set(f.read().splitlines())
with open(college_cet6_txt, encoding='utf-8') as f:
    college_cet6_set = set(f.read().splitlines())
with open(college_post_txt, encoding='utf-8') as f:
    college_post_set = set(f.read().splitlines())
with open(toefl_qu_txt, encoding='utf-8') as f:
    toefl_qu_set = set(f.read().splitlines())
with open(toefl_red_txt, encoding='utf-8') as f:
    toefl_red_set = set(f.read().splitlines())
with open(toefl_class_txt, encoding='utf-8') as f:
    toefl_class_set = set(f.read().splitlines())
with open(toefl_frequency_txt, encoding='utf-8') as f:
    fre_set = set(f.read().splitlines())
    toefl_frequency_set = set(map(lambda x: x.split('\\')[0], fre_set))
with open(gre_3000_txt, encoding='utf-8') as f:
    gre_3000_set = set(f.read().splitlines())
with open(gre_foot_txt, encoding='utf-8') as f:
    gre_foot_set = set(f.read().splitlines())
with open(gre_red_txt, encoding='utf-8') as f:
    gre_red_set = set(f.read().splitlines())
with open(gre_synonym_txt, encoding='utf-8') as f:
    gre_synonym_set = set(f.read().splitlines())
with open(gre_frequency_txt, encoding='utf-8') as f:
    fre_set = set(f.read().splitlines())
    gre_frequency_set = set(map(lambda x: x.split('\\')[0], fre_set))

all_word_set = high_school_set|college_cet4_set|college_cet6_set|college_post_set|toefl_qu_set|toefl_red_set|toefl_frequency_set|gre_3000_set|gre_foot_set|gre_red_set|gre_synonym_set|gre_frequency_set


def make_internal_list():
    assembled_root = Assembled_Root()

    internal_word_set = set()
    for word in all_word_set:
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
    print('making all.txt')
    with open(all_txt, 'w',encoding='utf-8') as f:
        for word in all_word_set:
            if len(word) <= 1:
                continue
            f.write(word)
            f.write('\n')


if __name__ == '__main__':
    make_internal_list()
    make_all_list()
