import time

from selenium.webdriver.common.by import By


class Wiki_GDP():
    row_length_XPATH= (By.XPATH,'//*[@id="mw-content-text"]/div[1]/table[2]/tbody/tr/td[1]')
    col_length_XPATH = (By.XPATH,'//*[@id="mw-content-text"]/div[1]/table[2]/tbody/tr[1]/td')





    def __init__(self, driver):
        self.driver = driver

    def Row_length(self):
        rw_len=len(self.driver.find_elements(*Wiki_GDP.row_length_XPATH))
        return rw_len

    def Col_length(self):
        col_len = len(self.driver.find_elements(*Wiki_GDP.col_length_XPATH))
        return col_len

    def scroll(self):
        m= self.driver.find_element(By.XPATH,"//tbody/tr[13]/td[1]")
        self.driver.execute_script('arguments[0].scrollIntoView();',m)

    def iteration(self,r,c):
        time.sleep(1)
        m=self.driver.find_element(By.XPATH,'//*[@id="mw-content-text"]/div[1]/table[2]/tbody/tr['+str(r)+']/td['+str(c)+']').text
        return m




