import pyttsx3

import speech_recognition as sr
import datetime
import wikipedia
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import pyautogui
# Use female voice
import pyperclip
hiddenimports = [
   'pyttsx3.drivers',
   'pyttsx3.drivers.dummy',
   'pyttsx3.drivers.espeak',
   'pyttsx3.drivers.nsss',
   'pyttsx3.drivers.sapi5', ]

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voice')
engine.setProperty('voice', voices)
engine.setProperty('rate', 150)
engine.setProperty('volume', 10)

def speak(audio):
 engine.say(audio)
 engine.runAndWait()

speak('all the systems,is online')    
     
def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,Good Morning Sir")
        print("Hello,Good Morning Sir")
    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon Sir")
        print("Hello,Good Afternoon Sir")
    else:
        speak("Hello,Good Evening Sir")
        print("Hello,Good Evening Sir")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print(f"➥ {query}\n")
    except Exception as e:
        print(e)
        return "None"
    return query


def typenh():
   r = sr.Recognizer()
   with sr.Microphone() as source:
       print("Listening....")
       r.pause_threshold = 1
       audio = r.listen(source)
   try:
    print("Recognizing....")
    typethingh = r.recognize_google(audio, language='hi')
    print(f"user said: {typethingh}\n")
   except Exception as e:
     print(e)
     speak("sorry I could not understand, say that again please...")
     return "None"
   return typethingh

i = 0


n = 0
k = 0

print("Say Jarvis To Begin Initiation Sequence") #Sounds SICK Right!
while (i<1):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.adjust_for_ambient_noise(source)
        n=(n+1)
        audio = r.listen(source)
        # interprete audio (Google Speech Recognition)
    try:
        s = (r.recognize_google(audio))
        message = (s.lower())

        if message == "jarvis":
            wishMe()
            k = 0
            while k == 0:
                query = takecommand().lower()
                query.replace("could you", "")
                query.replace("please", "")

                if 'go offline' in query:
                    k = 1

                if 'wikipedia' in query:
                       speak('searching Wikipedia...')
                       query = query.replace("wikipedia", "")
                       results = wikipedia.summary(query, sentences=2)
                       speak("according to wikipedia")
                       speak(results)
                if 'manav sampada' in query:
                       speak('loging in to manav sampada')
                       browser = webdriver.Chrome('D:\\chromedriver.exe')
                       browser.get('http://ehrms.upsdc.gov.in/')
                       elem = browser.find_element_by_partial_link_text('eHRMS Login')
                       elem.get_attribute('href')
                       time.sleep(1)
                       elem.click()
                       time.sleep(1)
                       loginr = browser.find_element_by_xpath('//*[@id="txtusername"]')
                       loginr.send_keys('your id ')
                       time.sleep(1)
                       select = Select(browser.find_element_by_id('ddldept'))
                       select.select_by_visible_text('Basic Education')
                       time.sleep(1)
                       password = browser.find_element_by_xpath('//*[@id="txtpwd"]')
                       password.send_keys('your password')
                       speak('sir I have filled all userID password etc. but ')
                       speak('sir you have to fill the human verification captha by yourself as I am just a bot ')
                       speak('I hope I was able to assist you')
                if 'software' in query:
                       speak('opening sir')
                       query = query.replace("software", "")
                       pyautogui.click(27, 880)
                       pyautogui.typewrite(query)
                       time.sleep(1)
                       pyautogui.click(79,441)
                if 'send' and 'gmail' in query:
                       speak('opening gmail')
                       browser = webdriver.Chrome('D:\\chromedriver.exe')
                       browser.get('https://accounts.google.com/b/0/AddMailService')
                       time.sleep(1)
                       login = browser.find_element_by_xpath('//*[@id="identifierId"]')
                       login.send_keys('your gmail id @gmail.com')
                       login.send_keys(Keys.ENTER)
                       time.sleep(1)
                       loginpwd = browser.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
                       loginpwd.send_keys('your awesom password here')
                       loginpwd.send_keys(Keys.ENTER)
                       time.sleep(10)
                       try:
                           speak('just a sec')
                           compose = browser.find_element_by_class_name('z0')
                           time.sleep(2)
                           compose.click()
                           time.sleep(1)
                           speak('whom do you want to send the gmail')
                           sendto = takecommand().lower()
                           sendto = ''.join(sendto.split())
                           tom = browser.find_element_by_name('to')
                           tom.send_keys(sendto)
                           speak('what is the subject?')
                           subject = browser.find_element_by_name('subjectbox')
                           time.sleep(0.5)
                           
                           whatissu = takecommand()
                           subject.send_keys(whatissu)
                           body = browser.find_element_by_name('Message Body')
                           speak('what is the main body?')
                           mainbody = takecommand()
                           body.send_keys(mainbody)

                       except Exception as identifier:
                           compose = browser.find_element_by_xpath('//*[@id=":jm"]/div/div')
                           time.sleep(1)
                           compose.click()
                           time.sleep(1)
                           speak('whom do you want to send the gmail')
                           sendto = takecommand().lower()
                           sendto = ''.join(sendto.split())
                           tom = browser.find_element_by_name('to')
                           tom.send_keys(sendto)                                                   
                           subject = browser.find_element_by_name('subjectbox')
                           time.sleep(0.5)
                           speak('what is the subject?')
                           whatissu = takecommand()
                           subject.send_keys(whatissu)
                           body = browser.find_element_by_name('Message Body')
                           speak('what is the main body?')
                           mainbody = takecommand()
                           body.send_keys(mainbody)            
                   
                if 'hindi' in query:
                   speak('what to type?')
                   typethingh = typenh()
                   content = typethingh
                   pyperclip.copy(content)
                   time.sleep(0.5)
                   pyautogui.hotkey('ctrl', 'v')

                if 'do you have a boyfriend' in query:
                    speak('I am happy to be single')

                if 'siri' in query:
                    speak('siri is smart but I dont like him')

                if 'how are you' in query:
                    speak('I am good ')

                if 'i hate you' in query:
                    speak('than go to siri or google. why are you even talking to me')

                if 'who is your creator' in query:
                    speak("my creater is John Cena(The OG Himself)")

                if 'who made you' in query:
                    speak('John Cena Made e. He Is An OG!')

                if 'who created you' in query:
                    speak('Booooob The BUILDER!!!')

                if 'whatsapp' in query:
                    browser = webdriver.Chrome('D:\\chromedriver.exe')
                    speak('opening whatsapp web')
                    browser.get('https://web.whatsapp.com/')
                    speak('please scan the qr code. I am waiting for 10 seconds')
                    time.sleep(10)
                    try:
                        find = browser.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
                        find.click()
                        speak('tell the first word of the contact to whom you want to send the messege')
                        sendmsg = takecommand()
                        find.send_keys(sendmsg)
                        time.sleep(1.5)
                        find.send_keys(Keys.ENTER)
                        try:
                            typenum = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
                            typenum.click()
                            speak('what do you want to send sir?')
                            whattosend = takecommand()
                            typenum.send_keys(whattosend)
                            typenum.send_keys(Keys.ENTER)
                        except Exception as identifier:
                            speak('there is no contact as'+sendmsg)
                    except Exception as identifier:
                        speak('you did not make it in 10 seconds')


                if 'quit' in query:
                   exit()

    except Exception as e:
        pass