from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Util:
  def __init__(self, driver, delay=3):
    self.driver = driver
    self.delay = delay
  
  def find_element_by_xpath(self, xpath):
    return WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located((By.XPATH, xpath)))