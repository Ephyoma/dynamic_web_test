from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_then_navigate_to_form_auth(driver):
    # Step 1: Go to the login page
    driver.get("https://the-internet.herokuapp.com/login")

    # Step 2: Log in with valid credentials
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # Step 3: Wait until redirected to secure area
    WebDriverWait(driver, 10).until(EC.url_contains("/secure"))
    assert "secure" in driver.current_url

    # Step 4: Navigate back to homepage
    driver.get("https://the-internet.herokuapp.com")

    # Step 5: Open "Form Authentication" again
    driver.find_element(By.LINK_TEXT, "Form Authentication").click()

    # Step 6: Confirm we're on the login page again
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username"))
    )
    assert "login" in driver.current_url
    assert "Login Page" in driver.page_source

    # Optional: Save screenshot
    driver.save_screenshot("screenshots/form_auth_returned.png")
