import requests
import time
import random
import os

# --- THE SASS BUCKETS (Add your 50+ lines here) ---

SUNNY_SASS = [
    "Miracle alert: Actual sunlight in Riga. Grab your SHADES. 😎",
    "Sun is out. Time to pretend you're a main character. 🕶️",
    "It's clear. Even the clouds found something better to do. 😎",
    "The sun is blinding. Put on shades so you don't walk into a pole. ☀️",
    "Warning: Bright orb spotted in sky. Use eye protection. 😎"
]

RAIN_SASS = [
    "It's raining. Your hair is officially a lost cause. ☔",
    "The sky is leaking again. No shades, just sadness. 🌧️",
    "Water is falling. If you wear shades now, you're a weirdo. ☔",
    "It's wet. Perfect for staying inside and doing literally nothing. 🌧️",
    "The clouds are crying. Probably because of your life choices. ☔"
]

SNOW_SASS = [
    "It's snowing. Walk like a penguin or meet the pavement. ❄️",
    "White stuff everywhere. Stay inside and drink cocoa. ❄️☕",
    "It's freezing. Your shades will just turn into ice cubes. ❄️",
    "Latvian winter has arrived. Good luck. ⛄"
]

# --- THE LOGIC ---

def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        return response.json() if response.status_code == 200 else None
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
