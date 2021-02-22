import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException        

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_should_see_button_basket(browser):
    browser.get(link)
    time.sleep(10)
    try:
        el = WebDriverWait(browser, 12).until(
                           EC.presence_of_element_located((By.CSS_SELECTOR,".btn.btn-lg.btn-primary.btn-add-to-basket")))
    except:     
        return False
    assert el.is_displayed() == True, f"Test should be ok"




 
                     