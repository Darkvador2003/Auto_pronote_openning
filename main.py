from selenium import webdriver
import time
import os, hashlib, getpass
passphrase = getpass.getpass("Passphrase:  ")
salt = b"{salt}" #Put the salt given by create_sha256_hashed_password.py
key = b"{key}" #Put the key given by create_sha256_hashed_password.py
username = 'darth.vader' #Put your username it's usually: prenom.nom
personal_datas = [salt, key, username]
hash_passphrase = hashlib.pbkdf2_hmac('sha256', passphrase.encode('utf-8'), salt, 100000)
if hash_passphrase == key:
    print('Correct password')
    driver = webdriver.Chrome()
    driver.get('https://ent.iledefrance.fr/auth/login')
    time.sleep(5) #Waiting the time for the page to be loaded
    login_area = driver.find_element('id', 'email')
    login_area.send_keys(username)
    password_area = driver.find_element_by_id('password')
    password_area.send_keys(passphrase)
    bouton = driver.find_element_by_class_name('flex-magnet-bottom-right')
    bouton.click()
    time.sleep(10) #Waiting the time for the page tp be loaded
    driver.find_element_by_class_name('pronote').click()
    time.sleep(5) #Waiting the time for the page to be loaded
    driver.switch_to.window(driver.window_handles[-1])
else:
    print("Incorect password")
