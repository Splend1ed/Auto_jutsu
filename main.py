import mss.tools
import pytesseract
import cv2
import pyautogui
from time import sleep, localtime, strftime
import os

pytesseract.pytesseract.tesseract_cmd = 'D:\\Tesseract\\tesseract.exe'


# Create screenshots
def screenshot():
    with mss.mss() as sct:
        button_skip = {"top": 1355, "left": 15, "width": 150, "height": 30}
        button_next = {"top": 1355, "left": 2405, "width": 140, "height": 30}
        button_ad = {"top": 825, "left": 1330, "width": 130, "height": 90}
        skip_sct = "skip.png".format(**button_skip)
        next_sct = "next.png".format(**button_next)
        ad_sct = "ad.png".format(**button_ad)

        next_img = sct.grab(button_next)
        skip_img = sct.grab(button_skip)
        ad_img = sct.grab(button_ad)

        mss.tools.to_png(skip_img.rgb, skip_img.size, output=skip_sct)
        mss.tools.to_png(next_img.rgb, next_img.size, output=next_sct)
        mss.tools.to_png(ad_img.rgb, ad_img.size, output=ad_sct)


# Read text from picture
def read():
    img_next = cv2.imread('next.png')
    img_next = cv2.cvtColor(img_next, cv2.COLOR_BGR2RGB)
    img_skip = cv2.imread('skip.png')
    img_skip = cv2.cvtColor(img_skip, cv2.COLOR_BGR2RGB)
    img_ad = cv2.imread('ad.png')
    img_ad = cv2.cvtColor(img_ad, cv2.COLOR_BGR2RGB)
    ai_next = pytesseract.image_to_string(img_next, lang='rus', config='--psm 7')
    ai_skip = pytesseract.image_to_string(img_skip, lang='rus', config='--psm 7')
    ai_ad = pytesseract.image_to_string(img_ad, config='--psm 7')
    return ai_skip, ai_next, ai_ad


# Main function
# Moving and click mouse
def main():
    while True:
        if strftime("%H:%M:%S", localtime()) == '03:00:10':
            os.system("shutdown /p")
            break
        else:
            screenshot()
            if 'Следующая серия' in str(read()[1]):
                # press button "next episode" in full screen
                pyautogui.moveTo(2450, 1360)
                pyautogui.click()
                sleep(2)
                # press play button
                pyautogui.moveTo(1150, 840)
                pyautogui.click()
                sleep(2)
                # press button full screen
                pyautogui.moveTo(1430, 900)
                pyautogui.click()
                sleep(2)
            elif 'Skip Ad' in str(read()[2]):
                # press button skip ad
                pyautogui.moveTo(1400, 950)
                pyautogui.click()
                sleep(2)
                # press button full screen
                pyautogui.moveTo(1430, 900)
                pyautogui.click()
                sleep(2)
            elif'Пропустить заставку' in str(read()[0]):
                # press button skip opening
                pyautogui.moveTo(90, 1360)
                pyautogui.click()
                sleep(2)
                pyautogui.moveTo(1555, 966)


main()
