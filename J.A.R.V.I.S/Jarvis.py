import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
import wolframalpha
import json
import requests


print('''
     _     _      ______     _____   ____   
    | |   / \    |  _ \ \   / /_ _| / ___|  
 _  | |  / _ \   | |_) \ \ / / | |  \___ \  
| |_| | / ___ \ _|  _ < \ V /_ | | _ ___) | 
 \___(_)_/   \_(_)_| \_(_)_/(_)___(_)____(_)
''')



engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[1].id')


def say(text):
    engine.say(text)
    engine.runAndWait()  

say('all the systems,is online')    
     
def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        say("Hello,Good Morning Sir")
        print("Hello,Good Morning Sir")
    elif hour>=12 and hour<18:
        say("Hello,Good Afternoon Sir")
        print("Hello,Good Afternoon Sir")
    else:
        say("Hello,Good Evening Sir")
        print("Hello,Good Evening Sir")


def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        audio=r.listen(source)

        try:
            voice=r.recognize_google(audio,language='en-in')
            print(f"➥ {voice}\n")

        except Exception as e:
            print(e)
            return "None"
        return voice

wishMe()


if __name__=='__main__':


    while True:
        voice = takeCommand().lower()
        if voice==0:
            continue
        
        
        elif "are you there" in voice or "you there" in voice:
            say('at your serviceSir')

       
        if "good bye" in voice or "go offline" in voice or "stop" in voice or "shutdown" in voice or "goodbye" in voice:
            say('your personal assistant JARVİS is shutting down Sir,Good bye')
            print('your personal assistant JARVİS is shutting down Sir,Good bye')
            break



        if 'wikipedia' in voice:
            say('Searching Wikipedia Sir... ')
            voice =voice.replace("wikipedia", "")
            results = wikipedia.summary(voice, sentences=3)
            say("According to Wikipedia Sir")
            print(results)
            say(results)
        
        elif "open twitch" in voice or "twitch" in voice:
            say('twitch is open now Sir')
            webbrowser.open_new_tab("https://www.twitch.tv")
        
        elif 'open instagram' in voice or "instagram" in voice:
            webbrowser.open_new_tab("https://www.instagram.com")
            say("instagram is open now Sir")
            time.sleep(5)
             
        elif 'open youtube' in voice or "youtube" in voice:
            webbrowser.open_new_tab("https://www.youtube.com")
            say("youtube is open now Sir")
            time.sleep(5)

        elif 'open google' in voice or "google" in voice:
            webbrowser.open_new_tab("https://www.google.com")
            say("Google chrome is open now Sir")
            time.sleep(5)

        elif 'open gmail' in voice or "gmail" in voice:
            webbrowser.open_new_tab("gmail.com")
            say("Google Mail open now Sir")
            time.sleep(5)

        elif "weather" in voice:
            api_key="8ef61edcf1c576d65d836254e11ea420"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            say("whats the city name,Sir")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                say(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

            else:
                say(" City Not Found Sir ")



        elif 'time' in voice:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            say(f"the time is {strTime}")

        elif 'who are you' in voice or 'what can you do' in voice:
            say('I am JARVİS your personal assistant,Just A Rather Very Intelligent System , '
                  'opening youtube,twitch,instagram,google,gmail and github ,predict time,search wikipedia,predict weather' 
                  'in different cities , get top headline news from times of Turkey and you can ask me computational or geographical questions too!')


        elif "who made you" in voice or "who created you" in voice or "who discovered you" in voice:
            say("I was built by Ahmet Enes")
            print("I was built by Ahmet Enes")

        elif "open github" in voice or "github" in voice:
            webbrowser.open_new_tab("https://github.com")
            say("Here is GitHub Sir")

        elif 'news' in voice:
            news = webbrowser.open_new_tab("https://tr.timesofturkey.com")
            say('Here are some headlines from the Times of Turkey,Happy reading sir')
            time.sleep(6)
        
        elif 'search'  in voice:
            voice = voice.replace("search", "")
            webbrowser.open_new_tab(voice)
            time.sleep(5)

        elif 'ask' in voice:
            say('I can answer to computational and geographical questions and what question do you want to ask now Sir')
            question=takeCommand()
            app_id="W7H935-VR7WJEVE7X"
            client = wolframalpha.Client('W7H935-VR7WJEVE7X')
            res = client.query(question)
            answer = next(res.results).text
            say(answer)
            print(answer)


        elif "log off" in voice or "sign out" in voice:
            say("Ok , your pc will log off in 10 sec make sure you exit from all applications sir")
            subprocess.call(["shutdown", "/l"])
            
        elif "open the helmet" in voice:
            say("okey sir i m opening the helmet") 
        
        elif"close the helmet" in voice:
            say('okey sir i m closing the helmet')
            
        elif"activate Barn Door protocol" in voice or "say" in voice:
            say('okey sir i m activateing Barn Door Protocol')

        elif"how are you" in voice:
            say('i m fine sir,thank you') 
                
        elif "sing me" in voice or "sing song" in voice or "sing"in voice or "song" in voice:
            say('okey sir')
            webbrowser.open_new_tab("https://open.spotify.com/playlist/6nHEen8hAih5mdDFHOe5Nq?si=806c8eb1c152401e")
        

time.sleep(3)

















