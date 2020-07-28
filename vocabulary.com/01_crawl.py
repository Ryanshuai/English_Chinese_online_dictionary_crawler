import os
import time
import random
import threading
from tqdm import tqdm
from word_to_url_to_txt import word_to_url, url_to_html_text


def save_txt(word, save_dir):
    url = word_to_url(word, 'vocabulary.com')
    # print(word, '\tbegin!')
    html_text = url_to_html_text(url)
    to_txt = os.path.join(save_dir, 'word_' + word + '.txt')
    with open(to_txt, 'w', encoding='utf-8') as f:
        f.write(html_text)
        print(word, '\tdone!')


if __name__ == '__main__':
    from utils.word_list.word_list_py.TOEFL_red import all_words_list

    word_set = set(all_words_list)

    html_text_dir = 'vocabulary_html_text'
    exist_set = set(map(lambda x: x[5:-4], os.listdir(html_text_dir)))

    waiting_set = word_set - exist_set

    # check and save html #########################################################################################
    for i, word in enumerate(waiting_set):
        print(i, "/", len(waiting_set), ":", word)
        time.sleep(random.uniform(0.1, 0.5) * 10)
        threading.Timer(0.00001, save_txt, (word, html_text_dir)).start()
        # save_txt(word, html_text_dir)
        if i > 500:
            break
