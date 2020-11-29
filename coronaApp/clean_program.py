import requests
from bs4 import BeautifulSoup
# from tkinter import *
import io
import base64
# from PIL import Image

try:
    # Python2
    from urllib2 import urlopen
except ImportError:
    # Python3
    from urllib.request import urlopen

r=requests.get("https://www.worldometers.info/coronavirus/#countries")
soup=BeautifulSoup(r.content,'html.parser')

x=requests.get("https://www.boldtuesday.com/pages/alphabetical-list-of-all-countries-and-capitals-shown-on-list-of-countries-poster")
soup_again=BeautifulSoup(x.content,'html.parser')

page=requests.get(url="https://www.worldometers.info/geography/flags-of-the-world/")
more_soup=BeautifulSoup(page.content,'html.parser')

t=soup.find('tbody')
tb=soup_again.find('tbody')

#List of Overall countries
cont_name_list=[]
for tr in tb.findAll('tr'):
    for td in tr.findAll('td'):
        cont_name_list.append(td.text.title())
contry_names=set(cont_name_list[2::2])

#Listwise data of every infected country
combined_data=[]
for tr in t.findAll('tr'):
    contry_data=[]
    for td in tr.findAll('td'):
        contry_data.append(td.text)
    combined_data.append(contry_data)

#List of the number of total cases of infections
total_inf=[]
inf_cont_names=set()
for i in range(0,len(combined_data)):
    total_inf.append(int(combined_data[i][2].replace(',','')))
    inf_cont_names.add(combined_data[i][1])


#Getting most infected contries

def inf_contries():
    # print("THE MOST AFFECTED PLACES ARE:")
    inf_cont_list = []
    for i in range(7):
        global f2
        f2=max(total_inf)
        first=total_inf.index(f2)
        global f1
        f1=combined_data[first][1]

        # print(f1,"\t",f2,"infected")
        total_inf.remove(f2)
        total_inf.insert(first,-1)
        inf_cont_list.append([f1,f2])
    return inf_cont_list


#Finding the safest places

def safe_places():
    # print("\nTHE SAFEST PLACES ARE:")

    rem=contry_names-inf_cont_names
    rem=rem-{'United Kingdom*','United States','Central African Republic','United Arab Emirates','South Korea','Bosnia & Herzegovina','Antigua & Barbuda','Bahamas, The','Congo, Democratic Republic Of The','Saint Vincent & The Grenadines','Gambia, The','Guinea-Bissau','South Sudan','Trinidad & Tobago'}
    rem=list(rem)
    rem.sort()

    return rem

    # if rem:
    #     for i in rem:
    #         print(i[1:-2], end=', ')
    #
    #     print("\nNOT A SINGLE PERSON IS RECORDED INFECTED IN THESE COUNTRIES")


##def getting_flag():
##    y=more_soup.findAll('div', attrs={'class': 'content-inner'})[0]
##    y2=y.findAll('div',attrs={'class': 'col-md-4'})
##
##    name_list=[]
##    for j in y2:
##        y4=j.find('div')
##        y5=y4.find('div').text
##        name_list.append(y5)
##
##    flag_list=[]
##    y3=y.findAll('a')[3:-3]
##    for i in y3:
##        flag_list.append("worldometers.info"+i['href'])



# inf_contries()
# safe_places()
##getting_flag()
##
