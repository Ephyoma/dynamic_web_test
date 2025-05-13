from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_open_form_authentication(driver):
    # Step 1: Go to the homepage
    driver.get("https://the-internet.herokuapp.com")

    # Step 2: Click the "Form Authentication" link
    driver.find_element(By.LINK_TEXT, "Form Authentication").click()

    # Step 3: Wait for the login form to be visible
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "username"))
    )

    # Step 4: Confirm we're on the login page
    assert "login" in driver.current_url
    assert "Login Page" in driver.page_source

    # Optional: Screenshot
    driver.save_screenshot("screenshots/form_auth_page.png")
