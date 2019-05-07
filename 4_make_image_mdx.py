from tqdm import tqdm
from writemdict.writemdict import MDictWriter
from PIL import Image
import io
import os


# ####################################################### build filter list
tst_txt = 'D:/github_project/make_anki_word_list/word_list/tst.txt'
all_word_txt = 'D:/github_project/make_anki_word_list/word_list/all_word_list.txt'

input_word_set = set()
with open(all_word_txt, 'r',encoding='utf-8') as f:
    word_list = f.read().splitlines()

word_list = sorted(word_list, key=str.lower)

for i in range(1, 11):
    root_dir = 'D:/github_project/word_root_spider/youdict_word_images/'
    mdx_dictionary = dict()
    mdd_dictionary = dict()
    for word in tqdm(word_list):
        word = word.strip()
        # print(word)
        if os.path.exists(root_dir+word+str(i)+'.jpg'):
            image = Image.open(root_dir+word+str(i)+'.jpg')
            output = io.BytesIO()
            image.save(output, format='JPEG')
            hex_data = output.getvalue()

            mdx_dictionary[word] = "<img src='file:///"+word+str(i)+".jpg' />"
            mdd_dictionary["\\"+word+str(i)+".jpg"] = hex_data

    outfile_mdx = open("output/youdict_image_"+str(i)+".mdx", "wb")
    writer = MDictWriter(mdx_dictionary, "Youdict Image " + str(i), "Youdict mdx file")
    writer.write(outfile_mdx)
    outfile_mdx.close()

    outfile_mdd = open("output/youdict_image_"+str(i)+".mdd", "wb")
    writer = MDictWriter(mdd_dictionary, "Youdict Image " + str(i), "Youdict mdd file", is_mdd=True)
    writer.write(outfile_mdd)
    outfile_mdd.close()
