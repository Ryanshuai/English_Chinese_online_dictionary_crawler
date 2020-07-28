from utils.word_list.word_list_py.all_words_list import all_words_list
from txt_to_dict import Backslash_Txt_Dict

dict_class = Backslash_Txt_Dict('quword_mem.txt', 'quword_mem.mdx')
dict_class.generate_dict(set(all_words_list))

dict_class = Backslash_Txt_Dict('quword_root.txt', 'quword_root.mdx')
dict_class.generate_dict(set(all_words_list))
