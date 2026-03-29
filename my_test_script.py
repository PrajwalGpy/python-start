from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

try:
    driver.get('https://www.youtube.com/')

    wait = WebDriverWait(driver,10)

    searh_bar = wait.until(EC.presence_of_element_located((By.NAME,'search_query')))

    searh_bar.send_keys("Prajwal")
    searh_bar.send_keys(Keys.RETURN)

    wait.until(EC.presence_of_element_located((By.ID,'video-title')))

    vedios = driver.find_elements(By.ID,'video-title')

    for i,vedio in  enumerate(vedios,1):
        title = vedio.text
        if title:
            print(f"{i}----{title}")
        

    import time
    time.sleep(5)
finally:
    print("dONE all code working fine hii")



