_high_school_txt = './high_school.txt'
_college_cet4_txt = './college_cet_4.txt'
_college_cet6_txt = './college_cet_6.txt'
_college_post_txt = './college_考研词汇表.txt'
_toefl_qu_txt = './qu_10000.txt'
_toefl_red_txt = './TOEFL_红宝书.txt'
_toefl_class_txt = './TOEFL_分类词汇.txt'
_toefl_frequency_6_txt = './TOEFL_frequency_6.0.txt'
_toefl_frequency_7_txt = './TOEFL_frequency_7.0.txt'
_gre_3000_txt = './GRE_3000.txt'
_gre_foot_txt = './GRE_foot.txt'
_gre_red_txt = './GRE_red.txt'
_gre_synonym_txt = './GRE_synonym.txt'
_gre_kmf_6_2_txt = './GRE_kmf_6_2.txt'

internal_txt = './internal_word.txt'

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
with open(_gre_3000_txt, encoding='utf-8') as f:
    gre_3000_set = set(f.read().splitlines())
with open(_gre_foot_txt, encoding='utf-8') as f:
    gre_foot_set = set(f.read().splitlines())
with open(_gre_red_txt, encoding='utf-8') as f:
    gre_red_set = set(f.read().splitlines())
with open(_gre_synonym_txt, encoding='utf-8') as f:
    gre_synonym_set = set(f.read().splitlines())
with open(internal_txt, encoding='utf-8') as f:
    internal_set = set(f.read().splitlines())

all_college_set = college_cet4_set | college_cet6_set | college_post_set
all_toefl_set = toefl_red_set | toefl_qu_set
all_gre_set = gre_3000_set | gre_foot_set | gre_red_set | gre_synonym_set
all_word_set = all_college_set | all_toefl_set | all_gre_set

word_set_dict = {'college_cet4': college_cet4_set,
                 'college_cet4': college_cet4_set,
                 'college_cet6': college_cet6_set,
                 'college_post': college_post_set,
                 'toefl_red_set': toefl_red_set,
                 'toefl_qu': toefl_qu_set,
                 'gre_3000': gre_3000_set,
                 'gre_foot': gre_foot_set,
                 'gre_red': gre_red_set,
                 'gre_synonym': gre_synonym_set,
                 'all_college': all_college_set,
                 'all_toefl': all_toefl_set,
                 'all_gre': all_gre_set,
                 }

all_word_set |= internal_set


def make_all_list():
    print('making all_words_list.py')
    with open('all_words_list.py', 'w', encoding='utf-8') as f:
        f.write('all_words_list = [')
        for word in all_word_set:
            if len(word) <= 1:
                continue
            f.write('"')
            f.write(word)
            f.write('",\n')
        f.write(']')


if __name__ == '__main__':
    make_all_list()
