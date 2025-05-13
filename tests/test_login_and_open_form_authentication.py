from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

def test_login_then_navigate_to_form_auth(driver):
    driver.get("https://the-internet.herokuapp.com/login")

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "username"))
    ).send_keys("tomsmith")

    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "flash.success"))
    )
    WebDriverWait(driver, 10).until(EC.url_contains("/secure"))
    assert "secure" in driver.current_url

    driver.get("https://the-internet.herokuapp.com")

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Form Authentication"))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "username"))
    )
    assert "login" in driver.current_url
    assert "Login Page" in driver.page_source

    os.makedirs("screenshots", exist_ok=True)
    driver.save_screenshot("screenshots/form_auth_returned.png")
