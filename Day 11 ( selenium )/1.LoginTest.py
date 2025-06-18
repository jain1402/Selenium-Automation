from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Create a driver instance
driver = webdriver.Chrome()  # Capitalize 'Chrome'
# https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "username")))

driver.find_element(By.NAME,"username").send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys("admin123")
driver.find_element(By.CSS_SELECTOR, ".oxd-button.oxd-button--medium.oxd-button--main.orangehrm-login-button").click()

act_title= driver.title
exp_title = "OrangeHRM"

if act_title==exp_title:
    print("Login test passed")
else:
    print("Login test failed")


input("Press Enter to close the browser...")

driver.quit()
