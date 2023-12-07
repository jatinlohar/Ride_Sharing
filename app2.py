import tkinter as tk
from ctypes import *
import time

class StringInputApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Traveler Companion")
        self.mess = None
        # self.root.title("String Input App")

        # Entry widget for text input
        self.input_entry = tk.Entry(self.root, width=30)
        self.input_entry.grid(row=0, column=0, padx=10, pady=10)

        # Send button
        self.send_button = tk.Button(self.root, text="Send", command=self.send_action)
        self.send_button.grid(row=1, column=0, pady=10)

        self.send_button = tk.Button(self.root, text="Recieve", command=self.recieve_action)
        self.send_button.grid(row=2, column=0, pady=10)


        self.send_button = tk.Button(self.root, text="Cancel", command=self.close_action)
        self.send_button.grid(row=3, column=0, pady=10)

        

    def send_action(self):
        # Get the entered text from the Entry widget
        self.mess = self.input_entry.get()

        # Perform an action with the entered text (replace this with your desired action)
        self.root.destroy()
    
    def recieve_action(self):
        # Get the entered text from the Entry widget
        self.mess = " "

        # Perform an action with the entered text (replace this with your desired action)
        self.root.destroy()


    def close_action(self):
        self.root.destroy()
        # time.sleep(30)
    
    def complete_action(self):
        self.mess = "Ride Completed"
        self.root.destroy()
        # time.sleep(30)


if __name__ == "__main__":

    so_file = "/home/jatin/Codes/MoveinSync/my_functions2.so"
    my_functions = CDLL(so_file)

    msg = "."
    my_functions.client(msg)
    while(True):
        
        root = tk.Tk()
        app = StringInputApp(root)
        root.mainloop()

        if(app.mess is None):
            my_functions.client("")
            time.sleep(30)
            # app2.mess = message
        else:
            msg = app.mess.encode('utf-8')
            my_functions.client(msg)



