from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Scenario: Username benar dan password benar


driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/login")

driver.find_element(By.ID, "username").send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

time.sleep(2)

success_message = driver.find_element(By.ID, "flash").text

if "You logged into a secure area!" in success_message:
    print("Scenario 1 : PASSED (Login Success)")
else:
    print("Scenario 1 : FAILED (Login Failed)")

driver.quit()


# Scenario: Username benar dan password salah


driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/login")

driver.find_element(By.ID, "username").send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("wrongpassword")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

time.sleep(2)

error_message = driver.find_element(By.ID, "flash").text

if "Your password is invalid!" in error_message:
    print("Scenario 2 : PASSED (Invalid Password Detected)")
else:
    print("Scenario 2 : FAILED")

driver.quit()

print("\nAll test scenarios completed.")