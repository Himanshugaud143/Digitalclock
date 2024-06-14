import tkinter as tk
from time import strftime
from datetime import datetime

class AdvancedClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Digital Clock")
        self.root.geometry("400x150")

        # Configure the main window
        self.root.configure(bg='black')

        # Create and configure the time label
        self.time_label = tk.Label(root, font=('Georgia', 40, 'bold', 'italic'), bg='black', fg='darkseagreen')
        self.time_label.pack(anchor='center', pady=10)

        # Create and configure the date label
        self.date_label = tk.Label(root, font=('Georgia', 15, 'bold', 'italic'), bg='black', fg='yellow')
        self.date_label.pack(anchor='center')

        # Start updating the time and date
        self.update_time()

    def update_time(self):
        # Get the current time, date, and day of the week
        current_time = strftime('%H:%M:%S %p')
        current_date = datetime.now().strftime('%A, %B %d, %Y')
        
        # Update the labels
        self.time_label.config(text=current_time)
        self.date_label.config(text=current_date)

        # Schedule the update_time function to be called every 1000 milliseconds (1 second)
        self.time_label.after(1000, self.update_time)

# Create the main window
root = tk.Tk()
clock = AdvancedClock(root)

# Run the application
root.mainloop()
