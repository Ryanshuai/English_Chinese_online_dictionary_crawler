from utils.word_list.word_list_py.all_words_list import all_words_list
from txt_to_dict import Backslash_Txt_Dict

dict_class = Backslash_Txt_Dict('enExplain.txt', 'English_Explain.mdx')
dict_class.generate_dict(set(all_words_list))
