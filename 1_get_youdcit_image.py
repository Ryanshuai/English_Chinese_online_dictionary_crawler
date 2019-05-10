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
    all_word_list = 'D:/github_project/make_anki_word_list/word_list/all.txt'
    with open(all_word_list, 'r', encoding='utf-8') as f:
        word_list = f.read().splitlines()
    word_set = set(word_list)
    word_set.discard('con')

    save_to_dir = 'C:/Users/YS/AppData/Roaming/Anki2/Ryan/collection.media/'

    # for word in word_list:
    #     save_word_image_to_dir(word)
    # save_word_image_to_dir('dictator')

    pool = ThreadPoolExecutor(10000)
    for word in word_set:
        for i in range(1, 11):
            name = word+str(i)
            if not os.path.exists(save_to_dir+name+'.jpg'):
                # print(name)
                # save_word_image_to_dir(word)
                a = pool.submit(save_word_image_to_dir, name, save_to_dir)

