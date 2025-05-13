from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

def test_dropdown_page(driver):
    # Step 1: Go to the dropdown page
    driver.get("https://the-internet.herokuapp.com/dropdown")

    # Step 2: Wait for dropdown to appear
    dropdown_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "dropdown"))
    )

    # Step 3: Interact with dropdown using Select
    dropdown = Select(dropdown_element)
    dropdown.select_by_value("2")  # Option 2

    # Step 4: Assert the selected option text
    selected_option = dropdown.first_selected_option
    assert selected_option.text == "Option 2", f"Expected 'Option 2' but got '{selected_option.text}'"

    # Optional: Screenshot
    driver.save_screenshot("screenshots/dropdown_selected_asserted.png")
