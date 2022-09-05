# Weather-Report-Scrapper

Description-
This project is based on Web scrapping. It gets the weather from web (Just a random Webpage), and sends it to the whatsapp number you will enter under 3 mins

Libraries req-
1. tkinter
2. customtkinter
3. datetime
4. requests
5. bs4
6. csv
7. pywhatkit
8. ipywidgets 

Before Running-
Make sure you have whatsapp web open in ur default browser, The whatsapp number will be the number you want to send the weather report from.

Instructions:-

1. The main file is named Weather.py

2. Run the main file

3. Fill in the information:

    -Name of the Receiver
  
    -Whatsapp Number of the receier
  
    -Name of the city for the weather report
  
4. Press "Get Weather" (Only press the button once to avoid error)

Waiting part:

The terminal will show how long it will take to send the message, it will open whatsapp web on your default browser and starts a chat with the receiver.
The program is made to wait 30 sec before it sends the message , in case of slow internet connection it wont generate an error.
Wait for the message to be sent and and the browser will automatically close after 5 secs

(You can change the values of wait time accordingly in Weather.py file)
