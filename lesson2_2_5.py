from selenium import webdriver
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Firefox()
browser.get(link)
button = browser.find_element_by_xpath("//button[@type='submit']")
button.click()
time.sleep(1)
new_window = browser.window_handles[1]
first_window = browser.window_handles[0]
browser.switch_to.window(new_window)
x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)
print("value of img: ", x)
print("value of img: ", y)
browser.execute_script("window.scrollBy(0, 300);")
input1 = browser.find_element_by_id("answer")
input1.send_keys(y)
button = browser.find_element_by_xpath("//button[@type='submit']")
button.click()
time.sleep(10)
browser.quit()