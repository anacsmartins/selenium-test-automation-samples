from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

test_case_id = "AUTH-TC-002"

def test_logout_authenticated_user():
    driver = webdriver.Chrome()
    driver.get("https://example.com/dashboard")

    # click logout button (hypothetical selector)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "logout-btn"))
    ).click()

    # assert user returned to login page
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username"))
    )

    assert "Login" in driver.page_source, f"Fail Test {test_case_id}"

    driver.quit()
