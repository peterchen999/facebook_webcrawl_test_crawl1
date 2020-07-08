import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from bs4 import BeautifulSoup

profile = webdriver.FirefoxProfile() # add firefox settings
profile.set_preference("dom.webnotifications.enabled", False) # close firefox notifications
profile.update_preferences() # update firefox preferences if needed
driver = webdriver.Firefox(firefox_profile=profile)
driver.get('https://www.facebook.com')
sleep(3)

email_input = driver.find_element_by_id('email')
sleep(3)
email_input.send_keys('peter.chen999@gmail.com')
pwd_input = driver.find_element_by_id('pass')
sleep(3)
pwd_input.send_keys('ru04ej/ 10223')
pwd_input.send_keys(Keys.RETURN)
sleep(5)

#user_navigation_label = driver.find_element_by_id('userNavigationLabel')
#user_navigation_label.click()
#settings = driver.find_elements_by_link_text('設定')

user_facebook_id = input('your id? ')
activity_log_url = 'https://www.facebook.com/profile.php?id='+user_facebook_id+'&sk=allactivity&privacy_source=your_facebook_information&entry_point=settings_yfi'
driver.get(activity_log_url)
#using direct url to move to user's activity log page
sleep(5)

for i in range(12): # 捲動12次
    driver.execute_script("window.scrollTo(0, {})".format(4000 * (i + 1))) #每次捲動4000的單位
    sleep(3) # 等待2秒鐘讓頁面讀取

htmltext = driver.page_source
#download the whole html source

print(htmltext)

fout = open('original_html.txt', 'w')
fout.write(htmltext)
fout.close()
#write to file as original_html.txt