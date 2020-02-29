import os

dir = 'D:\github_project\make_anki_word_list\etymonline\etymonline_html_text'
for name in os.listdir(dir):
    os.rename(os.path.join(dir, name), os.path.join(dir, 'word_' + name))
