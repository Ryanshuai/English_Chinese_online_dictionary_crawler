import os
import yaml


class Yaml_Root:
    def __init__(self):
        with open('D:/github_project/make_anki_word_list/yaml_root/1 词缀词根.yaml', encoding='utf-8') as f:
            self.root_content = yaml.load(f)
        with open('D:/github_project/make_anki_word_list/yaml_root/2 单词列表.yaml', encoding='utf-8') as f:
            word_content = yaml.load(f)
            self.word_dict = dict()
            for word_context in word_content:
                word = word_context[0]
                root = word_context[1][0][2]
                self.word_dict[word] = root

    def get_root(self, word):
        if word in self.word_dict:
            return self.word_dict[word]
        else:
            return ''

    # def order_word_list(self, word_list):
    #     for root_ in self.root_content:
    #         root_1 = root_[0] + ':' + root_[1] + ' ' + root_[2]
    #         for word_ in root_[3]:
    #             word = word_[0]
    #             if word in filter_word_list:
    #                 for w in word_content:
    #                     if w[0] == word:
    #                         root_2 = w[1][0][2]
    #                 line = word + '\\' + root_1 + '\\' + root_2
    #                 f.write(line)
    #                 f.write('\n')
    #                 if word in input_word_list:
    #                     input_word_list.remove(word)


# with open('anki_word_list.txt', 'w', encoding='utf-8') as f:
#     for root_ in root_content:
#         root_1 = root_[0] + ':' + root_[1] + ' ' + root_[2]
#         for word_ in root_[3]:
#             word = word_[0]
#             if word in filter_word_list:
#                 for w in word_content:
#                     if w[0] == word:
#                         root_2 = w[1][0][2]
#                 line = word + '\\' + root_1 + '\\' + root_2
#                 f.write(line)
#                 f.write('\n')
#                 if word in input_word_list:
#                     input_word_list.remove(word)
#
# print(input_word_list)
# print(len(input_word_list))


if __name__ == '__main__':
    yr = Yaml_Root()
    print(yr.get_root('abandon'))
