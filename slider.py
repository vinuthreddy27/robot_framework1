from time import sleep
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common import actions
from selenium.webdriver.support.expected_conditions import visibility_of_element_located, alert_is_present,element_to_be_clickable
from selenium.webdriver.support.wait import WebDriverWait

driver=WebDriver()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://demowebshop.tricentis.com/")
actions1=ActionChains(driver)
radio_btn=driver.find_element("xpath","//input[@value='1']")
radio_btn.click()

print(radio_btn.is_selected())
driver.quit()

driver.find_element("xpath", "//a[.='Log in']").click()
email=driver.find_element("id","Email")
password=driver.find_element("id","Password")
email.send_keys("reddyvinuth")


actions1.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
actions1.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
actions1.send_keys(Keys.TAB).perform()
actions1.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()

actions1.key_down(Keys.PAGE_DOWN).key_up(Keys.PAGE_UP).perform()
actions1.key_down(Keys.PAGE_UP).key_up(Keys.PAGE_DOWN).perform()



driver.get("https://tutorialsninja.com/demo/index.php?route=account/register")

fn=driver.find_element("name","firstname")
actions2=ActionChains(driver)
(actions2.click(fn).send_keys("vinuth").send_keys(Keys.TAB).send_keys("reddy").send_keys(Keys.TAB).send_keys("reddyvinuth27@gmail.com").send_keys(Keys.TAB).send_keys("7676252914").send_keys(Keys.TAB).send_keys("selenium").key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys("c").send_keys(Keys.TAB).key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform())


driver.get("https://demowebshop.tricentis.com/")

driver.find_element("xpath","//a[@href='/login']").click()

driver.find_element("id","Email").send_keys("reddyvinuth27@gmail.com")
element=driver.find_element("id","Password")
element.send_keys("selenium")
element.submit()

element2=driver.find_element("xpath","//span[.='25.00']")
element2.click()

element3=driver.find_element("xpath","//input[@value='Add to cart']")
element3.click()

driver.close()


driver.get("https://www.makemytrip.com/")
driver.find_element("xpath","//span[@class='commonModal__close']").click()

driver.find_element("id","fromCity").click()

option=driver.find_element("xpath","//input[@placeholder='From']")
option.send_keys("bali")

wait=WebDriverWait(driver,12)
element=wait.until(element_to_be_clickable((("xpath","//p[.='Ngurah Rai']"))))
element.click()


driver.get("https://letcode.in/forms")

options=driver.find_elements("xpath","(//div[@class='select'])[2]")
for option in options:
    if option.text=="Maldives":
        option.click()

driver.quit()

driver.get("https://testautomationpractice.blogspot.com/")

radio_btns=driver.find_elements("xpath","//input[@type='radio']")
for btn in radio_btns:
    radio=btn.get_attribute("value")
    if radio=="female":
        btn.click()

view=driver.find_element("xpath","//h2[.='Slider']")
slider=driver.find_element("xpath","(//span[@class='ui-slider-handle ui-corner-all ui-state-default'])[1]")
slider2=driver.find_element("xpath","(//span[@class='ui-slider-handle ui-corner-all ui-state-default'])[2]")

actions=ActionChains(driver)

hover=driver.find_element("class name","date-picker-box")
actions.move_to_element(hover).perform()
actions.context_click(hover).perform()

actions.scroll_to_element(view).perform()


source=driver.find_element("id","draggable")
target=driver.find_element("id","droppable")

actions.drag_and_drop(source,target).perform()

actions.click_and_hold(target).pause(3).move_to_element(source).release().perform()

actions.drag_and_drop_by_offset(slider,75,0).perform()
actions.drag_and_drop_by_offset(slider2,50,0).perform()


for btn in radio_btns:
    radio=btn.get_attribute("value")
    if radio=="male":
        btn.click()

driver.get("https://practice-automation.com/javascript-delays/")
driver.find_element("id","start").click()

wait=WebDriverWait(driver,10)
element=wait.until(visibility_of_element_located(("id","delay")))
element.clear()

driver.get("https://practice-automation.com/slider/")

slider3=driver.find_element("id","slideMe")

actions=ActionChains(driver)
actions.drag_and_drop_by_offset(slider3,250,0).perform()
actions.move_to_element_with_offset(slider3,450,0).perform()

sleep(3)


driver.get("https://practice-automation.com/window-operations/")
print(driver.title)
tab1=driver.find_element("xpath","//b[.='New Tab']")
tab1.click()

parent_handle=driver.current_window_handle
handles=driver.window_handles

for handle in handles:
    driver.switch_to.window(handle)
    if driver.title=="automateNow | The Best FREE Software Online Training Platform":
        print(driver.title)
        element = driver.find_element("xpath", "//img[@data-recalc-dims='1']/../../../..//img[@alt='Selenium tutorials']")
        print(element.is_displayed())
        element.click()
        print(driver.title)

driver.switch_to.window(parent_handle)
print(driver.title)

driver.get("https://automatenow.io/")
element = driver.find_element("xpath", "//img[@data-recalc-dims='1']/../../../..//img[@alt='Selenium tutorials']")
print(element.is_displayed())
element.click()
print(driver.title)


driver.get("https://practice-automation.com/calendars/")

element=driver.find_element("xpath","//input[starts-with(@id,'g1065-s')]")
element.click()

month=driver.find_element("class name","ui-datepicker-month").text
year=driver.find_element("class name","ui-datepicker-year").text


while not(month.__eq__("July") and year.__eq__("2025")):
    net_btn=driver.find_element("xpath","//a[@title='Next']")
    net_btn.click()
    month = driver.find_element("class name", "ui-datepicker-month").text
    year = driver.find_element("class name", "ui-datepicker-year").text

date=driver.find_element("xpath","//a[.='3']")
date.click()



driver.get("https://practice-automation.com/iframes/")

parent_window=driver.current_window_handle

driver.switch_to.frame("iframe-1")

view=driver.find_element("xpath","//a[.='YouTube']")

actions=ActionChains(driver)
actions.scroll_to_element(view).perform()

driver.find_element("xpath","//a[.='YouTube']").click()

handles=driver.window_handles

for handle in handles:
    driver.switch_to.window(handle)
    if driver.title=="Playwright - YouTube":
        print(driver.title)

driver.switch_to.window(parent_window)
print(driver.title)

driver.get("https://omayo.blogspot.com/")

alert=driver.find_element("xpath","//input[@value='ClickToGetAlert']")
alert.click()

wait=WebDriverWait(driver,12)

ok=wait.until(alert_is_present())
ok.accept()

driver.find_element("xpath","//button[@onclick='setTimeout(myFunction,3000)']").click()

element=wait.until(visibility_of_element_located(("xpath","//a[@href='http://flipkart.com/']")))
element.click()

if driver.title=="Online Shopping Site for Mobiles, Electronics, Furniture, Grocery, Lifestyle, Books & More. Best Offers!":
    print("test case passed")
else:
    print("test case failed")

