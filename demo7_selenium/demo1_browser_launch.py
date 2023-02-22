import time

from selenium import webdriver

d = webdriver.Chrome()
d.get("https://www.hackerrank.com/domains/python")
d.maximize_window()
print(d.title)
time.sleep(10)


# n = 5
# for i in range(n) :
#     print(i+1,end="")