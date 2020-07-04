from tqdm import tqdm
from utils.writemdict.writemdict import MDictWriter
from PIL import Image
import io
import os

# ####################################################### build filter list
from utils.word_list.all_words_list import all_words_list

for i in range(1, 11):
    print(i)
    root_dir = './quword_images/'
    mdx_dictionary = dict()
    mdd_dictionary = dict()
    for word in tqdm(all_words_list):
        word = word.strip()
        # print(word)
        if os.path.exists(root_dir + 'word_' + word + str(i) + '.jpg'):
            image = Image.open(root_dir + 'word_' + word + str(i) + '.jpg')
            output = io.BytesIO()
            image.save(output, format='JPEG')
            hex_data = output.getvalue()
            mdx_dictionary[word] = """<img src="file:///""" + word + """.png" />"""
            mdd_dictionary["\\" + word + ".png"] = hex_data

    writer = MDictWriter(mdx_dictionary, "Youdict Image " + str(i), "Youdict mdx file")
    with open("../output_mdx/Quword_images{:0>2d}.mdx".format(i), "wb") as f:
        writer.write(f)

    writer = MDictWriter(mdd_dictionary, "Youdict Image " + str(i), "Youdict mdd file", is_mdd=True)
    with open("../output_mdx/Quword_images{:0>2d}.mdd".format(i), "wb") as f:
        writer.write(f)
