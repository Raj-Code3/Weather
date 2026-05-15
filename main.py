from tkinter import *
from tkinter import messagebox
import requests

API_KEY = "197ea89007b64552bf770849261505"


BG_COLOR = "#2E2E2E"
TEXT_COLOR = "white"
BUTTON_COLOR = "#3A3A3A"


root = Tk()
root.title("Weather Application")
root.geometry("700x450")
root.configure(bg=BG_COLOR)


def get_weather():

    city = city_entry.get()

    if city == "":
        messagebox.showerror("Error", "Please enter city name")
        return

    try:

        url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"

        response = requests.get(url)

        data = response.json()


        if "error" in data:
            messagebox.showerror("Error", "City not found")
            return

        
        city_name = data["location"]["name"]
        country = data["location"]["country"]

        temp = data["current"]["temp_c"]
        humidity = data["current"]["humidity"]
        pressure = data["current"]["pressure_mb"]
        wind = data["current"]["wind_kph"]

        description = data["current"]["condition"]["text"]

        
        weather_text = f"""
               Current Weather

City        : {city_name}
Country     : {country}

Temperature : {temp} °C
Humidity    : {humidity} %
Pressure    : {pressure} mb
Wind Speed  : {wind} kph
Condition   : {description}
"""

        result_label.config(text=weather_text)

       
        with open("weather_logs.txt", "a") as file:

            file.write(
                f"{city_name} | {temp}°C | {description}\n"
            )

    except Exception as e:

        messagebox.showerror("Error", str(e))



top_frame = Frame(root, bg=BG_COLOR)
top_frame.pack(pady=20)



city_label = Label(
    top_frame,
    text="Enter City Name:",
    bg=BG_COLOR,
    fg=TEXT_COLOR,
    font=("Arial", 14)
)

city_label.grid(row=0, column=0, padx=10)


city_entry = Entry(
    top_frame,
    width=25,
    font=("Arial", 14)
)

city_entry.grid(row=0, column=1, padx=10)


fetch_button = Button(
    top_frame,
    text="Fetch Weather",
    command=get_weather,
    bg=BUTTON_COLOR,
    fg=TEXT_COLOR,
    font=("Arial", 12),
    padx=15,
    pady=5
)

fetch_button.grid(row=0, column=2, padx=10)


result_label = Label(
    root,
    text="",
    bg=BG_COLOR,
    fg=TEXT_COLOR,
    font=("Arial", 18),
    justify=LEFT
)

result_label.pack(pady=30)


root.mainloop()