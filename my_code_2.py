from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
  link = "https://suninjuly.github.io/math.html"
  browser = webdriver.Chrome()
  browser.get(link)

  x_element = browser.find_element(By.ID, 'input_value')
  x = x_element.text
  y = calc(x)

  answer = browser.find_element(By.ID, 'answer')
  answer.send_keys(y)

  check_box = browser.find_element(By.ID, 'robotCheckbox')
  check_box.click()

  robot_rule = browser.find_element(By.ID, 'robotsRule')
  robot_rule.click()

  button = browser.find_element(By.TAG_NAME, "button")
  button.click()


#   print(x)
#   print(y)

finally:
  time.sleep(10)
  browser.quit()
