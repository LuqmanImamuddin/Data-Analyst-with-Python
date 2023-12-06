import tkinter as tk
from datetime import timedelta
from datetime import datetime
import time
import webbrowser
import subprocess
import os

def convert_to_seconds(time_format):
    hours, minutes, seconds = map(int, time_format.split(':'))
    total_seconds = hours * 3600 + minutes * 60 + seconds
    return total_seconds

class Dota2Tracker:
    def __init__(self, master):
        self.master = master
        self.master.title("Dota 2 Playtime Tracker")

        self.open_button = tk.Button(self.master, text="Open Dota 2", command=self.open_dota2)
        self.open_button.pack()

        self.close_button = tk.Button(self.master, text="Close Dota 2", command=self.close_dota2, state=tk.DISABLED)
        self.close_button.pack()

    def open_dota2(self):
        # Change the URL to the Dota 2 internet shortcut
        url = "steam://rungameid/570"
        webbrowser.open(url)
        
        self.dota2_running = True
        self.playtime_start = time.time()
        self.open_button.config(state=tk.DISABLED)
        self.close_button.config(state=tk.NORMAL)

    def close_dota2(self):
        subprocess.Popen("taskkill /f /im Dota2.exe")  # Close Dota 2
        if self.dota2_running:
            self.dota2_running = False
            self.open_button.config(state=tk.NORMAL)
            self.close_button.config(state=tk.DISABLED)
            self.save_playtime()

    def save_playtime(self):
        playtime_seconds = int(time.time() - self.playtime_start)
        playtime_timedelta = timedelta(seconds=playtime_seconds)
        hours, remainder = divmod(playtime_timedelta.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
    
        current_datetime = datetime.now()
        formatted_datetime = current_datetime.strftime("%d/%m/%Y")
    
        file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "Playtime_PowerBI.csv")
        with open(file_path, "a") as file:
            file.write(f"{formatted_datetime};{int(hours)};{int(minutes)};{int(seconds)}\n")

if __name__ == "__main__":
    root = tk.Tk()
    dota2_tracker = Dota2Tracker(root)
    root.mainloop()
