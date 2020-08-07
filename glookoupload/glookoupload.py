from selenium import webdriver
import time, pyautogui

#enter username and password below
username = ''
password = ''


browser = webdriver.Chrome()
browser.get('http://my.glooko.com/users/sign_in')
browser.maximize_window()


email_elem = browser.find_element_by_id('user_email')
email_elem.send_keys(username)
pass_elem = browser.find_element_by_id('user_password')
pass_elem.send_keys(password)


sign_in_elem = browser.find_element_by_id('sign-in-button')
sign_in_elem.click()

time.sleep(5)
upload_elem = browser.find_element_by_class_name('OmnipodUpload_btnOmnipodUploader')
upload_elem.click()

upload_butt_elem = browser.find_element_by_class_name('OmnipodUploadContainer_omnipodBlueButton')
upload_butt_elem.click()

time.sleep(1)
pyautogui.click(153, 195)
pyautogui.scroll(-2000)
pyautogui.click(96, 409)
pyautogui.click(497, 140)
pyautogui.click(787, 537)

time.sleep(15)
done_button = browser.find_element_by_class_name('OmnipodUploadContainer_omnipodGreyButton')
done_button.click()

browser.quit()
