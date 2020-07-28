from tqdm import tqdm
from utils.writemdict.writemdict import MDictWriter
from PIL import Image
import io
import os

# ####################################################### build filter list
from utils.word_list.all_words_list import all_words_list

num = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
for i, num in enumerate(num):
    print(i + 1)
    root_dir = './quword_images/'
    mdx_dictionary = dict()
    mdd_dictionary = dict()
    for word in tqdm(all_words_list):
        word = word.strip()
        # print(word)
        if os.path.exists(root_dir + 'word_' + word + str(i + 1) + '.jpg'):
            image = Image.open(root_dir + 'word_' + word + str(i + 1) + '.jpg')
            output = io.BytesIO()
            image.save(output, format='JPEG')
            hex_data = output.getvalue()
            mdx_dictionary[word] = """<img src="file:///""" + word + """.png" />"""
            mdd_dictionary["\\" + word + ".png"] = hex_data

    writer = MDictWriter(mdx_dictionary, "Youdict Image " + num, "Youdict mdx file")
    with open("../output_mdx/Quword_images_{}.mdx".format(num), "wb") as f:
        writer.write(f)

    writer = MDictWriter(mdd_dictionary, "Youdict Image " + num, "Youdict mdd file", is_mdd=True)
    with open("../output_mdx/Quword_images_{}.mdd".format(num), "wb") as f:
        writer.write(f)
