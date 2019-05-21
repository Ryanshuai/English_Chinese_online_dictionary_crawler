from pykeyboard import PyKeyboardEvent
from PIL import ImageGrab
import cv2
import os
import numpy as np
from find_word_by_image import find_word_by_image


class Key_listener(PyKeyboardEvent):
    def __init__(self):
        PyKeyboardEvent.__init__(self)
        if os.path.exists('num.txt'):
            with open('num.txt', 'r') as f:
                self.word_dict = eval(f.read())
        else:
            self.word_dict = dict()
        self.now_word = ''
        self.wait_for_front = True

    def tap(self, keycode, character, press):
        if (keycode == 32 or 13) and press and self.wait_for_front:  # front
            screen = ImageGrab.grab()
            screen = np.array(screen)
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)
            word = find_word_by_image(screen)
            self.now_word = word
            print(word)
            num = self.word_dict.get(word, 0)
            print('\n' )
            print((str(num)*100+'\n')* 80)
            self.wait_for_front = False

        elif (keycode == 32 or 13 or 98) and press and (not self.wait_for_front):  # back
            num = self.word_dict.get(self.now_word, 0)
            self.word_dict[self.now_word] = num + 1
            self.wait_for_front = True

        elif keycode == (96 or 97) and press and (not self.wait_for_front):  # 1
            self.word_dict[self.now_word] = 0
            self.wait_for_front = True

        # print(keycode, press)
        with open('num.txt', 'w') as f:
            f.write(str(self.word_dict))



t = Key_listener()
t.run()



