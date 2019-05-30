
from word_root import Assembled_Root


_high_school_txt = 'D:/github_project/make_anki_word_list/word_list/high_school.txt'
_college_cet4_txt = 'D:/github_project/make_anki_word_list/word_list/college_cet_4.txt'
_college_cet6_txt = 'D:/github_project/make_anki_word_list/word_list/college_cet_6.txt'
_college_post_txt = 'D:/github_project/make_anki_word_list/word_list/college_考研词汇表.txt'
_toefl_qu_txt = 'D:/github_project/make_anki_word_list/word_list/qu_10000.txt'
_toefl_red_txt = 'D:/github_project/make_anki_word_list/word_list/TOEFL_红宝书.txt'
_toefl_class_txt = 'D:/github_project/make_anki_word_list/word_list/TOEFL_分类词汇.txt'
_toefl_frequency_6_txt = 'D:/github_project/make_anki_word_list/word_list/TOEFL_frequency_6.0.txt'
_toefl_frequency_7_txt = 'D:/github_project/make_anki_word_list/word_list/TOEFL_frequency_7.0.txt'
# _toefl_frequency_export_txt = 'D:/github_project/make_anki_word_list/word_list/TOEFL_frequency_export.txt'
_gre_3000_txt = 'D:/github_project/make_anki_word_list/word_list/GRE_3000.txt'
_gre_foot_txt = 'D:/github_project/make_anki_word_list/word_list/GRE_foot.txt'
_gre_red_txt = 'D:/github_project/make_anki_word_list/word_list/GRE_red.txt'
_gre_synonym_txt = 'D:/github_project/make_anki_word_list/word_list/GRE_synonym.txt'
_gre_kmf_6_2_txt = 'D:/github_project/make_anki_word_list/word_list/GRE_kmf_6_2.txt'
_gre_frequency_txt = 'D:/github_project/make_anki_word_list/word_list/GRE_frequency.txt'

internal_txt = 'D:/github_project/make_anki_word_list/word_list/internal_word.txt'
all_txt = 'D:/github_project/make_anki_word_list/word_list/all.txt'

with open(_high_school_txt, encoding='utf-8') as f:
    high_school_set = set(f.read().splitlines())
with open(_college_cet4_txt, encoding='utf-8') as f:
    college_cet4_set = set(f.read().splitlines())
with open(_college_cet6_txt, encoding='utf-8') as f:
    college_cet6_set = set(f.read().splitlines())
with open(_college_post_txt, encoding='utf-8') as f:
    college_post_set = set(f.read().splitlines())
with open(_toefl_qu_txt, encoding='utf-8') as f:
    toefl_qu_set = set(f.read().splitlines())
with open(_toefl_red_txt, encoding='utf-8') as f:
    toefl_red_set = set(f.read().splitlines())
with open(_toefl_class_txt, encoding='utf-8') as f:
    toefl_class_set = set(f.read().splitlines())
with open(_toefl_frequency_6_txt, encoding='utf-8') as f:
    fre_set = set(f.read().splitlines())
    toefl_frequency_6_set = set(map(lambda x: x.split('\\')[0], fre_set))
with open(_toefl_frequency_7_txt, encoding='utf-8') as f:
    fre_set = set(f.read().splitlines())
    toefl_frequency_7_set = set(map(lambda x: x.split('\\')[0], fre_set))
# with open(_toefl_frequency_export_txt, encoding='utf-8') as f:
#     fre_set = set(f.read().splitlines())
#     toefl_frequency_export_set = set(map(lambda x: x.split('\\')[0], fre_set))
with open(_gre_3000_txt, encoding='utf-8') as f:
    gre_3000_set = set(f.read().splitlines())
with open(_gre_foot_txt, encoding='utf-8') as f:
    gre_foot_set = set(f.read().splitlines())
with open(_gre_red_txt, encoding='utf-8') as f:
    gre_red_set = set(f.read().splitlines())
with open(_gre_synonym_txt, encoding='utf-8') as f:
    gre_synonym_set = set(f.read().splitlines())
with open(_gre_frequency_txt, encoding='utf-8') as f:
    fre_set = set(f.read().splitlines())
    gre_frequency_set = set(map(lambda x: x.split('\\')[0], fre_set))
with open(internal_txt, encoding='utf-8') as f:
    internal_set = set(f.read().splitlines())

all_college_set = college_cet4_set|college_cet6_set|college_post_set
all_toefl_set = toefl_red_set|toefl_frequency_6_set|toefl_frequency_7_set|toefl_qu_set
all_gre_set = gre_3000_set|gre_foot_set|gre_red_set|gre_synonym_set|gre_frequency_set
all_word_set = all_college_set|all_toefl_set|all_gre_set

word_set_dict = {'college_cet4': college_cet4_set,
                'college_cet4': college_cet4_set,
                'college_cet6': college_cet6_set,
                'college_post': college_post_set,
                'toefl_red_set': toefl_red_set,
                'toefl_frequency_6_set': toefl_frequency_6_set,
                'toefl_frequency_7': toefl_frequency_7_set,
                'toefl_qu': toefl_qu_set,
                'gre_3000': gre_3000_set,
                'gre_foot': gre_foot_set,
                'gre_red': gre_red_set,
                'gre_synonym': gre_synonym_set,
                'gre_frequency': gre_frequency_set,
                'all_college': all_college_set,
                'all_toefl': all_toefl_set,
                'all_gre': all_gre_set,
                 }

def make_internal_list():
    assembled_root = Assembled_Root()

    internal_word_set = set()
    for word in all_word_set:
        root_htmls = assembled_root.get_all_kind_root_html(word)
        internal_word = assembled_root.get_internal_word_set(root_htmls)
        internal_word_set |= internal_word
    internal_word_list = sorted(internal_word_set, key=str.lower)

    print('making internal_word.txt')
    with open(internal_txt, 'w', encoding='utf-8') as f:
        for word in internal_word_list:
            if len(word) <= 1:
                continue
            f.write(word)
            f.write('\n')


all_word_set |= internal_set
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
