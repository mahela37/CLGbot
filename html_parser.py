from bs4 import BeautifulSoup

f = open("html_source.txt", "r")
f_contents=f.read()
f.close()


soup=BeautifulSoup(f_contents,'html.parser')

mydivs=soup.findAll("div", {"class": "label"})
print(mydivs)
