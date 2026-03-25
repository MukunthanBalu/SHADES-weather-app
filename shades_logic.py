import requests
import time
import random
import os
import sys

# --- THE EXPANDED SASS LIBRARY (The 'Soul' of the App) ---
SASS_LIBRARY = {
    "Clear": [
        "Miracle alert: Actual sunlight. Grab your SHADES. 😎",
        "The sun is out. Don't let it see you looking like a ghost. ☀️",
        "Warning: Bright orb spotted. Eye protection recommended. 🕶️",
        "Go outside before the clouds realize they're missing. 🏃‍♂️",
        "It's clear. Even the sky has more clarity than your future. Ouch. 😎",
        "The sun is basically a giant flashbang today. Protect those eyes. 💥",
        "If you stay inside now, you're legally a vampire. 🧛‍♂️",
        "Sun's out, guns out. But mostly, shades on. 🕶️",
        "Perfect weather for people who actually have a life. Go join them. 🚶‍♂️",
        "Blue skies? In this economy? Enjoy it while it lasts. 💸"
    ],
    "Clouds": [
        "It's 50 shades of grey, and none of them are interesting. ☁️💀",
        "The sky looks like a bowl of cold oatmeal. 🥣",
        "Riga status: 100% Grey. Welcome to the flat-light depression. ☁️",
        "No shades needed. The clouds are acting like a giant, sad blanket. ☁️",
        "It's not raining, it's just 'Pre-Rain'. Classic. ☁️",
        "The sky is buffering. Please wait for actual weather. ⏳",
        "Standard Baltic lighting: 'Despair Grey' #808080. 🎨",
        "Even the sun couldn't be bothered to show up today. 😴",
        "It's like living inside a giant tupperware container. ☁️",
        "The clouds are just nature's way of saying 'Meh'. 🤷‍♂️"
    ],
    "Rain": [
        "The sky is leaking. Your hair is officially a lost cause. ☔",
        "Welcome to the 'Riga Special'. Water is falling. 🌧️",
        "If you wear shades now, everyone will know you're a weirdo. ☔",
        "Free shower! Too bad it's cold and smells like wet concrete. 🌧️",
        "It's raining. Time to practice your 'sad protagonist' window look. 🪟",
        "God is crying because of your commit history. 🌧️",
        "The Daugava is rising, and so is your level of annoyance. 🌊",
        "Wet socks: The ultimate prize for going outside right now. 🧦",
        "Rain. Again. Groundbreaking. 🙄",
        "Unless you're a duck, today is a total write-off. 🦆"
    ],
    "Drizzle": [
        "It's just a little drizzle. Stop being a baby. 🌧️",
        "The sky is just sweating. No big deal. ☔",
        "It's that annoying mist that ruins your glasses but doesn't water the plants. 👓"
    ],
    "Snow": [
        "White stuff everywhere. Walk like a penguin or meet the pavement. ❄️",
        "Latvian winter has arrived. Good luck, you'll need it. ⛄",
        "The air is spicy and frozen. Stay inside and hide. ❄️",
        "Congrats! Everything is now slippery and dangerous. 🎿",
        "It's a winter wonderland, if your 'wonderland' involves frostbite. ❄️"
    ],
    "Thunderstorm": [
        "Thor is angry. Put the shades away and find a roof. ⛈️",
        "Lightning! Nature's way of taking a photo of you looking wet. ⛈️",
        "The sky is literally screaming. Maybe stay away from tall metal poles. ⚡"
    ],
    "Mist": [
        "Visibility: Zero. You don't need shades, you need a foghorn. 🌫️",
        "It's like walking through a damp ghost. 👻",
        "Silent Hill vibes today. Watch out for pyramid heads. 🌫️"
    ],
    "Windy": [
        "It's windy enough to fly to Estonia without a plane. 🌬️",
        "The Daugava wind is trying to steal your face. Hold on. 🌬️",
        "Hold onto your hat, your dignity, and your small pets. 🌪️"
    ]
}

def get_weather(city, api_key):
    """ Calls OpenWeather API and handles potential errors gracefully """
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    
    try:
        response = requests.get(base_url, params=params, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            return {
                "temp": data['main']['temp'],
                "condition": data['weather'][0]['main'],
                "wind_speed": data['wind']['speed'],
                "city_name": data['name']
            }
        elif response.status_code == 401:
            print("❌ ERROR: Invalid API Key. Check your .env file.")
            return "AUTH_ERROR"
        else:
            print(f"❌ ERROR: Received status code {response.status_code}")
            return None
            
    except requests.exceptions.ConnectionError:
        print("❌ ERROR: No internet connection. Shades can't see the sky.")
        return None
    except Exception as e:
        print(f"❌ UNEXPECTED ERROR: {e}")
        return None

def send_mac_notification(message):
    """ Uses AppleScript to push a native macOS notification """
    title = "🕶️ SHADES ALERT"
    safe_msg = message.replace('"', '\\"') # Prevent quotes from breaking the command
    command = f'display notification "{safe_msg}" with title "{title}"'
    os.system(f"osascript -e '{command}'")

def start_shades():
    # Attempt to load API Key from environment or use fallback
    API_KEY = os.getenv("OPENWEATHER_API_KEY", "6937a3320b215aa90b8a667873fc651a")
    CITY = "Riga"
    last_drawer = None

    print("\n" + "="*45)
    print(f"🕶️  SHADES V1.0 - ACTIVATED AND WATCHING {CITY.upper()}")
    print("="*45)
    print("Pulse check: Every 10 minutes.")
    print("Press Ctrl+C to stop the roast.\n")

    while True:
        weather_data = get_weather(CITY, API_KEY)
        
        if weather_data == "AUTH_ERROR":
            break # Exit if key is bad
            
        if weather_data:
            current_cond = weather_data['condition']
            wind = weather_data['wind_speed']
            
            # Logic Engine: Deciding which 'Sass Drawer' to open
            if wind > 8.5:
                active_drawer = "Windy"
            elif current_cond in SASS_LIBRARY:
                active_drawer = current_cond
            else:
                active_drawer = "Clouds"

            # State Management: Only notify if the weather CATEGORY has changed
            if active_drawer != last_drawer:
                selected_sass = random.choice(SASS_LIBRARY[active_drawer])
                timestamp = time.strftime('%H:%M:%S')
                
                print(f"[{timestamp}] 🚩 CHANGE DETECTED: {active_drawer}")
                print(f"[{timestamp}] SASS: {selected_sass}\n")
                
                send_mac_notification(selected_sass)
                last_drawer = active_drawer
            else:
                # Still log to terminal so you know it's working
                print(f"[{time.strftime('%H:%M:%S')}] Weather is still {active_drawer}. No new alerts.")
        
        # Hibernate for 600 seconds (10 mins)
        time.sleep(600)

if __name__ == "__main__":
    try:
        start_shades()
    except KeyboardInterrupt:
        print("\n\n🕶️  SHADES shutting down. Go outside (or don't, I'm a script, not your mom).")
        sys.exit()
