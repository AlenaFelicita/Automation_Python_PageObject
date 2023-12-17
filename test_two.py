import time

import pytest
from testpage import OperationHelper
username = "Alena808"
password = "sb23re1a"

def test_step_1(browser):
    test_page1 = OperationHelper(browser)
    test_page1.go_to_site()
    test_page1.enter_login("Alena808")
    test_page1.enter_pswd("sb23re1a")
    test_page1.click_button()
    time.sleep(3)
  
    test_page1.click_contact()
    time.sleep(3)
    
    test_page1.enter_cont_name("Alena808")
    test_page1.enter_cont_email("mail@yandex.ru")
    test_page1.enter_cont_text("Hi, Alena!")
    time.sleep(1)
    
    test_page1.click_button()
    time.sleep(1)

    assert test_page1.get_alert_text() == "Form successfully submitted"
