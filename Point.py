import pyttsx3                                     # pip install pyttsx3
import datetime
import speech_recognition as sr                    # pip install SpeechRecognition
import wikipedia                                   # pip install wikipedia
import webbrowser
import os
import sys
from email.message import EmailMessage
import pywhatkit                                   # pip install pywhatkit
import MyAlarm                  
import pyjokes                                     # pip install pyjokes
from speedtest import Speedtest                    # pip install speedtest-cli
from pywikihow import search_wikihow               # pip install pywikihow
import pyautogui                                   # pip install pyAutoGUI
import random
from forex_python.converter import CurrencyRates   # pip install forex-python
import requests                                    # pip install requests
import time
from quote import quote                            # pip install quote
import winshell as winshell                        # pip install winshell
from geopy.geocoders import Nominatim              # pip install geopy  and pip install geocoder
from geopy import distance
import random
import SnakeGame
import Record
import requests
from PIL import Image
import datetime
import speech_recognition as sr
import wikipedia
import tkinter as tk
import threading
from tkinter import messagebox

from tkinter import *

root = Tk()

root.title("Following commands User Manual")  # Set the window title
root.geometry("1000x1000")  
# Sample array list
array_list = ["Image = getting sample image on internet",
              " ", 
              "Open youtube = opening youtube on net", 
              " ", 
              "Open google = opening google search", 
              " ", 
              "Opening stack overflow", 
              " ", 
              "the time = for saying what time is it",
              " ", 
              "The date = for saying what is the data today",
              " ", 
              "open visual studio code = opening vs code",
              " ", 
              'open notepad = opening notepad',
              " ", 
              'open charm = opening py charm',
              " ", 
              'open mozilla firefox = opening mozilla firefox',
              " ", 
              'open chrome = opening chrome',
              " ", 
              'who are you = for entertainment',
              " ", 
              'what you want to do = = for entertainment',
              " ", 
              'alexa = = for entertainment',
              " ", 
              'google assistant = = for entertainment',
              " ", 
              'siri = = for entertainment',
              " ", 
              'cortana = = for entertainment',
              " ", 
              'python assistant = = for entertainment',
              " ", 
              'what language you use = = for entertainment',
              " ", 
              'play = playing something on youtube',
              " ", 
              'search = searching something on google',
              " ", 
              'set alarm = setting an alarm clock',
              " ", 
              'close command prompt = closing command prompt EXE',
              " ", 
              'close firefox = closing firefox exe' ,
              " ", 
              'close visual studio code = closing vs code exe',
              " ", 
              'close eclipse = closing eclipse ide exe ',
              " ", 
              'close notepad = closing notepad',
              " ", 
              'close charm = closing pycharm',
              " ", 
              'close chrome = closing chrome',
              " ", 
              'close spotify = closing spotify',
              " ", 
              'resume or pause = playing or pause media',
              " ", 
              'previous = playing previous music / media',
              " ", 
              'next = playing next song / media', 
              " ", 
              'weather or temperature either of the 2 commands',
              " ", 
              'month = saying the present month',
              " ", 
              'day = saying the present day',
              " ", 
              'quote = for entertainment and also for motivatiob',
              " ", 
              'empty recycle bin = emptying the recycle bin ',
              " ", 
              'write a note = writing a note which is some of important notes ',
              " ", 
              'show me the notes = showing notes ' ,
              " ", 
              'distance = distancy of between of the 2 location example from QC to manila',
              " ", 
              'screenshot = screenshot of the screen',
              " ", 
              'volume up = voluming up',
              " ", 
              'volume down = voluming down',
              " ", 
              'mute volume = muting volume',
              " ", 
              'shut down = shutting down',
              " ", 
              'restart = restart the pc',
              " ", 
              'logout = logging out the pc',
              " ", 
              'joke = telling you a joke',
              " ", 
              'internet speed = checking your internet speed',
              " ", 
              'screen recording = recording your screen but not totally recording',
              " ", 
              'snake = a snake game that we ve prepared ',
              " ", 
              ]

# Create a Listbox widget
listbox = Listbox(root, height=200, width=200)
listbox.pack()

# Insert each item from the array list into the Listbox
for item in array_list:
    listbox.insert(END, item)


engine = pyttsx3.init()   

root = tk.Tk()
root.geometry('1000x500')
root.minsize(700, 500)
root.wm_title('Desktop Assistant')
root.resizable(False, True)

chat_listbox = tk.Listbox(master=root, height=150, width=50)
scroll_bar = tk.Scrollbar(master=root)
output_text = tk.Text(master=root, height=10, width=50)  # Added Text widget for output

scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
chat_listbox.pack(fill=tk.Y, side=tk.RIGHT)
scroll_bar.configure(command=chat_listbox.yview)
chat_listbox.configure(yscrollcommand=scroll_bar.set)


