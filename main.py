import time
from selenium import webdriver




driver = webdriver.Chrome('chromedriver.exe')  # Optional argument, if not specified will search path.
driver.get('https://www.clg.org/Class-Action/List-of-Class-Actions');
time.sleep(5) # Let the user actually see something!
html_source=driver.page_source


f= open("html_source.txt","w")
f.write(html_source)
f.close()


"""
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5) # Let the user actually see something!
"""
driver.quit()