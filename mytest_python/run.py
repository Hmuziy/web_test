from selenium import webdriver
from python_class import test07
from test_data import test_date
driver = webdriver.Chrome()
driver.implicitly_wait(10)
url = test_date.url["url"]
username = test_date.user_info["username"]
pwd = test_date.user_info["pwd"]
s_key = test_date.s_key["s_key"]
find_result = test07.search_key(driver=driver,url=url,username=username,pwd=pwd,s_key=s_key)
if s_key not in find_result :
    print("没有找到该订单")
else:
    print("该订单的单据编号为:{}".format(find_result))