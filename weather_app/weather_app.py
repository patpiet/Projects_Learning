from tkinter import *
from PIL import ImageTk, Image
import requests
import json

root = Tk()
root.title('Weather App')
root.geometry("400x70")

def search():
    zipcode = zipcode_entry.get()
    try:
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode="+ zipcode_entry.get() +"&distance=5&API_KEY=19E65CA0-A4A4-4AF9-89E4-1BD6AF83DBA6")
        api = json.loads(api_request.content)
        city = api[0]['ReportingArea']
        quality = api[0]['AQI']
        category = api[0]['Category']['Name']
        color = "green"
        if category == "Good":
            color = "#00e400"
        elif category == "Moderate":
            color = "#ffff00"
        elif category == "Unhealthy for Sensitive Group":
            color = "#ff7e00"
        elif category == "Unhealthy":
            color = "#ff0000"
        elif category == "Very Unhealthy":
            color = "#99004c"
        elif category == "Hazardous":
            color = "#7e0023"
        else:
            color = "white"

        myLabel = Label(root, text=f"{city} Air Quality {quality} {category}", font=('Helvetica', 20), bg=color)
        root.configure(background=color)
        myLabel.grid(row=1, column=0, columnspan=3)
    except Exception as e:
        api = "Error..."

# https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=19E65CA0-A4A4-4AF9-89E4-1BD6AF83DBA6

zipcode_label = Label(root, text="Enter ZipCode: ")
zipcode_label.grid(row=0, column=0)

zipcode_entry = Entry(root, width=30)
zipcode_entry.grid(row=0, column=1)

zipcode_button = Button(root, text="Submit", command=search)
zipcode_button.grid(row=0, column=2, columnspan=2)

root.mainloop()