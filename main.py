#PS5s bot for the Best Buy website
#Tracks PS5 Inventory and automatically purchases it when available


import ctypes
import requests
import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#PS5 Inventory Availability URL
URL = 'https://www.bestbuy.ca/ecomm-api/availability/products?accept=application%2Fvnd.bestbuy.standardproduct.v1%2Bjson&accept-language=en-CA&skus=15689336'

#HTTP Request Header
headers = {
    'authority': 'www.bestbuy.ca',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0',
    'accept': '*/*',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.bestbuy.ca/en-ca/product/playstation-5-console/15689336',
    'accept-language': 'en-US,en;q=0.9'
}

#Check inventory stock
def checkInventory():

    #Stores current inventory
    inventory = 0

    #Track number of attempts
    attempts = 0

    #Check inventory
    #Loop ends when stock is found
    while(1):

        # Send HTTP request
        response = requests.get(URL, headers=headers)

        # Format HTTP response
        response_formatted = json.loads(response.content.decode('utf-8-sig').encode('utf-8'))

        # Get current inventory count
        inventory = response_formatted['availabilities'][0]['shipping']['quantityRemaining']

        #Found stock, so end the loop
        if(inventory > 0):
            break
        #Still out of stock
        else:
            print("Out of stock" + " Attempt number = " + str(attempts))
            attempts += 1

            #Wait x seconds before re-attempting another request
            time.sleep(60)


#Purchase PS5 automatically
def purchase():
    options = Options()

    #Disable webdriver flag (disable bot prevention features from website)
    options.add_argument('--disable-blink-features=AutomationControlled')

    #Chrome Driver path
    PATH ="CHROMEDRIVER.EXE PATH"

    #Open Google Chrome browser
    driver = webdriver.Chrome(PATH, options=options)

    #Open bestbuy.ca website
    driver.get("https://www.bestbuy.ca/en-ca")

    #Look for search bar
    searchBar = driver.find_element(by=By.NAME, value="search")

    #Enter Nintendo Switch in search bar
    searchBar.send_keys("PS5")

    time.sleep(0.5)

    #Perform search with Keys.ENTER
    searchBar.send_keys(Keys.ENTER)

    #Delay for load
    time.sleep(10)

    #Scroll page down
    driver.execute_script("window.scrollBy(176,2800)", "")

    #Delay for loading
    time.sleep(3)

    #Look for PS5 link
    ps5Link = driver.find_element(By.XPATH, "//*[contains(text(), 'PlayStation 5 Console')]")

    #Open PS5 page
    ps5Link.click()

    time.sleep(5)

    #Look for Add to Cart button
    addToCartButton = driver.find_element(By.CLASS_NAME, "addToCartLabel_YZaVX")

    #Click Add to Cart
    addToCartButton.click()

    #Delay for loading
    time.sleep(5)

    #Look for Go to Cart button
    goToCartButton = driver.find_element(By.XPATH, "//*[contains(text(), 'Go to Cart')]")

    #Click Go to Cart
    goToCartButton.click()

    #Delay for loading
    time.sleep(5)

    #Look for Continue to Checkout Button
    continueToCheckoutButton = driver.find_element(By.XPATH, "//*[contains(text(), 'Continue to Checkout')]")

    #Click Continue to Checkout Button
    continueToCheckoutButton.click()

    #Delay for loading
    time.sleep(5)

    #Look for Continue (Guest checkout)
    continueAsGuest = driver.find_element(By.XPATH, "//*[contains(text(), 'Continue')]")

    #Click Continue
    continueAsGuest.click()

    #Delay for loading
    time.sleep(5)

    #Enter email address
    emailAddress = driver.find_element(By.NAME, "email")
    emailAddress.send_keys("EMAIL_ADDRESS")
    time.sleep(0.5)

    #Enter first name
    firstName = driver.find_element(By.NAME, "firstName")
    firstName.send_keys("FIRST_NAME")
    time.sleep(0.5)


    #Enter last name
    lastName = driver.find_element(By.NAME, "lastName")
    lastName.send_keys("LAST_NAME")
    time.sleep(0.5)

    #Enter phone number
    phoneNumber = driver.find_element(By.NAME, "phoneNumber")
    phoneNumber.send_keys("PHONE_NUMBER")
    time.sleep(0.5)

    #Enter address
    address = driver.find_element(By.NAME, "addressLine1")
    address.send_keys("ADDRESS")
    time.sleep(0.5)

    #Enter city
    city = driver.find_element(By.NAME, "city")
    city.send_keys("CITY")
    time.sleep(0.5)

    #Enter province
    province = driver.find_element(By.NAME, "regionCode")
    province.send_keys("PROVINCE")
    time.sleep(0.5)

    #Enter postal code
    postalCode = driver.find_element(By.NAME, "postalCode")
    postalCode.send_keys("POSTAL_CODE")
    time.sleep(2)

    #Press continue
    continueButton = driver.find_element(By.XPATH, "//*[contains(text(), 'Continue')]")
    continueButton.click()
    time.sleep(5)


    #Enter credit card number
    cardNumber = driver.find_element(By.NAME, "shownCardNumber")
    cardNumber.send_keys("CREDIT_CARD_NUMBER")

    #Enter credit card expiration month
    expirationMonth = driver.find_element(By.NAME, "expirationMonth")
    expirationMonth.send_keys("EXPIRATION_MONTH")

    #Enter credit card expiration year
    expirationYear = driver.find_element(By.NAME, "expirationYear")
    expirationYear.send_keys("EXPIRATION_YEAR")

    #Enter credit card cvv
    cvv = driver.find_element(By.NAME, "cvv")
    cvv.send_keys("CVV")

    #Press continue
    continueButton = driver.find_element(By.XPATH, "//*[contains(text(), 'Continue')]")
    continueButton.click()
    time.sleep(5)

    #Press place order
    placeOrderButton = driver.find_element(By.XPATH, "//*[contains(text(), 'Place Order')]")
    placeOrderButton.click();
    time.sleep(10)


def main():
    #Check for inventory
    checkInventory()

    #Purchase PS5
    purchase()

    # Create windows pop-out message box to notify user when purchase is complete
    ctypes.windll.user32.MessageBoxW(0, "PS5 Successfully Purchased!", 1)


main()