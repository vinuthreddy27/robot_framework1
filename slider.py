from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

driver=WebDriver()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://testautomationpractice.blogspot.com/")

radio_btns=driver.find_elements("xpath","//input[@type='radio']")
for btn in radio_btns:
    radio=btn.get_attribute("value")
    if radio=="female":
        btn.click()

sleep(3)

view=driver.find_element("xpath","//h2[.='Slider']")
slider=driver.find_element("xpath","(//span[@class='ui-slider-handle ui-corner-all ui-state-default'])[1]")
slider2=driver.find_element("xpath","(//span[@class='ui-slider-handle ui-corner-all ui-state-default'])[2]")

actions=ActionChains(driver)

hover=driver.find_element("class name","date-picker-box")
actions.move_to_element(hover).perform()
actions.context_click(hover).perform()
sleep(3)

actions.scroll_to_element(view).perform()
sleep(3)

source=driver.find_element("id","draggable")
target=driver.find_element("id","droppable")

actions.drag_and_drop(source,target).perform()
sleep(2)
actions.click_and_hold(target).pause(3).move_to_element(source).release().perform()

actions.drag_and_drop_by_offset(slider,75,0).perform()
actions.drag_and_drop_by_offset(slider2,50,0).perform()


for btn in radio_btns:
    radio=btn.get_attribute("value")
    if radio=="male":
        btn.click()
sleep(3)

driver.get("https://practice-automation.com/javascript-delays/")
driver.find_element("id","start").click()

wait=WebDriverWait(driver,10)
element=wait.until(visibility_of_element_located(("id","delay")))
element.clear()

driver.get("https://practice-automation.com/slider/")

slider3=driver.find_element("id","slideMe")

actions=ActionChains(driver)
actions.drag_and_drop_by_offset(slider3,250,0).perform()
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
sleep(3)
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

sleep(3)

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