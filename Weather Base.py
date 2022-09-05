import requests
import bs4
import csv
import pywhatkit
from ipywidgets import interact,interactive,fixed
import ipywidgets as widgets

class Weather():
    def __init__(self,name,number,city):
        self.name=name
        self.num='+91'+number
        self.city=city
    
    def change_city(self,city):
        self.city=city
        
    def fetch_weather(self):
        res = requests.get('https://www.timeanddate.com/weather/india/{}'.format(self.city)) 
        self.soup = bs4.BeautifulSoup(res.text,'lxml')
    
    def generate_info(self):
        temp = self.soup.select('.h2')[0]
        temp = str(temp)
        degree = '°C'
        temp = temp[16:18]+temp[19:21]
        
        sky = str(self.soup.select('p')[0])[3:-4]

        extras = self.soup.select('p')[1].text
        feels_like = extras[12:14]+degree
        high_low = extras[27:34]
        
        #print(temp+' '+high_low+' '+feels_like+' '+sky)
        print('Weather Updated')
        
        self.temp=temp
        self.sky=sky
        self.high_low=high_low
        self.feels_like=feels_like

#Default Inputs
a = Weather('Yashvar','9752413118','jabalpur')
a.fetch_weather()
a.generate_info()

#GUI


#Whatsapp Text
#input
a.name=input("Enter Your Name: ")
a.city=input("Enter City: ")
x,y=map(int,input("Enter Time in Hr(space)Min  [24 hrs format]: ").split())

a.fetch_weather()
a.generate_info()
pywhatkit.sendwhatmsg("{}".format(a.num), '''Hi There! Here Is Your Current Weather Info.

  Weather: {}
  Temprature: {}
  High / Low: {}
  Feels Like: {}
  
Have A Dreat Day'''.format(a.sky,a.temp,a.high_low,a.feels_like), x, y, 30, True, 10)
