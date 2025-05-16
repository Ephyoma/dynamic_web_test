from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

def test_full_login_logout_flow(driver):
    driver.get("https://the-internet.herokuapp.com/login")

    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "username"))
    ).send_keys("tomsmith")

    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    WebDriverWait(driver, 20).until(EC.url_contains("/secure"))
    assert "secure" in driver.current_url
    assert "You logged into a secure area!" in driver.page_source

    driver.find_element(By.LINK_TEXT, "Logout").click()

    try:
        WebDriverWait(driver, 20).until(EC.url_contains("/login"))
    except Exception as e:
        os.makedirs("screenshots", exist_ok=True)
        driver.save_screenshot("screenshots/logout_fail.png")
        raise e