def exit_program():
    if messagebox.askokcancel("Exit", "Are you sure you want to exit?"):
        fun_talk("Exiting Sir...")
        sys.exit()
    root.destroy()

def fun_talk(audio):
    engine.say(audio)
    engine.runAndWait()

def update_chat_list(text):
    chat_listbox.insert(tk.END, text)  # Insert text to the chat_listbox
    output_text.insert(tk.END, text + '\n')  # Insert text to the output_text

def wish_user():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        fun_talk("Good Morning !")
    elif hour >= 12 and hour < 18:
        fun_talk("Good Afternoon !")
    else:
        fun_talk("Good Evening !")
    output = f"I am Point an (Ai Assistant). Tell me how may I help you."
    output = f"{output}"
    update_chat_list(output)
    fun_talk(output)

def get_command():
    rec = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        rec.pause_threshold = 1
        audio = rec.listen(source)

        try:
            print(f"Recognizing...")
            query = rec.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
            output = f"User said: {query}\n"
            update_chat_list(output)
            return query.lower()
        except sr.UnknownValueError:
            print(f"Google Speech Recognition could not understand audio")
            output = f"Google Speech Recognition could not understand audio"
            update_chat_list(output)
            return "None"
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {0}".format(e))
            output = f"Could not request results from Google Speech Recognition service; {e}"
            update_chat_list(output)
            return "None"
        except Exception as e:
            print(e)
            print(f"Say that again please...")
            output = f"Error: {e}\nSay that again please..."
            update_chat_list(output)
            return "None"



