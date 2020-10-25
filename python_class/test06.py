from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://erp.lemfix.com")
driver.implicitly_wait(10)
driver.maximize_window()
driver.find_element_by_id("username").send_keys("test123")
driver.find_element_by_id("password").send_keys("123456")
driver.find_element_by_id("btnSubmit").click()

#验证页面标题
title1 = driver.find_element_by_xpath("//div[@class='login-box']//b").text   #层级定位
print(title1)
title2 = driver.find_element_by_xpath('//b[text()="柠檬ERP"]').text  #文本属性定位
print(title2)
title3 = driver.title   #通过title直接获取页面标题
print(title3)

#获取页面中的用户名
login_name = driver.find_element_by_xpath('//p[text()="测试用户"]').text
if login_name == "测试用户":
    print("用例通过")
else:
    print("用例不通过")

#点击零售出库
driver.find_element_by_xpath('//a[@title="零售出库"]').click()

#搜索单据编号
id_value = driver.find_element_by_xpath('//div[text()="零售出库"]/..').get_attribute("id") #获取id的值
# id_value = driver.find_element_by_xpath('//ul[@class="tabpanel_mover"]//li[2]').get_attribute("id")
frame_value = id_value + "-frame"
# print(frame_value)
driver.switch_to.frame(frame_value)   #通过id值切换页面
driver.find_element_by_xpath('//div[@id="tablePanel"]//input[@id="searchNumber"]').send_keys("314")
# driver.find_element_by_xpath('//div[@id="tablePanel"]//span[text()="查询"]').click()
driver.find_element_by_id("searchBtn").click()
find_result = driver.find_element_by_xpath('//tr[@id="datagrid-row-r1-2-0"]//div[contains(text(),314)]').text
if find_result == "":
    print("没有找到该订单")
else:
    print("该订单的单据编号为:{}".format(find_result))