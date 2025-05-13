from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_full_login_logout_flow(driver):
    # Step 1: Open login page
    driver.get("https://the-internet.herokuapp.com/login")

    # Step 2: Perform login
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # Step 3: Confirm login success
    WebDriverWait(driver, 10).until(EC.url_contains("/secure"))
    assert "secure" in driver.current_url
    assert "You logged into a secure area!" in driver.page_source

    # Step 4: Click logout button
    driver.find_element(By.LINK_TEXT, "Logout").click()

    # Step 5: Verify redirection back to login page
    WebDriverWait(driver, 10).until(EC.url_contains("/login"))
    assert "login" in driver.current_url
    assert "You logged out of the secure area!" in driver.page_source

    # Optional: Screenshot the result
    driver.save_screenshot("screenshots/logout_confirmation.png")
