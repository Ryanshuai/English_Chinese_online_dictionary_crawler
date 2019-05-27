
import time
import random
from os.path import normpath, join, exists
import requests
import os
import urllib3
import threading
from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def get_dynamic_ip():
    url = 'http://proxy.httpdaili.com/apinew.asp?sl=3&noinfo=true&ddbh=397693856548944151'
    html = requests.get(url)
    ip_list = html.text.split('\r\n')[0:3]
    # print(ip_list)
    return ip_list


def get_html_from_url(url, ip=None):
    if ip is None:
        head = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
        html = requests.get(url, headers=head, verify=False)
        html.encoding = 'utf-8'
    else:
        proxy = {'http': ip}
        head = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
        html = requests.get(url, headers=head, verify=False, proxies=proxy)
        html.encoding = 'utf-8'
    # p = requests.get('http://icanhazip.com', headers=head, proxies=proxy)
    # print('------------------------')
    # print(p.text)
    return html.text


def save_if_not_exist(word, base_url, save_dir):
    to_txt = normpath(join(save_dir, word + '.txt'))
    if not os.path.exists(to_txt):
        print(word, '\tbegin!')
        url = base_url + word
        html_text = get_html_from_url(url)
        with open(to_txt, 'w', encoding='utf-8') as f:
            f.write(html_text)
            print(word, '\tdone!')


def save_if_not_exist_for_youdict(word, base_url, save_dir):
    to_txt = normpath(join(save_dir, word + '.txt'))
    if not os.path.exists(to_txt):
        print('===============================', word, '\tbegin!')
        url = base_url + word
        html_text = get_html_from_url(url)
        with open(to_txt, 'w', encoding='utf-8') as f:
            f.write(html_text)
            print('===============================', word, '\tdone!')
    else:
        with open(to_txt, encoding='utf-8') as f:
            txt = f.read()
        if not txt.startswith('<!DOCTYPE html>'):
            print(word, '\tbegin!')
            url = base_url + word
            html_text = get_html_from_url(url)
            with open(to_txt, 'w', encoding='utf-8') as f:
                f.write(html_text)
                print(word, '\tdone!')


def one_thread_check_and_save(func, iterable, *args):
    for iter in iterable:
        func(iter, *args)
        t = random.uniform(0.01, 0.5)
        time.sleep(t)


def multi_thread(func, iterable, *args, max_workers=8):
    executor = ThreadPoolExecutor(max_workers=max_workers)
    all_task = [executor.submit(func, iter, *args,)
                for iter in iterable]
    wait(all_task, return_when=ALL_COMPLETED)


# def multi_thread_with_lock(func, read_iterable, writer_iterable, *args, max_workers=1280):
#     threading_list = list()
#     num_work = 0
#     for r_iter in read_iterable:
#         num_work += 1
#         t = threading.Thread(target=func, args=(r_iter, *args,))
#         threading_list.append(t)
#         t.start()
#     for t in threading_list:
#         t.join()




if __name__ == '__main__':
    # ws = Word_Spider()
    # txt = ws.get_men_root('dictator')
    # print(txt)

    url = 'https://www.youdict.com/w/abjure'
    ip_list = get_dynamic_ip()
    print(ip_list)
    html = get_html_from_url(url, ip_list[2])


