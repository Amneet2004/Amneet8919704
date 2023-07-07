# Importing required libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Maximize the window
driver.maximize_window()

# Navigating to the Amazon.ca homepage
driver.get("https://www.amazon.ca")
# time.sleep(3)

# Finding the "Accounts & Lists" link and clicking it
accounts_link = driver.find_element("xpath","/html/body/div[1]/header/div/div[3]/div[13]/div[2]/a/span")
accounts_link.click()

# Find the email input field and enter your email
email_input = driver.find_element("id","ap_email")
email_input.send_keys("amneet9704@conestogac.on.ca")

# Find the continue button and click it
continue_button = driver.find_element("id","continue")
continue_button.click()

# Find the password input field and enter your password
password_input = driver.find_element("id","ap_password")
password_input.send_keys("Sabharwal20$")

# Find the sign-in button and click it
sign_in_button = driver.find_element("id","signInSubmit")
sign_in_button.click()

# Finding the search bar and entering text
search_bar = driver.find_element("id","twotabsearchtextbox")
search_bar.send_keys("Laptop")

# Submitting the search query
search_bar.send_keys(Keys.RETURN)

# Waiting for the search results page to load
time.sleep(5)

# Verifying that the search results page has loaded
assert "Laptop" in driver.title

# Selecting a laptop from the search results
laptop_link = driver.find_element("xpath","/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/div/div/div[1]/span/a/div/img")
# laptop_link = driver.find_element("By.CSS_SELECTOR","span[data-component-type='s-product-image'] a")
laptop_link.click()



# Waiting for the laptop details page to load
time.sleep(5)

# Adding the laptop to the cart
add_to_cart_button = driver.find_element("id","add-to-cart-button")
add_to_cart_button.click()

# Waiting for the cart to update
time.sleep(5)

# Clicking on no thanks button
no_thanks_button= driver.find_element("xpath","/html/body/div[8]/div[3]/div[1]/div/div/div[2]/div[2]/div/div/div[3]/div/span[2]")
no_thanks_button.click()
time.sleep(2)

# Verifying that the laptop has been added to the cart
cart_count = driver.find_element("id","attach-sidesheet-view-cart-button")
cart_count.click()
time.sleep(2)

# Proceeding to Checkout
proceed_to_checkout= driver.find_element("xpath","/html/body/div[1]/div[2]/div[3]/div[5]/div/div[1]/div[1]/div/form/div/div/span/span/span/input")
proceed_to_checkout.click()

# Closing the webdriver
driver.close()
