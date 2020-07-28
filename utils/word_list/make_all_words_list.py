import os


# def txt_to_set(input_file):
#     all_set = set()
#     for txt in os.listdir(input_file):
#         file = os.path.join(input_file, txt)
#         with open(file, encoding='utf-8') as f:
#             file_set = set(f.read().splitlines())
#             all_set |= file_set


def txt_to_set(input_file):
    with open(input_file, encoding='utf-8') as f:
        file_set = set(f.read().splitlines())
    return file_set


def filter_the_word(word):
    english_only_word = ''.join(x for x in word if ord(x) < 256)
    no_comma_word = ''.join(x for x in english_only_word if x != ",")
    return no_comma_word


def make_all_list(all_set, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('all_words_list = [')
        for word in all_set:
            word = filter_the_word(word)
            if len(word) <= 1:
                continue
            f.write('"')
            f.write(word)
            f.write('",\n')
        f.write(']')


if __name__ == '__main__':
    input_file = "word_list_txt/TOEFL_red.txt"
    output_file = "word_list_py/TOEFL_red.py"

    word_set = txt_to_set(input_file)
    make_all_list(word_set, output_file)
