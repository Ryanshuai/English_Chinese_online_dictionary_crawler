from bs4 import BeautifulSoup


def get_root_txt_from_youdict_html_text(html_text):
    Soup = BeautifulSoup(html_text, 'lxml')
    Soup = Soup.find(attrs={"id": "youdict"})
    Soup = Soup.find_all(attrs={"class": "container"})[-1]
    Soup = Soup.find(attrs={"class": "row"})
    Soup = Soup.find(attrs={"class": "col-sm-8"})
    Soup = Soup.find(attrs={"id": "yd-ciyuan"})
    root_txt = ''
    if Soup is not None:
        soup_p = Soup.find('p')
        if soup_p is None:
            root_txt += Soup.get_text()
        else:
            root_txt += soup_p.get_text()

    return root_txt


def get_mem_txt_from_youdict_html_text(html_text):
    Soup = BeautifulSoup(html_text, 'lxml')
    Soup = Soup.find(attrs={"id": "youdict"})
    Soup = Soup.find_all(attrs={"class": "container"})[-1]
    Soup = Soup.find(attrs={"class": "row"})
    Soup = Soup.find(attrs={"class": "col-sm-8"})
    Soup_1 = Soup.find(attrs={"class": "page-header"})
    if Soup_1 is None:
        return ''
    if '记忆方法' == Soup_1.get_text():
        Soup_2 = Soup.find(attrs={"style": "font-family:SimSun,serif;"})
        txt = Soup_2.get_text()
        txt = txt.replace('\r\n', '\\')
        txt = txt.replace('\n\n', '\\')
        txt = txt.replace('\n', '\\')
        return txt
    else:
        return ''


def get_root_txt_from_etymonline_html_text(html_text):
    Soup = BeautifulSoup(html_text, 'lxml')
    Soup = Soup.find(attrs={"data-gr-c-s-loaded": "true"})
    Soup = Soup.find(attrs={"id": "root"})
    Soup = Soup.find(attrs={"bis_skin_checked": "1"})
    Soup = Soup.find(attrs={"class": "container--1mazc"})
    Soup = Soup.find(attrs={"class": "header header--1Mejf header__vanila--2dqaM"})
    Soup = Soup.find(attrs={"class": "main main--10rAd"})
    Soup = Soup.find(attrs={"class": "ant-row-flex ant-row-flex-space-around"})
    Soup = Soup.find(attrs={"class": "ant-col-xs-24 ant-col-sm-24 ant-col-md-24 ant-col-lg-17"})
    Soup = Soup.find(attrs={"class": "word--C9UPa word_4pc--2SZw8"})
    Soup = Soup.find(attrs={"class": "heade"})
    Soup = Soup.find(attrs={"class": "heade"})
    Soup = Soup.find(attrs={"class": "heade"})
    return Soup


if __name__ == '__main__':
    # ws = Word_Spider()
    # txt = ws.get_men_root('dictator')
    # print(txt)

    url = 'https://www.youdict.com/w/abjure'
    ip_list = get_dynamic_ip()
    print(ip_list)
    html = get_html(url, ip_list[2])
    root = get_root_txt_from_youdict_html_text(html.text)
    print(root)
    mem = get_mem_txt_from_youdict_html_text(html.text)
    print(mem)

