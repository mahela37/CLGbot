def parseMainPage():
    from bs4 import BeautifulSoup
    import re
    import requests

    r=requests.get("https://www.clg.org/Class-Action/List-of-Class-Actions")
    soup=BeautifulSoup(r.text,'html.parser')
    mydivs=soup.find("div",{"class":'classactions'})

    div_array=[]
    category=""
    for div in mydivs:
        try:
            class_type=div.attrs['class'][0]+div.attrs['class'][1]  #it's a lawsuit entry
            if(class_type=="actionwith_image"):
                #the regex is for french characters that the website has used for a few entries. We wanna strip ito out.
                #for each lawsuit, make a dict entry with the name, href and the category
                temp_entry={'name':re.sub(r'[^a-zA-Z]', "", div.contents[5].contents[0].contents[0].strip()),'href':div.contents[5].contents[0].attrs['href'],'category':category}
                div_array.append(temp_entry)

        except:
            try:
                if('cat' in class_type):    #it's a new category
                    category=class_type
            except:
                """"""

    return div_array
