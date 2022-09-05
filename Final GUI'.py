import tkinter
import customtkinter
from datetime import datetime

import requests
import bs4
import csv
import pywhatkit
from ipywidgets import interact,interactive,fixed
import ipywidgets as widgets



#################Weather report base program###############
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
a = Weather('Xavier','XXXXXXXXXX','jabalpur')
a.fetch_weather()
a.generate_info()
###########################################################


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

app=customtkinter.CTk()
app.geometry("500x300")
app.title("Weather Report Scrapper")



def button_callback():
    #update name
    name=entry_1.get()
    a.name=name
    
    #update mobile number
    num=entry_2.get()
    a.num='+91'+num
    
    #update location
    loc=entry_3.get()
    a.city=loc

    #WeatherGenerating
    a.fetch_weather()
    a.generate_info()


    #update Time
    now=datetime.now()
    x=now.strftime("%H:%M")
    hrs = int(x[:2])
    mins = int(x[3:])

    if mins>55:
        hrs=hrs+1
        mins=60-mins+1
    else:
        mins=mins+3
    
    print(hrs,mins)
    pass

    #Whatsapp Part {Sending Msg}
    pywhatkit.sendwhatmsg("{}".format(a.num), '''Hi There! Here Is Your Current Weather Info.

      Weather: {}
      Temprature: {}
      High / Low: {}
      Feels Like: {}
  
    Have A Dreat Day'''.format(a.sky,a.temp,a.high_low,a.feels_like), hrs, mins, 30, True, 10)

frame_1 =customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20,padx=60,fill="both", expand=True)

label_1 = customtkinter.CTkLabel(master=frame_1, text="Weather Report (Fill in the Details)")#justify=tkinter.LEFT)
label_1.pack(pady=12, padx=10)

entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="Name")
entry_1.pack(pady=12, padx=10)

entry_2 = customtkinter.CTkEntry(master=frame_1, placeholder_text="Whatsapp No.")
entry_2.pack(pady=12, padx=10)

entry_3 = customtkinter.CTkEntry(master=frame_1, placeholder_text="City")
entry_3.pack(pady=12, padx=10)


button_1 = customtkinter.CTkButton(master=frame_1, text="Get Weather",command=button_callback)
button_1.pack(pady=12, padx=10)

app.mainloop()
