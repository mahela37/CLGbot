import time
from selenium import webdriver



#
# driver = webdriver.Chrome('chromedriver.exe')  # Optional argument, if not specified will search path.
# driver.get('https://www.clg.org/Class-Action/List-of-Class-Actions');
# time.sleep(5) # Let the user actually see something!
# html_source=driver.page_source
#
#
# f= open("html_source.txt","w")
# f.write(html_source)
# f.close()
#
#
# driver.quit()


import html_parser


f= open("entries_completed.txt","r")
completedList=f.readlines()
f.close()

lawsuitList=html_parser.parseMainPage()
newLawsuitsList=[]
for lawsuit in lawsuitList:
    alreadyDone=0
    lawsuitName=lawsuit['name']
    for completedEntry in completedList:
        completedEntry=completedEntry.strip()
        completedEntry=completedEntry.split(";")
        if(lawsuitName==completedEntry[0]):
            alreadyDone=1
            break
    if(alreadyDone==0):
        newLawsuitsList.append(lawsuit)


for lawsuit in newLawsuitsList:
    print(lawsuit)