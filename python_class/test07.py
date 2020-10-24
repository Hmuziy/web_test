def get_url(driver,url):
    driver.get(url)
    driver.maximize_window()
def login_page(driver,username,pwd):
    driver.find_element_by_id("username").send_keys(username)
    driver.find_element_by_id("password").send_keys(pwd)
    driver.find_element_by_id("btnSubmit").click()
def search_key(driver,url,username,pwd,s_key):
    get_url(driver, url)
    login_page(driver, username, pwd)
    driver.find_element_by_xpath('//a[@title="零售出库"]').click()
    id_value = driver.find_element_by_xpath('//div[text()="零售出库"]/..').get_attribute("id")  # 获取id的值
    frame_value = id_value + "-frame"
    driver.switch_to.frame(frame_value)  # 通过id值切换页面
    driver.find_element_by_xpath('//div[@id="tablePanel"]//input[@id="searchNumber"]').send_keys(s_key)
    driver.find_element_by_id("searchBtn").click()
    find_result = driver.find_element_by_xpath('//tr[@id="datagrid-row-r1-2-0"]//div[contains(text(),314)]').text
    return find_result  #设置返回值，可供别人使用