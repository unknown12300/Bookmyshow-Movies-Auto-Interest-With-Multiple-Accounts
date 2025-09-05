# for more emails want means add..
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

email_list = [
"abc1@gmail.com",
"abc2@gmail.com",
"abc3@gmail.com",
"abc4@gmail.com",
"abc5@gmail.com",
"abc6@gmail.com",
"abc7@gmail.com",
"abc8@gmail.com",
"abc9@gmail.com",
"abc10@gmail.com",
"abc11@gmail.com",
"abc12@gmail.com",
"abc13@gmail.com",
"abc14@gmail.com",
"abc15@gmail.com",
"abc16@gmail.com",
"abc17@gmail.com",
"abc18@gmail.com",
"abc19@gmail.com",
"abc20@gmail.com",
"abc21@gmail.com",
"abc22@gmail.com",
"abc23@gmail.com",
"abc24@gmail.com",
"abc25@gmail.com",
"abc26@gmail.com",
"abc27@gmail.com",
"abc28@gmail.com",
"abc29@gmail.com",
"abc30@gmail.com",
"abc31@gmail.com",
"abc32@gmail.com",
"abc33@gmail.com",
"abc34@gmail.com",
"abc35@gmail.com",
"abc36@gmail.com",
"abc37@gmail.com",
"abc38@gmail.com",
"abc39@gmail.com",
"abc40@gmail.com",
"abc41@gmail.com",
"abc42@gmail.com",
"abc43@gmail.com",
"abc44@gmail.com",
"abc45@gmail.com",
"abc46@gmail.com",
"abc47@gmail.com",
"abc48@gmail.com",
"abc49@gmail.com",
"abc50@gmail.com",
"abc51@gmail.com",
"abc52@gmail.com",
"abc53@gmail.com",
"abc54@gmail.com",
"abc55@gmail.com",
"abc56@gmail.com",
"abc57@gmail.com",
"abc58@gmail.com",
"abc59@gmail.com",
"abc60@gmail.com",
"abc61@gmail.com",
"abc62@gmail.com",
"abc63@gmail.com",
"abc64@gmail.com",
"abc65@gmail.com",
"abc66@gmail.com",
"abc67@gmail.com",
"abc68@gmail.com",
"abc69@gmail.com",
"abc70@gmail.com",
"abc71@gmail.com",
"abc72@gmail.com",
"abc73@gmail.com",
"abc74@gmail.com",
"abc75@gmail.com",
"abc76@gmail.com",
"abc77@gmail.com",
"abc78@gmail.com",
"abc79@gmail.com",
"abc80@gmail.com",
"abc81@gmail.com",
"abc82@gmail.com",
"abc83@gmail.com",
"abc84@gmail.com",
"abc85@gmail.com",
"abc86@gmail.com",
"abc87@gmail.com",
"abc88@gmail.com",
"abc89@gmail.com",
"abc90@gmail.com",
"abc91@gmail.com",
"abc92@gmail.com",
"abc93@gmail.com",
"abc94@gmail.com",
"abc95@gmail.com",
"abc96@gmail.com",
"abc97@gmail.com",
"abc98@gmail.com",
"abc99@gmail.com",
"abc100@gmail.com"
]



option = webdriver.ChromeOptions()
option.add_experimental_option("debuggerAddress", "localhost:9222")
driver = webdriver.Chrome(options=option)
driver.maximize_window()


def visit_bookmyshow():
    """Visit the movie page."""
    driver.get("https://in.bookmyshow.com/movies/bengaluru/mark/ET00460662?type=coming-soon") # change to which movie url needed.
    time.sleep(2)  

def click_im_interested():
    """Click the 'I'm interested' button."""
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),\"I'm interested\")]"))
    )
    button.click()
    time.sleep(1)

def click_continue_with_email():
    """Click 'Continue with Email' option."""
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Continue with Email')]"))
    )
    button.click()
    time.sleep(1)

def enter_email(email):
    """Enter email in the input and submit."""
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#emailId"))
    )
    email_input.send_keys(email)
    time.sleep(1)
    email_input.send_keys(Keys.ENTER)

def confirm_interest():
    """Wait for OTP entry and click 'I'm interested' again."""
    button = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),\"I'm interested\")]"))
    )
    button.click()
    time.sleep(1)

def sign_out():
    """Sign out of the account."""
    driver.find_element(By.XPATH, "//span[contains(text(),'Hi, Guest')]").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//div[contains(text(),'Sign out')]").click()
    time.sleep(1)

for email in email_list:
    try:
        visit_bookmyshow()
        click_im_interested()
        click_continue_with_email()
        enter_email(email)
        confirm_interest()
        sign_out()

        time.sleep(random.uniform(2, 5))

    except Exception as e:
        print(f"Error with {email}: {e}")
        continue

driver.quit()
