# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# driver=webdriver.Chrome()


# driver.get("https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/")
# driver.maximize_window()

# driver.find_element(By.XPATH,"//button[@id='comboTree353226ArrowBtn']//span[@class='comboTreeArrowBtnImg'][contains(text(),'▼')]").click()
# time.sleep(5)
# input("press Enter to close the browser... ")

# driver.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize WebDriver
driver = webdriver.Chrome()

# Open URL
driver.get("https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/")
driver.maximize_window()

# Wait for 5 seconds before interacting (to allow full page load)
time.sleep(5)

try:
    # Wait until the element is visible before clicking
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='comboTree353226ArrowBtn']/span"))
    )

    # Check if the element is actually interactable
    if element.is_displayed() and element.is_enabled():
        element.click()
        print("Dropdown button clicked successfully.")
    else:
        print("Dropdown button is present but not interactable.")

except Exception as e:
    print("Error:", e)

# Wait for user input before closing
input("Press Enter to close the browser... ")

# Quit driver
driver.quit()