def speak():
    wish_user()
    while True:
        query = get_command()
        home_user_dir = os.path.expanduser("~")

        if 'image' in query:
            fun_talk("Please provide the desired keywords to search related Images")
            txt=get_command()
            fun_talk("Providing Images of"+txt)
            response=requests.get("https://source.unsplash.com/random?{0}".format(txt))
            file=open('sample_image.jpg','wb')
            file.write(response.content)
            img=Image.open(r"sample_image.jpg")
            img.show()
            file.close

        elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")

        elif 'open google' in query:
            webbrowser.open("www.google.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            fun_talk(f"The time is {strTime}")

        elif 'the date' in query:
            strDate = datetime.datetime.today().strftime('%Y-%m-%d')
            print(strDate)
            fun_talk(f"The date is {strDate}")

        elif 'open visual studio code' in query:
            os.startfile(home_user_dir + "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\"
                         "Programs\\Visual Studio Code\\Visual Studio Code")

        elif 'open notepad' in query:
            os.startfile("C:\\Windows\\notepad.exe")

        elif 'open charm' in query:
            os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\JetBrains\PyCharm Community Edition 2023.1.2.lnk")

        elif 'open mozilla firefox' in query:
            os.startfile("C:\\Program Files\\Mozilla Firefox\\firefox.exe")

        elif 'open chrome' in query:
            os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

        elif 'who are you' in query:
            fun_talk("I am POINT an (AI Assistant), developed by INNOVATO INC. ""Created as a project in their college.")

        elif 'what you want to do' in query:
            fun_talk("I want to help people to do certain tasks on their single voice commands.")

        elif 'alexa' in query:
            fun_talk("I don't know Alexa, but I've heard of Alexa. If you have Alexa")

        elif 'google assistant' in query:
            fun_talk("He was my classmate, too intelligent guy. We both are best friends.")

        elif 'siri' in query:
            fun_talk("Siri, She's a competing virtual assistant on a competitor's phone. "
                        "Not that I'm competitive or anything.")

        elif 'cortana' in query:
            fun_talk("I thought you'd never ask. So I've never thought about it.")

        elif 'python assistant' in query:
            fun_talk("Are you joking. You're coming in loud and clear.")

        elif 'what language you use' in query:
            fun_talk("I am written in Python and I generally speak english.")


        elif 'play' in query:
            cmd_info = query.replace('play', '')
            fun_talk(f'Playing {cmd_info} ')
            print(cmd_info)
            pywhatkit.playonyt(cmd_info)

        elif 'search' in query:
            query = query.replace('search', '')
            pywhatkit.search(query)

        elif 'set alarm' in query:
            fun_talk("Tell me the time to set an Alarm. For example, set an alarm for 11:21 AM")
            a_info = get_command()
            a_info = a_info.replace('set an alarm for', '')
            a_info = a_info.replace('.', '')
            a_info = a_info.upper()
            MyAlarm.alarm(a_info)

        elif 'close command prompt' in query:
            os.system("TASKKILL /F /IM cmd.exe")

        elif 'close firefox' in query:
            os.system("TASKKILL /F /IM firefox.exe")
            # subprocess.call(["taskkill", "/F", "/IM", "firefox.exe"])

        elif 'close visual studio code' in query:
            os.system("TASKKILL /F /IM Code.exe")

        elif 'close eclipse' in query:
            os.system("TASKKILL /F /IM eclipse.exe")

        elif 'close notepad' in query:
            os.system("TASKKILL /F /IM notepad.exe")

        elif 'close charm' in query:
            os.system("TASKKILL /F /IM pycharm64.exe")

        elif 'close chrome' in query:
            os.system("TASKKILL /F /IM chrome.exe")

        elif 'close spotify' in query:
            os.system("TASKKILL /F /IM Spotify.exe")

        elif 'price of' in query:
            query = query.replace('price of', '')
            query = "https://www.amazon.in/s?k=" + query[-1] #indexing since I only want the keyword
            webbrowser.open(query)

        elif 'resume' in query or 'pause' in query:
            pyautogui.press("playpause")

        elif 'previous' in query:
            pyautogui.press("prevtrack")

        elif 'next' in query:
            pyautogui.press("nexttrack")

        elif 'convert currency' in query:
            try:
                curr_list = {
                    'dollar': 'USD', 'taka': 'BDT', 'dinar': 'BHD',
                    'rupee': 'INR', 'afghani': 'AFN', 'real': 'BRL',
                    'yen': 'JPY', 'peso': 'ARS', 'pound': 'EGP', 'rial': 'OMR',
                    'lek': 'ALL', 'kwanza': 'AOA', 'manat': 'AZN', 'franc': 'CHF',
                    'philippines' : 'PHP'
                }

                cur = CurrencyRates()
                # print(cur.get_rate('USD', 'INR'))
                fun_talk('From which currency u want to convert?')
                from_cur = get_command()
                src_cur = curr_list[from_cur.lower()]
                fun_talk('To which currency u want to convert?')
                to_cur = get_command()
                dest_cur = curr_list[to_cur.lower()]
                fun_talk('Tell me the value of currency u want to convert.')
                val_cur = float(get_command())
                # print(val_cur)
                print(cur.convert(src_cur, dest_cur, val_cur))
                        
            except Exception as e:
                print("Couldn't get what you have said, Can you say it again??")

        elif 'weather' in query or 'temperature' in query:
            try:
                fun_talk("Tell me the city name.")
                city = get_command()
                api = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=eea37893e6d01d234eca31616e48c631"
                w_data = requests.get(api).json()
                weather = w_data['weather'][0]['main']
                temp = int(w_data['main']['temp'] - 273.15)
                temp_min = int(w_data['main']['temp_min'] - 273.15)
                temp_max = int(w_data['main']['temp_max'] - 273.15)
                pressure = w_data['main']['pressure']
                humidity = w_data['main']['humidity']
                visibility = w_data['visibility']
                wind = w_data['wind']['speed']
                sunrise = time.strftime("%H:%M:%S", time.gmtime(w_data['sys']['sunrise'] + 19800))
                sunset = time.strftime("%H:%M:%S", time.gmtime(w_data['sys']['sunset'] + 19800))

                all_data1 = f"Condition: {weather} \nTemperature: {str(temp)}°C\n"
                all_data2 = f"Minimum Temperature: {str(temp_min)}°C \nMaximum Temperature: {str(temp_max)}°C \n" \
                            f"Pressure: {str(pressure)} millibar \nHumidity: {str(humidity)}% \n\n" \
                            f"Visibility: {str(visibility)} metres \nWind: {str(wind)} km/hr \nSunrise: {sunrise}  " \
                            f"\nSunset: {sunset}"
                fun_talk(f"Gathering the weather information of {city}...")
                print(f"Gathering the weather information of {city}...")
                print(all_data1)
                fun_talk(all_data1)
                print(all_data2)
                fun_talk(all_data2)

            except Exception as e:
                pass

        elif 'month' in query or 'month is going' in query:
            def tell_month():
                month = datetime.datetime.now().strftime("%B")
                fun_talk(month)

            tell_month()

        elif 'day' in query or 'day today' in query:
            def tell_day():
                day = datetime.datetime.now().strftime("%A")
                fun_talk(day)

            tell_day()

        elif 'quote' in query or 'quotes' in query:
            fun_talk("Tell me the author or person name.")
            q_author = get_command()
            quotes = quote(q_author)
            quote_no = random.randint(1, len(quotes))
            # print(len(quotes))
            # print(quotes)
            print("Author: ", quotes[quote_no]['author'])
            print("-->", quotes[quote_no]['quote'])
            fun_talk(f"Author: {quotes[quote_no]['author']}")
            fun_talk(f"He said {quotes[quote_no]['quote']}")

        elif 'empty recycle bin' in query or 'clear recycle bin' in query:
            try:
                winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
                print("Recycle Bin is cleaned successfully.")
                fun_talk("Recycle Bin is cleaned successfully.")

            except Exception as e:
                print("Recycle bin is already Empty.")
                fun_talk("Recycle bin is already Empty.")

        elif 'write a note' in query or 'make a note' in query:
            fun_talk("What should I write, sir??")
            note = get_command()
            file = open('Notes.txt', 'a')
            fun_talk("Should I include the date and time??")
            n_conf = get_command()
            if 'yes' in n_conf:
                str_time = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(str_time)
                file.write(" --> ")
                file.write(note)
                fun_talk("Point noted successfully.")
            else:
                file.write("\n")
                file.write(note)
                fun_talk("Point noted successfully.")

        elif 'show me the notes' in query or 'read notes' in query:
            fun_talk("Reading Notes")
            file = open("Notes.txt", "r")
            data_note = file.readlines()
            # for points in data_note:
            print(data_note)
            fun_talk(data_note)

        elif 'distance' in query:
            geocoder = Nominatim(user_agent="Josh")
            fun_talk("Tell me the first city name??")
            location1 = get_command()
            fun_talk("Tell me the second city name??")
            location2 = get_command()

            coordinates1 = geocoder.geocode(location1)
            coordinates2 = geocoder.geocode(location2)

            lat1, long1 = coordinates1.latitude, coordinates1.longitude
            lat2, long2 = coordinates2.latitude, coordinates2.longitude

            place1 = (lat1, long1)
            place2 = (lat2, long2)

            distance_places = distance.distance(place1, place2)

            print(f"The distance between {location1} and {location2} is {distance_places}.")
            fun_talk(f"The distance between {location1} and {location2} is {distance_places}")

        elif 'screenshot' in query:
            sc = pyautogui.screenshot()
            sc.save('pa_ss.png')
            print("Screenshot taken successfully.")
            fun_talk("Screenshot taken successfully.")

        elif 'volume up' in query:
            pyautogui.press("volumeup")

        elif 'volume down' in query:
            pyautogui.press("volumedown")

        elif 'mute volume' in query:
            pyautogui.press("volumemute")

        elif 'shut down' in query:
            print("Do you want to shutdown you system?")
            fun_talk("Do you want to shutdown you system?")
            cmd = get_command()
            if 'no' in cmd:
                continue
            else:
                
                os.system("shutdown /s /t 1")

        elif 'restart' in query:
            print("Do you want to restart your system?")
            fun_talk("Do you want to restart your system?")
            cmd = get_command()
            if 'no' in cmd:
                continue
            else:
                
                os.system("shutdown /r /t 1")

        elif 'logout' in query:
            print("Do you want to logout from your system?")
            fun_talk("Do you want to logout from your system?")
            cmd = get_command()
            if 'no' in cmd:
                continue
            else:
                os.system("shutdown -l")

        elif 'joke' in query:
            joke = pyjokes.get_joke()
            print(joke)
            fun_talk(joke)

        elif 'internet speed' in query:
            st = Speedtest()
            print("Wait!! I am checking your Internet Speed...")
            fun_talk("Wait!! I am checking your Internet Speed...")
            dw_speed = st.download()
            up_speed = st.upload()
            dw_speed = dw_speed / 1000000
            up_speed = up_speed / 1000000
            print('Your download speed is', round(dw_speed, 3), 'Mbps')
            print('Your upload speed is', round(up_speed, 3), 'Mbps')
            fun_talk(f'Your download speed is {round(dw_speed, 3)} Mbps')
            fun_talk(f'Your upload speed is {round(up_speed, 3)} Mbps') 

        elif 'screen recording' in query:
          fun_talk('Press Q to stop and save recording')                      #Screen recorder functionality
          Record.screen_record()
        
        elif 'snake' in query:
            try:
                print("Starting the game!")
                fun_talk("Starting the game!")
                SnakeGame.game()
            except Exception as e:
                pass
            process_query(query)

def run_console_application():
    speak()

def start_console_thread():
    # Create a new thread for the console application
    console_thread = threading.Thread(target=run_console_application)
    console_thread.start()

def process_query(query):
    if query == 'exit':
        global is_running
        is_running = False
        output = "Assistant: Exiting the program"
        update_chat_list(output)
    elif 'wikipedia' in query:
        fun_talk('Searching Wikipedia')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=3)
        fun_talk("According to Wikipedia")
        output = f"Assistant: {results}"
        update_chat_list(output)

exit_button = tk.Button(root, text="Exit", command=exit_program)
exit_button.pack(side=tk.LEFT, anchor=tk.CENTER, padx=150, pady=150)

start_console_thread()

root.mainloop()

