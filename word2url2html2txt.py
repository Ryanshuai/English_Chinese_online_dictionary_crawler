import requests ##导入requests
from bs4 import BeautifulSoup ##导入bs4中的BeautifulSoup
import telnetlib
import os


def get_dynamic_ip():
    url = 'http://proxy.httpdaili.com/apinew.asp?sl=3&noinfo=true&ddbh=397693856548944151'
    html = requests.get(url)
    ip_list = html.text.split('\r\n')[0:3]
    # print(ip_list)
    return ip_list


def get_html_from_url(url, ip=None):
    if ip is None:
        head = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}  ##浏览器请求头（大部分网站没有这个请求头会报错、请务必加上哦）
        html = requests.get(url, headers=head, verify=False)
        html.encoding = 'utf-8'
        return html
    else:
        proxy = {'http': ip}
        head = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}  ##浏览器请求头（大部分网站没有这个请求头会报错、请务必加上哦）
        html = requests.get(url, headers=head, verify=False, proxies=proxy)
        html.encoding = 'utf-8'
    # p = requests.get('http://icanhazip.com', headers=head, proxies=proxy)
    # print('------------------------')
    # print(p.text)
    return html.text


def get_word_html_text_from_web(word):
    url = 'https://www.youdict.com/w/' + word
    html_text = get_html_from_url(url)
    save_word_html_text_to_dir(word, html_text)
    return html_text


def save_word_html_text_to_dir(word, html_text, dire='youdict_word_html/'):
    to_txt = dire+word+'.txt'
    with open(to_txt, 'w', encoding='utf-8') as f:
        f.write(html_text)


def get_word_html_text_from_txt_dir(word):  # .txt must exists
    html_text_dir = 'D:\github_project\make_anki_word_list\youdict_word_html/'
    html_text_path = html_text_dir + '\\' + word + '.txt'
    with open(html_text_path, 'r', encoding='utf-8') as f:
        html_text = f.read()
    return html_text


def get_word_html_from_everywhere(word):
    if os.path.exists('D:\github_project\make_anki_word_list\youdict_word_html/' + word + '.txt'):
        html_text = get_word_html_text_from_txt_dir(word)
    else:
        html_text = get_word_html_text_from_web(word)
    return html_text


def get_root_txt_from_html_text(html_text):
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


def get_mem_txt_from_html_text(html_text):
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
        txt = txt.replace('\n', '\\')
        return txt
    else:
        return ''


if __name__ == '__main__':
    # ws = Word_Spider()
    # txt = ws.get_men_root('dictator')
    # print(txt)

    url = 'https://www.youdict.com/w/abjure'
    ip_list = get_dynamic_ip()
    print(ip_list)
    html = get_html(url, ip_list[2])
    root = get_root_txt_from_html_text(html.text)
    print(root)
    mem = get_mem_txt_from_html_text(html.text)
    print(mem)

