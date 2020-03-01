from bs4 import BeautifulSoup


def get_root_txt_from_etymonline_html_text(html_text):
    if 'No results were found for' in html_text:
        return ''
    Soup = BeautifulSoup(html_text, 'lxml')
    Soup = Soup.find(attrs={"lang": "en"})
    # Soup = Soup.find(attrs={"data-gr-c-s-loaded": "true"})
    Soup = Soup.find(attrs={"id": "root"})
    # Soup = Soup.find(attrs={"bis_skin_checked": "1"})
    Soup = Soup.find(attrs={"class": "container--1mazc"})
    # Soup = Soup.find(attrs={"class": "header header--1Mejf header__vanila--2dqaM"})
    Soup = Soup.find(attrs={"class": "main main--10rAd"})
    Soup = Soup.find(attrs={"class": "ant-row-flex ant-row-flex-space-around"})
    Soup = Soup.find(attrs={"class": "ant-col-xs-24 ant-col-sm-24 ant-col-md-24 ant-col-lg-17"})
    Soup = Soup.find(attrs={"class": "word--C9UPa word_4pc--2SZw8"})
    Soup = Soup.find(attrs={"class": "word__defination--2q7ZH undefined"})
    txt = Soup.get_text()
    txt = txt.replace('\r\n', '\\')
    txt = txt.replace('\n\n', '\\')
    txt = txt.replace('\n', '\\')
    return txt


if __name__ == '__main__':
    import os

    from_html_text_dir = 'etymonline_html_text'
    root_line_list = list()
    for file in os.listdir(from_html_text_dir):
        html_text_path = os.path.join(from_html_text_dir, file)
        with open(html_text_path, 'r', encoding='utf-8') as f:
            html_txt = f.read()
        root_txt = get_root_txt_from_etymonline_html_text(html_txt)
        root_line_list.append(file[5:-4] + '\\' + root_txt)

    save_to_txt = 'etymonline_root.txt'
    with open(save_to_txt, 'w', encoding='utf-8') as f:
        for line in root_line_list:
            f.write(line)
            f.write('\n')

