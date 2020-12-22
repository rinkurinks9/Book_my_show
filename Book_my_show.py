from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
path = "C:\\Program Files (x86)\\chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get("https://in.bookmyshow.com/")
driver.maximize_window()
action = ActionChains(driver)
time.sleep(5)
personalised_updates_off = driver.find_element_by_xpath('//*[@id="wzrk-cancel"]')
personalised_updates_off.click()
time.sleep(3)

#search_city = driver.find_element_by_xpath('//*[@id="modal-root"]/div/div/div/div[1]/div/div/input')
#search_city.send_keys('Kurnool')
Hyderabad = driver.find_element_by_xpath('//*[@id="modal-root"]/div/div/div/div[2]/ul/li[4]/div/div')
Hyderabad.click()
time.sleep(4)

#link = driver.find_element_by_link_text("Kanulu Kanulanu Dhochaayante")
#link.click()

kkda = driver.find_elements_by_tag_name("a")
ls = []
for lnk in kkda:
    ls.append((lnk.get_attribute('href')))
#print(ls)
kkda1 = 'https://in.bookmyshow.com/hyderabad/movies/kanulu-kanulanu-dhochaayante/ET00127469'
if kkda1 in ls:
    driver.get(kkda1)
    time.sleep(5)
book_tickets = driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/div[2]/div/button')
book_tickets.click()
time.sleep(2)

show = driver.find_element_by_xpath("/html/body/section[1]/div[2]/div/ul/li[1]/div[2]/div[2]/div/a")
show.click()

accept = driver.find_element_by_link_text("Accept")
accept.click()
time.sleep(3)

select_seats = driver.find_element_by_class_name("action-btn")
select_seats.click()

seat_7 = driver.find_element_by_id("B_J_20")
seat_7.click()
time.sleep(2)

seat_9 = driver.find_element_by_id("B_J_18")
seat_9.click()
time.sleep(2)

pay = driver.find_element_by_id("btmcntbook")
pay.click()
time.sleep(5)

m_ticket = driver.find_element_by_xpath("/html/body/section[2]/div[3]/section[2]/div[3]/div/div[3]/div[1]")
m_ticket.click()
time.sleep(5)

proceed_pay = driver.find_element_by_xpath("/html/body/section[2]/div[3]/section[2]/div[3]/div/div[4]/a[2]")
proceed_pay.click()
#pvr = driver.find_element_by_xpath("/html/body/section[1]/div[2]/div/ul/li[2]/div[1]/div[2]/div/div[1]/a")
#pvr.click()

