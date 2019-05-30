import requests
from PIL import Image
from io import BytesIO
from concurrent.futures import ThreadPoolExecutor
import urllib.request
import os


def get_image_from_url(url):
    response = requests.get(url)
    image = Image.open(BytesIO(response.content))
    return image


def save_word_image_to_dir(name, di):

    url = 'http://www.youdict.com/images/words/' + name + '.jpg'
    image_name = name + '.jpg'
    image = get_image_from_url(url)
    # print('saving>>>>>>/t', di+image_name)
    image.convert('RGB').save(di+image_name)
    print(name, '\t\t\t done')


if __name__ == '__main__':
    # all_word_list = 'D:/github_project/make_anki_word_list/word_list/all.txt'
    all_word_list = 'D:/github_project/make_anki_word_list/word_list/TOEFL_frequency_export.txt'
    with open(all_word_list, encoding='utf-8') as f:
        words = f.read().splitlines()
    # words = set(words)
    # words.discard('con')

    save_to_dir = 'C:/Users/YS/AppData/Roaming/Anki2/Ryan/collection.media/'

    # for word in word_list:
    #     save_word_image_to_dir(word)
    # save_word_image_to_dir('dictator')

    pool = ThreadPoolExecutor(128)
    for word in words:
        word = 'crustal'
        for i in range(1, 11):
            name = word+str(i)
            if not os.path.exists(save_to_dir+name+'.jpg'):
                print(word)
                print(name)
                save_word_image_to_dir(name, save_to_dir)
                # a = pool.submit(save_word_image_to_dir, name, save_to_dir)

