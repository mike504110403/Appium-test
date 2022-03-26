from appium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction

''' ad '''
account = "sgtest019"
password = "a156156"
''' ad '''



''' connect device '''
desired_cap = {
  "appium:deviceName": "emulator-5554",
  "appium:platformName": "Android",
  "appium:platformVersion": "11",
  "appium:appPackage": "com.more.laozi",
  "appium:appActivity": "sgt.o8app.ui.LaunchActivity"
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
driver.implicitly_wait(20)

# close announcement
# driver.find_element_by_id('com.more.laozi:id/new_proclamation_btn_close').click()
''' connect device '''




''' Log in '''
MemberLogin = driver.find_element_by_id('com.more.laozi:id/preload_btn_account')
MemberLogin.click()
driver.implicitly_wait(10)
KeyAccount = driver.find_element_by_id('com.more.laozi:id/newLogin_edit_account')

driver.implicitly_wait(10)
KeyAccount.send_keys(account)
KeyPassword = driver.find_element_by_id('com.more.laozi:id/newLogin_edit_password')

driver.implicitly_wait(5)
KeyPassword.send_keys(password)
Login = driver.find_element_by_id('com.more.laozi:id/newLogin_btn_submit')
Login.click()
driver.implicitly_wait(30)
''' Log in '''




''' Open & Close game '''
### 切至轉輪館 ###
# click filter
filter_e = driver.find_element_by_id('com.more.laozi:id/btnFilter')
driver.implicitly_wait(5)
filter_e.click()
# click slot
driver.implicitly_wait(5)
slot_e = driver.find_element_by_id('com.more.laozi:id/tvFilter2')
driver.implicitly_wait(5)
slot_e.click()
driver.implicitly_wait(5)

### click game 1 ###
# click game
Game = driver.find_element_by_id('com.more.laozi:id/gameMenuItem_rl_layout')
# print(Game)
driver.implicitly_wait(50)
Game.click()
print('game clicked')
driver.implicitly_wait(50)
# click play now
playnow = driver.find_element_by_id('com.more.laozi:id/gameMenuItem_btn_play')
playnow.click()

### time condition ###
# wait_element = WebDriverWait(driver, 500).until(EC.visibility_of_element_located('com.more.laozi:id/game_activity_ll_layout_01'))
print('wait for loading')
time.sleep(50)

### quit game ###
# click setting
TouchAction(driver).tap(x=648, y=92).perform()
driver.implicitly_wait(15)
# click quit game
TouchAction(driver).tap(x=412, y=913).perform()
driver.implicitly_wait(15)
# click no retain
TouchAction(driver).tap(x=196, y=734).perform()
driver.implicitly_wait(15)
# click rrevious page
TouchAction(driver).tap(x=78, y=48).perform()
''' Open & Close game '''




# quit driver
driver.quit()





#                                    /hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.ImageView[2]
# driver.press_keycode(84)
# driver.set_value()
# android:id/content