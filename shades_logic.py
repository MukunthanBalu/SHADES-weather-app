def get_shades_comment(weather_condition):
    comments = {
        "Wind": "Wind today. Your umbrella might become a kite.",
        "Snow": "Snow today. Umbrella optional but dramatic.",
        "Rain": "Rain today. Free shower, but your hair won't like it.",
        "Sunny": "Sun is out. Don't forget your 'Shades' and some attitude."
    }
    return comments.get(weather_condition, "Weather's doing its thing. Stay cool.")

# Test it
current_weather = "Wind"
print(f"SHADES says: {get_shades_comment(current_weather)}")
