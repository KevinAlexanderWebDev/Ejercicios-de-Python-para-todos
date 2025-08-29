from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import datetime

brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
driver_path = (
    "C:/Users/alexa/DRIVERS/chromedriver-win64/chromedriver.exe"  
)

options = webdriver.ChromeOptions()
options.binary_location = brave_path
options.add_argument(
    "--user-data-dir=C:/Users/alexa/AppData/Local/BraveUserData"
)  

service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://web.whatsapp.com")
print("Escanea el código QR si es la primera vez...")

WebDriverWait(driver, 60).until(
    EC.presence_of_element_located(
        (By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
    )
)

# 🕒 Este bloque es para esperar la hora deseada, formato (12, 00)
hora_objetivo = datetime.datetime.combine(
    datetime.date.today(), datetime.time(11, 59)
)
while datetime.datetime.now() < hora_objetivo:
    time.sleep(10)

search_box = driver.find_element(
    By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]'
)
search_box.click()
search_box.send_keys("I A Eligio")
time.sleep(6)

contact = driver.find_element(By.XPATH, '//span[@title="I A Eligio"]')
contact.click()
time.sleep(15)

hora_actual= datetime.datetime.now()
mensaje = f"Frase programada de las {hora_actual}: Recuerda mantenerte hidratada y hacer tus deberes. Te amo"
message_box = driver.find_element(
    By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]'
)
message_box.click()
message_box.send_keys(mensaje)
message_box.send_keys(Keys.ENTER)

print(
    "✅ Mensaje enviado correctamente a las", datetime.datetime.now().strftime("%H:%M")
)
