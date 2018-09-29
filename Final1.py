from selenium import webdriver
import cv2
import pyautogui as pag
import sys
import webbrowser
import time

aa = 0
browser = webdriver.Firefox()

def click(url):
    sys.path.append("libs")
    webbrowser.open(url)
    webbrowser.get()
    time.sleep(5)
    for _ in range(0, 5):
        time.sleep(1)
        pag.click(1537, 817, button="left")  # 点5下
    pag.click(1893, 10, button="left")      # 关闭

def find(word):
    start = word.find("http://live.bilibili.com")         # 先找到网站的位置
    box = word[int(start):int(start+35)]
    end = box.find("?")
    url = box[0:end]
    return url

if __name__ == '__main__':
    count = 0
    cv2.imshow("1", aa)

    browser.get("https://live.bilibili.com/9486749")
    # browser.get("https://live.bilibili.com/2734726")
    print('success')
    while True:
        if  cv2.waitKey(10000)  &  0xFF == ord('q'):  # 按q显示
            print(browser.page_source)
            print("######################")
            print(count)
        # time.sleep(10)
        url = find(browser.page_source)
        if url != "":
            count += 1
            print(count)
            click(url)
            browser.refresh()