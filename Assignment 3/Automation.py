from selenium import webdriver  #Importing Libraries
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()  # Maximize Screen


# HOME PAGE

baseurl = "http://13.64.144.136/qa/onboarding"  # Website Url
driver.get(baseurl)
time.sleep(2)  # 2 sec pause
driver.find_element("xpath", "//button[@type='submit']").click()  # By Relative Xpath (Get started button)


# CUSTOMER PROFILE

driver.find_element("name", "name").send_keys("Python1")  # NAME
driver.find_element("name", "phone").send_keys("9876543210")  # CONTACT NUMBER
driver.find_element("name", "email").send_keys("pythontest@yopmail.com")  # EMAIL
driver.find_element("name", "company").send_keys("company1")  # COMPANY NAME
select1 = Select(driver.find_element("xpath", "//select[@name='industry']"))  # INDUSTRY DROPDOWN
element1 = select1.options
for val in element1:  # FOR LOOP
    if val.text == "Technology":
        val.click()
        break
else:
    print("Value not matched")

driver.find_element("name", "total_entities").send_keys("0")  # NUMBER OF ENTITIES

clickable = driver.find_element("xpath", "/html/body/div[2]/div/form/div[2]/div/div[8]/div/div[2]/span")  # TOOLTIP INFO
ActionChains(driver) \
    .click(clickable) \
    .perform()
time.sleep(2)
ActionChains(driver).move_to_element_with_offset(clickable, -100, -100).perform()
select1 = Select(driver.find_element("xpath", "//select[@name='purpose']"))  # INTENTION DROPDOWN
val = select1.options
x = len(val)
i = 3
if i <= 3:
    while i <= x:  # WHILE LOOP
        if i == 1:
            m = driver.find_element("xpath", "//*[contains(text(),'Entity Formations')]");
            m.click()
            break
        elif i == 2:
            m = driver.find_element("xpath", "//*[contains(text(),'Entity Compliance & Maintenance')]");
            m.click()
            break
        else:
            m = driver.find_element("xpath", "//*[contains(text(),'Entity Organization & Collaboration')]");
            m.click()
            break
else:
    print("No value found")
driver.find_element("name", "password").send_keys("123456")  # PASSWORD
driver.find_element("name", "password_confirm").send_keys("123456")  # CONFIRM PASSWORD
time.sleep(3)  # 3 sec pause
driver.find_element("xpath", "//button[@type='submit']").click()  # SUBMIT BUTTON (Next button)
time.sleep(5)  # 5 sec pause


# FORMATION FILING

driver.find_element("xpath", "/html/body/div[2]/div/div[2]/a[2]").click()  # SKIP
time.sleep(2)  # 2 sec pause

# PLAN DETAILS

driver.find_element("name", "training_fee").send_keys("2")  # ADDITIONAL HOURS
time.sleep(5)  # 5 sec pause
driver.find_element("xpath", "//button[@type='submit']").click()  # NEXT BUTTON
# time.sleep(5)  # 5 sec pause


# BILLING INFORMATION

# CARD DETAILS
driver.find_element("name", "card[name]").send_keys("test card")  # NAME ON CARD
driver.find_element("name", "card[cardNumber]").send_keys("4242 4242 4242 4242")  # CARD NUMBER
driver.find_element("name", "card[cardExpiry]").send_keys("12/24")  # EXPIRATION DATE
driver.find_element("name", "card[cardCvv]").send_keys("123")  # CVV

# BILLING ADDRESS
driver.find_element("name", "address").send_keys("Hope street")  # BILLING ADDRESS
driver.find_element("name", "city").send_keys("Test City")  # CITY
select1 = Select(driver.find_element("name", "state_id"))  # STATE DROPDOWN
element1 = select1.options
for val in element1:  # FOR LOOP
    if val.text == "Florida":
        val.click()
        break
else:
    print("Value not matched")
driver.find_element("name", "zip").send_keys("54354")  # ZIP CODE
driver.find_element("id", "next-confirm-col").click()  # CONFIRM PURCHASE BUTTON
time.sleep(14)  # 14 sec pause

print("Test Completed")  # CONSOLE OUTPUT

driver.close()
driver.quit()
