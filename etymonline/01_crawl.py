import os
import time
import random
import threading
from tqdm import tqdm
from word_to_url_to_txt import word_to_url, url_to_html_text


def save_txt(word, save_dir):
    url = word_to_url(word, 'etymonline')
    print(word, '\tbegin!')
    html_text = url_to_html_text(url)
    to_txt = os.path.join(save_dir, 'word_' + word + '.txt')
    with open(to_txt, 'w', encoding='utf-8') as f:
        f.write(html_text)
        print(word, '\tdone!')


if __name__ == '__main__':
    all_word_list = '../word_list/all.txt'
    with open(all_word_list, 'r', encoding='utf-8') as f:
        word_list = f.read().splitlines()
    word_set = set(word_list)

    html_text_dir = 'etymonline_html_text'
    exist_set = set(map(lambda x: x[5:-4], os.listdir(html_text_dir)))

    waiting_set = word_set - exist_set

    # check and save html #########################################################################################
    counter = 0
    for word in waiting_set:
        time.sleep(random.uniform(0.01, 0.5))
        threading.Timer(0.00001, save_txt, (word, html_text_dir)).start()
        if counter > 500:
            break
