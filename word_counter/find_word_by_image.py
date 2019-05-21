import cv2
import pytesseract


def find_word_by_image(screen):
    crop_im = screen[360: 410, 635: 1055, :]
    crop_im = cv2.cvtColor(crop_im, cv2.COLOR_BGR2GRAY)
    ret, crop_im = cv2.threshold(crop_im, 127, 255, cv2.THRESH_BINARY)
    # cv2.imshow('1111', crop_im)
    # cv2.waitKey()
    crop_im = 255 - crop_im
    # cv2.imshow('BINARY', crop_im)
    # cv2.waitKey()
    word = pytesseract.image_to_string(crop_im)
    return word


if __name__ == '__main__':
    im = cv2.imread('1.png')
    word = find_word_by_image(im)
    print(word)

