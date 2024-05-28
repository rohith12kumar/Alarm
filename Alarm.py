from tkinter import *
import datetime
import time
import winsound
from threading import *

# Create Object
root = Tk()

# Set geometry
root.geometry("400x300")
root.title("Advanced Alarm Clock")

alarm_active = False

def Threading():
    t1 = Thread(target=alarm)
    t1.start()


def alarm():
    global alarm_active
    alarm_active = True
    # Infinite Loop
    while alarm_active:
        # Set Alarm
        set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"

        # Wait for one second
        time.sleep(1)

        # Get current time
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        time_display.config(text="Current Time: " + current_time)

        # It Check's whether set alarm is equal to current time or not
        if current_time == set_alarm_time and alarm_active:
            alarm_label.config(text="Time to Wake Up!")
            # Playing sound
            winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
            alarm_active = False  # Stop the alarm after it goes off


def stop_alarm():
    global alarm_active
    alarm_active = False
    winsound.PlaySound(None, winsound.SND_ASYNC)
    alarm_label.config(text="")


# Add Labels, Frame, Button, Optionmenus
Label(root, text="Alarm Clock", font=("Helvetica 20 bold"), fg="red").pack(pady=10)
Label(root, text="Set Time", font=("Helvetica 15 bold")).pack()

frame = Frame(root)
frame.pack()

hour = StringVar(root)
hours = ('00', '01', '02', '03', '04', '05', '06', '07',
         '08', '09', '10', '11', '12', '13', '14', '15',
         '16', '17', '18', '19', '20', '21', '22', '23')
hour.set(hours[0])

hrs = OptionMenu(frame, hour, *hours)
hrs.pack(side=LEFT)

minute = StringVar(root)
minutes = ('00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59')
minute.set(minutes[0])

mins = OptionMenu(frame, minute, *minutes)
mins.pack(side=LEFT)

second = StringVar(root)
seconds = ('00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59')
second.set(seconds[0])

secs = OptionMenu(frame, second, *seconds)
secs.pack(side=LEFT)

Button(root, text="Set Alarm", font=("Helvetica 15"), command=Threading).pack(pady=20)

# used to show the current time
time_display = Label(root, text="", font=("Helvetica 12"))
time_display.pack()

# used to show the alarm status
alarm_label = Label(root, text="", font=("Helvetica 12 bold"), fg="blue")
alarm_label.pack()

# used for  stop the alarm
Button(root, text="Stop Alarm", font=("Helvetica 15"), command=stop_alarm).pack(pady=20)

# Execute Tkinter
root.mainloop()
