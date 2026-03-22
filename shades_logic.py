import requests
import time
import random
import os

# --- THE SASS LIBRARY (Your Goal: 50 per category!) ---
SASS_LIBRARY = {
    "Clear": [
        "Miracle alert: Actual sunlight. Grab your SHADES. 😎",
        "The sun is out. Don't let it see you looking like a hermit. ☀️",
        "Warning: Bright orb spotted. Eye protection recommended. 🕶️",
        "Go outside before the clouds realize they're missing. 🏃‍♂️",
        "It's clear. Even the sky has more clarity than your future. Ouch. 😎"
    ],
    "Clouds": [
        "It's 50 shades of grey, and none of them are interesting. ☁️💀",
        "The sky looks like a bowl of cold oatmeal. 🥣",
        "Riga status: 100% Grey. Welcome to the flat-light depression. ☁️",
        "No shades needed. The clouds are acting like a giant, sad blanket. ☁️",
        "It's not raining, it's just 'Pre-Rain'. Classic. ☁️"
    ],
    "Rain": [
        "The sky is leaking. Your hair is officially a lost cause. ☔",
        "Welcome to the 'Riga Special'. Water is falling. 🌧️",
        "If you wear shades now, everyone will know you're a weirdo. ☔🚔",
        "Free shower! Too bad it's cold and smells like wet concrete. 🌧️"
    ],
    "Drizzle": [
        "It's barely raining, but enough to be annoying. Static rain. 🌫️",
        "It's like the sky has a leaky faucet. 🌧️"
    ],
    "Snow": [
        "White stuff everywhere. Walk like a penguin or meet the pavement. ❄️",
        "Latvian winter has arrived. Good luck, you'll need it. ⛄",
        "The air is spicy and frozen. Stay inside and hide. ❄️"
    ],
    "Thunderstorm": [
        "Thor is angry. Put the shades away and find a roof. ⛈️",
        "Lightning! Nature's way of taking a photo of you looking wet. ⛈️"
    ],
    "Mist": [
        "Visibility: Zero. You don't need shades, you need a foghorn. 🌫️",
        "It's like walking through a damp ghost. 👻"
    ],
    "Windy": [
        "It's windy enough to fly to Estonia without a plane. 🌬️",
        "The Daugava wind is trying to steal your face. Hold on. 🌬️"
    ]
}

def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        r = requests.get(url)
        if r.status_code == 200:
            data = r.json()
            return {
                "temp": data['main']['temp'],
                "condition": data['weather'][0]['main'],
                "wind": data['wind']['speed']
            }
        return None
    except:
        return None

def start_shades():
    # We pull the key from your .env logic
    MY_KEY = "6937a3320b215aa90b8a667873fc651a"
    CITY = "Riga"
    last_condition = None

    while True:
        data = get_weather(CITY, MY_KEY)
        if data:
            cond = data['condition']
            wind = data['wind']
            
            # --- WHICH DRAWER DO WE OPEN? ---
            if wind > 8: # If it's windy, prioritize that
                drawer = "Windy"
            elif cond in SASS_LIBRARY:
                drawer = cond
            else:
                drawer = "Clouds" # Default for Riga

            if drawer != last_condition:
                msg = random.choice(SASS_LIBRARY[drawer])
                # Show in terminal
                print(f"[{time.strftime('%H:%M')}] ALERT: {msg}")
                # Mac Notification
                os.system(f"osascript -e 'display notification \"{msg}\" with title \"🕶️ SHADES ALERT\"'")
                last_condition = drawer
        
        time.sleep(600) # Check every 10 mins

if __name__ == "__main__":
    start_shades()        return response.json() if response.status_code == 200 else None
    except:
        return None

def send_notification(message):
    # This works on Mac. For Windows, we'd use 'plyer' or 'win10toast'
    os.system(f"osascript -e 'display notification \"{message}\" with title \"🕶️ SHADES ALERT\"'")

def start_shades():
    MY_KEY = "6937a3320b215aa90b8a667873fc651a"
    CITY = "Riga"
    
    last_condition = None # This is the app's 'Memory'
    
    print(f"--- 🕶️ SHADES IS WATCHING {CITY.upper()} ---")

    while True:
        data = get_weather(CITY, MY_KEY)
        
        if data:
            current_temp = data['main']['temp']
            current_condition = data['weather'][0]['main']
            
            # --- ONLY NOTIFY IF THE WEATHER CHANGES ---
            if current_condition != last_condition:
                
                if "Clear" in current_condition:
                    msg = random.choice(SUNNY_SASS)
                elif "Rain" in current_condition or "Drizzle" in current_condition:
                    msg = random.choice(RAIN_SASS)
                elif "Snow" in current_condition:
                    msg = random.choice(SNOW_SASS)
                else:
                    msg = f"It's {current_temp}°C and {current_condition}. Mid. 🤷‍♂️"
                
                send_notification(msg)
                print(f"ALERT SENT: {msg}")
                
                # Update memory so we don't spam the same thing
                last_condition = current_condition 
            else:
                print(f"[{time.strftime('%H:%M')}] Weather is still {current_condition}. Staying quiet.")

        # Check every 10 minutes, but only NOTIFY if something changed
        time.sleep(600) 

if __name__ == "__main__":
    start_shades()
