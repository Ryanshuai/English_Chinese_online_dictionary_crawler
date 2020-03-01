import requests
import re
from tqdm import tqdm


def get_phonetic_symbol(word):
    word = word.replace(" ", "_")
    request = requests.get("https://en.oxforddictionaries.com/definition/" + word)
    html = request.text

    regularExpression = r'<span\s+class="phoneticspelling">/([^\/]*)/</span>'
    matchObject = re.search(regularExpression, html, re.I)

    phoneticSpelling = ""
    if matchObject:
        if matchObject.group(1):
            phoneticSpelling = matchObject.group(1)

    return phoneticSpelling


if __name__ == '__main__':
    phonetic_symbol_text_dir = 'D:/github_project/make_anki_word_list/phonetic_symbol/phonetic_symbol.txt'
    all_word_list = 'D:/github_project/make_anki_word_list/word_list/all.txt'
    with open(all_word_list, 'r', encoding='utf-8') as f:
        word_list = f.read().splitlines()
    word_set = set(word_list)
    word_set.discard('con')

    # update txt ###################################################################################################
    phonetic_symbol_line_list = list()
    for word in tqdm(word_set, desc='decoding'):
        phonetic_symbol = get_phonetic_symbol(word)
        phonetic_symbol_line_list.append(word + '\\' + phonetic_symbol)

    with open(phonetic_symbol_text_dir, 'w', encoding='utf-8') as f:
        for line in phonetic_symbol_line_list:
            f.write(line)
            f.write('\n')
