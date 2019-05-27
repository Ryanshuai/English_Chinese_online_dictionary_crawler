
from os.path import join, basename

input_txt = 'D:/github_project/make_anki_word_list/anki_exports/TOEFL.txt'

input_base_name = basename(input_txt)
output_txt = join('D:/github_project/make_anki_word_list/word_list/', input_base_name.split('.')[0] + '_export.txt')

with open(input_txt, encoding='utf-8') as f:
    lines = f.readlines()

new_line_list = list()
in_new_card = False
for i, line in enumerate(lines):
    if '<!--所有释义的入口，if有头词-->' in line:
        in_new_card = True
    if '<span class=""title"">' in line and in_new_card:
        word = line[27:-8]
        word = word.replace('ˈ','')
        word = word.replace('ˌ','')
        if 'ˌ' in line[27:-8]:
            print(word)
        new_line_list.append(word)
        in_new_card = False

with open(output_txt, 'w', encoding='utf-8') as f:
    for word in new_line_list:
        f.write(word)
        f.write('\n')
