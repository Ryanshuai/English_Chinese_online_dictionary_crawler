import requests
from PIL import Image
from io import BytesIO
from concurrent.futures import ThreadPoolExecutor
import urllib.request
import os
import time
import random


def save_word_image_to_dir(name, save_path):
    url = 'http://www.youdict.com/images/words/' + name + '.jpg'
    try:
        response = requests.get(url)
        image = Image.open(BytesIO(response.content))
    except:
        return False
    else:
        # print('saving>>>>>>/t', di+image_name)
        image.convert('RGB').save(save_path)
        print(name, '\t\t\t done')
        return True


if __name__ == '__main__':
    from utils.word_list.all_words_list import all_words_list

    save_to_dir = './quword_images/'

    # pool = ThreadPoolExecutor(2)
    for word in all_words_list:
        word = word.strip()
        for i in range(1, 11):
            name = word + str(i)
            save_path = save_to_dir + 'word_' + name + '.jpg'
            if not os.path.exists(save_path):
                print(name)
                is_found = save_word_image_to_dir(name, save_path)
                if not is_found:
                    break
                time.sleep(random.randint(1, 5))
                # a = pool.submit(save_word_image_to_dir, name, save_path)
