from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

test_case_id = "AUTH-TC-001"   # mapping TestRail reference

driver = webdriver.Chrome()
driver.get("https://example.com/login")

username = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "username"))
)
password = driver.find_element(By.ID, "password")

username.send_keys("valid_user")
password.send_keys("valid_pass")
driver.find_element(By.ID, "login-submit").click()

WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "header h1"), "Welcome")
)

assert "Welcome" in driver.page_source, f"Fail Test {test_case_id}"

driver.quit()
