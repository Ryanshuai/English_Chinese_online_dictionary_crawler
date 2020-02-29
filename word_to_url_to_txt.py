import requests


def word_to_url(word, web):
    if web == 'etymonline':
        return 'https://www.etymonline.com/search?q=' + word
    if web == 'quword':
        return 'https://www.quword.com/w/' + word


def url_to_html_text(url):
    head = {
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
    html = requests.get(url, headers=head, verify=False)
    html.encoding = 'utf-8'

    # p = requests.get('http://icanhazip.com', headers=head, proxies=proxy)
    # print('------------------------')
    # print(p.text)
    return html.text
