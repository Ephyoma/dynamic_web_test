from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_form_auth_flow(driver):
    # Step 1: Go to the login page
    driver.get("https://the-internet.herokuapp.com/login")

    # Step 2: Log in (first time)
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # Step 3: Wait for secure area and assert successful login
    WebDriverWait(driver, 10).until(EC.url_contains("/secure"))
    assert "secure" in driver.current_url
    assert "You logged into a secure area!" in driver.page_source

    # Step 4: Go back to the homepage
    driver.get("https://the-internet.herokuapp.com")

    # Step 5: Open "Form Authentication" again
    driver.find_element(By.LINK_TEXT, "Form Authentication").click()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "username"))
    )

    # Step 6: Fill the form again (interact with fields like a real user)
    username_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.ID, "password")

    # Clear and retype
    username_field.clear()
    password_field.clear()
    username_field.send_keys("tomsmith")
    password_field.send_keys("SuperSecretPassword!")

    # Step 7: Submit form
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # Step 8: Validate success again
    WebDriverWait(driver, 10).until(EC.url_contains("/secure"))
    assert "You logged into a secure area!" in driver.page_source

    # Optional: Screenshot result
    driver.save_screenshot("screenshots/form_auth_success.png")
