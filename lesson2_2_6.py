from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Firefox()
browser.implicitly_wait(5)
browser.get(link)
price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),'100'))
button = browser.find_element_by_xpath("//button[@id='book']")
button.click()
x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)
print("value of img: ", x)
print("value of img: ", y)
browser.execute_script("window.scrollBy(0, 300);")
input1 = browser.find_element_by_id("answer")
input1.send_keys(y)
button = browser.find_element_by_xpath("//button[@id='solve']")
button.click()
time.sleep(10)

browser.quit()