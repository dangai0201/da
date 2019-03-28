# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("http://192.168.43.129:811/ecshop/upload/")

#方法1
# window=driver.window_handles
# print(window)
# driver.find_element_by_css_selector("body > div.indexw_foot_service > div > div.indexw_foot_service_middle > ul:nth-child(1) > li:nth-child(2) > a").click()
# windows=driver.window_handles
# print(windows)
# driver.switch_to.window(windows[-1])
# a=driver.find_element_by_class_name("tc").text
# print(a)

#方法2
# driver.find_element_by_css_selector("body > div.indexw_foot_service > div > div.indexw_foot_service_middle > ul:nth-child(1) > li:nth-child(2) > a").click()
# window1=driver.current_window_handle
# print(window1)
# windows=driver.window_handles
# print(windows)
# for cureent_window in windows:
#     if cureent_window!=window1:
#         driver.switch_to.window(cureent_window)
#
# a=driver.find_element_by_class_name("tc").text
# b="售后流程"
# if b in a:
#     print("成功")
# else:
#     print("失败")

# [::-1] 顺序相反操作
# [-1] 读取倒数第一个元素
# [3::-1] 从下标为3（从0开始）的元素开始翻转读取
a=[1,2,3,4,5]
b=a[::-1]
print(b)
b1=a[-1]
print(b1)
b2=a[3::-1]
print(b2)







