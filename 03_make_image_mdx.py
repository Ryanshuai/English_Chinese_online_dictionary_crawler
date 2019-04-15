from tqdm import tqdm
from writemdict.writemdict import MDictWriter
from PIL import Image
import io



# ####################################################### build filter list
tst_txt = 'D:/github_project/make_anki_word_list/kinds_of_word_list/tst.txt'
cet4_txt = 'D:/github_project/make_anki_word_list/kinds_of_word_list/4-cet.txt'
cet6_txt = 'D:/github_project/make_anki_word_list/kinds_of_word_list/6-cet.txt'
post_txt = 'D:/github_project/make_anki_word_list/kinds_of_word_list/考研词汇表.txt'
toefl_qu_txt = 'D:/github_project/make_anki_word_list/kinds_of_word_list/曲根10000词汇表.txt'
toefl_red_txt = 'D:/github_project/make_anki_word_list/kinds_of_word_list/托福红宝书.txt'
toefl_class = 'D:/github_project/make_anki_word_list/kinds_of_word_list/分类词汇.txt'
gre300_txt = 'D:/github_project/make_anki_word_list/kinds_of_word_list/3000.txt'
gre_foot_txt = 'D:/github_project/make_anki_word_list/kinds_of_word_list/佛脚词.txt'
gre_red_txt = 'D:/github_project/make_anki_word_list/kinds_of_word_list/gre红宝书.txt'

input_txt_list = list()
input_txt_list.append(tst_txt)
# input_txt_list.append(cet4_txt)
# input_txt_list.append(cet6_txt)
# input_txt_list.append(post_txt)
# input_txt_list.append(toefl_qu_txt)
# input_txt_list.append(toefl_red_txt)
# input_txt_list.append(gre300_txt)
# input_txt_list.append(gre_foot_txt)
# input_txt_list.append(gre_red_txt)


input_word_set = set()
for file in input_txt_list:
    with open(file, 'r',encoding='utf-8') as f:
        word_list = f.read().splitlines()
        input_word_set |= set(word_list)

for i in range(1, 11):
    root_dir = 'D:/github_project/word_root_spider/youdict_word_images/'
    mdx_dictionary = dict()
    mdd_dictionary = dict()
    for word in tqdm(input_word_set):
        image = Image.open(root_dir+word+str(i)+'.jpg')
        output = io.BytesIO()
        image.save(output, format='JPEG')
        hex_data = output.getvalue()

        if image is not None:
            mdx_dictionary[word] = "<img src='file:///"+word+str(i)+"' />"
            mdd_dictionary["\\"+word+str(i)] = hex_data

    outfile_mdx = open("output/youdict_image_"+str(i)+".mdx", "wb")
    writer = MDictWriter(mdx_dictionary, "Youdict Image " + str(i), "Youdict mdx file")
    writer.write(outfile_mdx)
    outfile_mdx.close()

    outfile_mdd = open("output/youdict_image_"+str(i)+".mdd", "wb")
    writer = MDictWriter(mdd_dictionary, "Youdict Image " + str(i), "Youdict mdd file", is_mdd=True)
    writer.write(outfile_mdd)
    outfile_mdd.close()