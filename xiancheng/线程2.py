#-*-coding:utf-8-*-
import os,sys
os.getcwd()
sys.path.append(os.getcwd())
import threading, time
from selenium import webdriver


def test_baidu(browser, search):
    print('start---%s' % time.ctime())
    print('browser is %s' % browser)
    if browser == 'Chrome':
      driver = webdriver.Chrome()
    elif browser == 'FireFox':
      driver = webdriver.Firefox()
    else:
        print(u'浏览器只能为Chrome或FireFox')

    driver.get('https://www.baidu.com')
    driver.find_element_by_id('kw').send_keys(search)
    driver.find_element_by_id('su').click()
    time.sleep(2)
    driver.quit()


if __name__ == '__main__':
    # 启动参数，指定浏览器和搜索内容
    lists = {'Chrome': u'大连一方', 'FireFox': u'中国大连'}

    thread = []
    files = range(len(lists))
    # 创建线程
    for browser,search in lists.items():
        t = threading.Thread(target=test_baidu, args=(browser, search))
        thread.append(t)
    # 启动线程
    for i in files:
        thread[i].start()
    for i in files:
        thread[i].join()
    print('all end---%s' % time.ctime())


