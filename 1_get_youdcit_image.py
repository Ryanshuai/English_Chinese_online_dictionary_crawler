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


def save_word_image_to_dir(name, di='youdict_word_images/'):

    url = 'http://www.youdict.com/images/words/' + name + '.jpg'
    image_name = name + '.jpg'
    image = get_image_from_url(url)
    # print('saving>>>>>>\t', di+image_name)
    image.convert('RGB').save(di+image_name)


if __name__ == '__main__':
    # ####################################################### build filter list
    all_word_list = 'D:/github_project/make_anki_word_list/word_list/all.txt'
    with open(all_word_list, 'r', encoding='utf-8') as f:
        word_list = f.read().splitlines()
    word_set = set(word_list)
    word_set.remove('con')

    print('download image for {} word'.format(len(word_set)))

    # for word in word_list:
    #     save_word_image_to_dir(word)
    # save_word_image_to_dir('dictator')

    pool = ThreadPoolExecutor(10000)
    for word in word_set:
        for i in range(1, 11):
            name = word+str(i)
            if not os.path.exists('youdict_word_images/'+name+'.jpg'):
                print(name)
                # save_word_image_to_dir(word)
                a = pool.submit(save_word_image_to_dir, name)

