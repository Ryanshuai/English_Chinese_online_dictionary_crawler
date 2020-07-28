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
    if '词源不详。' in root:
        return ''
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


if __name__ == '__main__':
    word = 'make'

    url = 'https://www.youdict.com/w/abjure'
    ip_list = get_dynamic_ip()
    print(ip_list)
    html = get_html(url, ip_list[2])
    root = get_root_txt_from_youdict_html_text(html.text)
    print(root)
    mem = get_mem_txt_from_youdict_html_text(html.text)
    print(mem)
