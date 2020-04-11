def completeApplication(url,name,category):
    f = open("user_information.txt", "r")
    userInfo= f.readlines()
    f.close()

    firstName=userInfo[0].split(":")[1].strip()
    lastName = userInfo[1].split(":")[1].strip()
    email = userInfo[2].split(":")[1].strip()
    address = userInfo[3].split(":")[1].strip()
    city = userInfo[4].split(":")[1].strip()
    province = userInfo[5].split(":")[1].strip()
    country = userInfo[6].split(":")[1].strip()
    postalCode = userInfo[7].split(":")[1].strip()
    homePhone = userInfo[8].split(":")[1].strip()


    import time
    from selenium import webdriver
    from selenium.webdriver.support.ui import Select

    driver = webdriver.Chrome('chromedriver.exe')
    driver.get(url)
    time.sleep(2)

    try:
        elem=driver.find_element_by_class_name("closepopup")
        elem.click()
    except:
        """"""

    elem = driver.find_element_by_name("firstname")
    elem.send_keys(firstName)
    elem = driver.find_element_by_name("lastname")
    elem.send_keys(lastName)
    elem = driver.find_element_by_name("email")
    elem.send_keys(email)
    elem = driver.find_element_by_name("emailc")
    elem.send_keys(email)
    elem = driver.find_element_by_name("address")
    elem.send_keys(address)
    elem = driver.find_element_by_name("city")
    elem.send_keys(city)
    elem = Select(driver.find_element_by_name("state"))
    elem.select_by_value(province)
    elem = Select(driver.find_element_by_name("country"))
    elem.select_by_value(country)
    elem = driver.find_element_by_name("zip")
    elem.send_keys(postalCode)
    elem = driver.find_element_by_name("tel_home")
    elem.send_keys(homePhone)

    elem = driver.find_element_by_name("damages")
    elem.send_keys("damage")


    html_source = driver.page_source
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html_source, 'html.parser')
    mydivs = soup.find("img", {"class": 'captcha'})
    captchaImageLink = mydivs.attrs['src']
    captchaImageLink = "https://www.clg.org" + captchaImageLink
    print(captchaImageLink)

    import urllib.request
    urllib.request.urlretrieve(captchaImageLink, "captcha.jpeg")
    time.sleep(5)
    import pytesseract
    from PIL import Image
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    captchaText = pytesseract.image_to_string(Image.open('captcha.jpeg'))

    elem = driver.find_element_by_name("captcha[answer]")
    print(captchaText)
    elem.send_keys(captchaText)

    #hmm its not working exactly for some reason

    time.sleep(5)
    driver.quit()

completeApplication(url='https://www.clg.org/Class-Action/List-of-Class-Actions/Intel-Processor-Security-Flaw-Class-Action',name="Intel",category="Tech")