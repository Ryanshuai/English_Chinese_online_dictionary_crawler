import requests
from PIL import Image
from io import BytesIO
import os
import time
import random

from PIL import ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True


def save_word_image_to_dir(name, save_path):
    url = 'https://www.quword.com/images/words/' + name + '.jpg'
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

    form_num = 0
    for i, word in enumerate(all_words_list[form_num:]):
        print(i + form_num)
        word = word.strip()
        for i in range(1, 11):
            name = word + str(i)
            save_path = save_to_dir + 'word_' + name + '.jpg'
            if not os.path.exists(save_path):
                is_found = save_word_image_to_dir(name, save_path)
                if not is_found:
                    break
                # time.sleep(random.random() * 0.2)
