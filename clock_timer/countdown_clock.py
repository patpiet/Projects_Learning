import time
from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("Countdown App")
root.geometry("300x250")

# Create count variables
hour = StringVar()
minute = StringVar()
second = StringVar()
title = StringVar()

hour.set("00")
minute.set("00")
second.set("00")

# Create Labels
hour_label = Label(root, text="HOUR")
hour_label.place(x=80, y=10)
minute_label = Label(root, text="MINUTE")
minute_label.place(x=126, y=10)
second_label = Label(root, text="SECOND")
second_label.place(x=176, y=10)
title_label = Label(root, text="Alarm title:")
title_label.place(x=120, y=120)

# Create Entries
hourEntry = Entry(root, width=3, font=("Arial", 18, ""), textvariable=hour)
hourEntry.place(x=80, y=30)
minuteEntry = Entry(root, width=3, font=("Arial", 18, ""), textvariable=minute)
minuteEntry.place(x=130,y=30)
minuteEntry = Entry(root, width=3, font=("Arial", 18, ""), textvariable=second)
minuteEntry.place(x=180,y=30)
titleEntry = Entry(root, width=40, font=("Arial", 9, ""), textvariable=title)
titleEntry.place(x=10, y=140)

def submit():
    title_inside = titleEntry.get()
    try:
        # Input provided by user = temp
        temp = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
    except:
        error_label = Label(root, text="Please enter the right value!")
        error_label.place(x=76, y=60)
    while temp > -1:
        mins, secs = divmod(temp, 60)

        hours = 0
        if mins > 60:
            hours, mins = divmod(mins, 60)
        hour.set("{0:2d}".format(hours))
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))
        root.update()
        time.sleep(1)

        if temp == 0:
            messagebox.showinfo("Time Countdown!", title_inside)

        temp -= 1

btn = Button(root, text='Set Time Countdown', bd='5', command = submit)
btn.place(x = 87,y = 200)


root.mainloop()
