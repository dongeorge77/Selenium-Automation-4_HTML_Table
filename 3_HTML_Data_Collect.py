from selenium import webdriver
driver=webdriver.Chrome()
driver.get("file:///C:/Users/ADMIN/PycharmProjects/8_Class_17_2_2019/HTML_Table/Table.html")
driver.maximize_window()
driver.implicitly_wait(30)

ele=driver.find_elements_by_xpath("//*[@id='Employe']/thead/tr/th")
#ele=driver.find_elements_by_xpath("//*[@id='Employe']/tbody/tr[1]")
print(ele)
for i in ele:
    print(i.text)