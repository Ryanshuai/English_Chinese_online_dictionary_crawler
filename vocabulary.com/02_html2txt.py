def get_enExplain_txt_from_vocabulary_html_text(html_text):
    html_text = html_text[24:-2]
    html_text = html_text.replace('n\\r\\n\\t\\t\\t\\t\\t\\t    ', '')
    html_text = html_text.replace('\\r\\n\\t\\t\\t\\t\\t\\t     ', '')
    html_text = html_text.replace('\\r\\n\\t\\t\\t\\t\\t\\t    ', '')
    html_text = html_text.replace('\\"', '\"')

    return html_text


if __name__ == '__main__':
    import os

    word = 'make'
    from_html_text_dir = "vocabulary_html_text"

    enExplain_line_list = list()
    for file in os.listdir(from_html_text_dir):
        with open(os.path.join(from_html_text_dir, file), encoding='utf-8') as f:
            line = f.readline()
        enExplain = get_enExplain_txt_from_vocabulary_html_text(line)
        enExplain_line_list.append(file[5:-4] + '\\' + enExplain)

    save_to_txt = 'enExplain.txt'
    with open(save_to_txt, 'w', encoding='utf-8') as f:
        for line in enExplain_line_list:
            f.write(line)
            f.write('\n')
