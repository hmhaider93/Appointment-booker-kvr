# I am really proud to say that I have got an appointment using this 😎
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from playsound import playsound
chrome_driver_path = '/Users/haidermushtaq/Documents/GitHub/Appointment-booker-kvr/chromedriver'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# driver.get("https://stadt.muenchen.de/terminvereinbarung_/terminvereinbarung_fs.html")
driver.get("https://terminvereinbarung.muenchen.de/fs/termin/?")
driver.implicitly_wait(10)
transfer_forigen_licence = driver.find_element(By.XPATH,'//*[@id="F00e214c9f52bf4cddab8ebc9bbb11b2b"]/fieldset/a[2]/h3')
# transfer_forigen_licence = driver.find_element(By.ID,'appointment')
# print(transfer_forigen_licence)
print("going to click")
transfer_forigen_licence.click()
# all_select = driver.find_element_by_css_selector('#Umschreibung_SPACE_eines_SPACE_ausländischen_SPACE_Führerscheins select')

select = Select( driver.find_element_by_css_selector('#Umschreibung_SPACE_eines_SPACE_ausländischen_SPACE_Führerscheins select'))
select.select_by_visible_text('1')

# Select button
submit_button = driver.find_element_by_class_name('WEB_APPOINT_FORWARDBUTTON')
submit_button.click()


    # print(h3.get_attribute('id'))
count = 0
while(1):
    
    #Select all dates and go through them to check 
  
    found_something = 0
    all_dates = driver.find_elements_by_css_selector('td.nat_calendar')
    for date_elem in all_dates :
        date_elem_content = date_elem.get_attribute('innerHTML')
        print(date_elem_content)
        if('Keine freien Termine am' in date_elem_content):
            print("Unavailible")
            # found_something = 1
            # break 
        elif(not date_elem_content):
            print("Empty String")
        else:
            print("SOMETHING ELSE IS HERE")
            found_something = 1
            date_elem.click()
            break
    if(found_something):
        
        #Select Possible times (prefferably the last)
        # try:
        #     all_times = driver.find_elements_by_css_selector('.WEB_APPOINT_TIMELIST_RADIOTABLE td')
        #     for time_elem in reversed(all_times):
        #         time_elem_content = time_elem.get_attribute('innerHTML')
        #         time_elem.click()
        #         break
        # except:
        #     print("An Error Occured finding time")
            
        #Select Possible times (prefferably the last)
        try:
            all_times = driver.find_elements_by_css_selector('.WEB_APPOINT_TIMELIST_BUTTON')
            for time_elem in reversed(all_times):
                time_elem_content = time_elem.get_attribute('innerHTML')
                print(time_elem_content)
                time_elem.click()
                break
        except:
            print("An Error Occured finding time Button")    
            
        playsound('song.mp3')
        print('playing sound using  playsound')
        break
    else:
        driver.refresh()
        count += 1
        print("Loop Number: " + str(count))
        current_time = datetime.now().strftime("%H:%M:%S")
        print("Current Time =", current_time)
        time.sleep(30)
        continue
    
print("CODE FINISHED")
# print(transfer_forigen_licence.get_attribute('innerHTML'))
# time.sleep(10)
# transfer_forigen_licence2 = driver.find_element(By.ID,'appointment')
# print(transfer_forigen_licence2.get_attribute('innerHTML'))

    
# driver.close()

# <a class="nat_calendar nat_calendar_weekday_bookable" href="javascript:locationList.showTimeList('a6a84abc3c8666ca80a3655eef15bade','a6a84abc3c8666ca80a3655eef15badeTL','2022-04-28')"><span class="hidden">Termin am </span>28<span class="hidden">.4.2022 reservieren</span></a>