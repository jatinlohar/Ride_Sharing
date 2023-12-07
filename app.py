import tkinter as tk
from ctypes import *
import time


class StringInputApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Traveler")
        self.mess = None
        # self.root.title("String Input App")

        # Entry widget for text input
        self.input_entry = tk.Entry(self.root, width=30)
        self.input_entry.grid(row=0, column=0, padx=10, pady=10)

        # Send button
        self.send_button = tk.Button(self.root, text="Send", command=self.send_action)
        self.send_button.grid(row=1, column=0, pady=10)

        self.send_button = tk.Button(self.root, text="Cancel", command=self.close_action)
        self.send_button.grid(row=2, column=0, pady=10)
        
        self.send_button = tk.Button(self.root, text="Ride Complete", command=self.complete_action)
        self.send_button.grid(row=3, column=0, pady=10)

    def send_action(self):
        self.mess = self.input_entry.get()

        if self.mess:
            self.root.destroy()
        else:
            print("No text entered.")

    def close_action(self):
        self.root.destroy()
        # time.sleep(30)
    
    def complete_action(self):
        self.mess = "Ride Completed"
        self.root.destroy()
        # time.sleep(30)



class CustomInputDialog:
    def __init__(self, parent, prompt):
        self.dialog = tk.Toplevel(parent)
        self.dialog.title("Custom Input")

        self.prompt_label = tk.Label(self.dialog, text=prompt)
        self.prompt_label.grid(row=0, column=0, padx=10, pady=5)

        self.input_entry = tk.Entry(self.dialog)
        self.input_entry.grid(row=1, column=0, padx=10, pady=5)

        self.ok_button = tk.Button(self.dialog, text="OK", command=self.on_ok_button)
        self.ok_button.grid(row=2, column=0, pady=10)

        self.result = None

    def on_ok_button(self):
        user_input = self.input_entry.get()

        self.result = user_input
        
        self.dialog.destroy()

    def show_dialog(self):
        self.dialog.wait_window()

class ArrayDisplayApp:
    def __init__(self, root, array):
        self.root = root
        self.root.title("Cab Drivers Details")

        self.array = array
        self.rows = len(array)
        self.columns = len(array[0])

        self.selected_row_var = tk.IntVar()
        self.selected_row = None
        self.result = None

        

        # Create OK button
        self.ok_button = tk.Button(self.root, text="OK", command=self.on_ok_button)
        self.ok_button.grid(row=self.rows + 3, column=0, columnspan=self.columns + 1)

    def create_window(self):
        self.create_widgets()

    def create_widgets(self):
        heading = ["Name of Driver", "Mobile No", "Cab Number", "Rating"]
        for j in range(self.columns):
            heading_label = tk.Label(self.root, text=heading[j], borderwidth=1, relief="solid", width=2*len(heading[j]), height=2, fg="blue", font=("Helvetica", 11, "bold"))
            heading_label.grid(row=0, column=j+1)

        # Create Radiobuttons for each row
        for i, array in enumerate(self.array):

            radio_button = tk.Radiobutton(self.root, variable=self.selected_row_var, value=i + 1)
            radio_button.grid(row=i+1, column=0, sticky=tk.W)

            for j, element in enumerate(array):
                label = tk.Label(self.root, text=str(element), borderwidth=1, relief="solid", width=2*len(heading[j]), height=2)
                label.grid(row=i+1, column=j+1)

    def on_ok_button(self):
        self.selected_row = self.selected_row_var.get()

        custom_input_dialog1 = CustomInputDialog(self.root, "Estimated duration in minutes:")
        custom_input_dialog1.show_dialog()

        custom_input_dialog2 = CustomInputDialog(self.root, "Start Location:")
        custom_input_dialog2.show_dialog()

        custom_input_dialog3 = CustomInputDialog(self.root, "End location:")
        custom_input_dialog3.show_dialog()

        self.result = [custom_input_dialog1.result, custom_input_dialog2.result, custom_input_dialog3.result]

        self.root.destroy()

if __name__ == "__main__":

    so_file = "/home/jatin/Codes/MoveinSync/my_functions.so"
    my_functions = CDLL(so_file)
    file1 = open("drivers.txt", "r+")

    driver_data = file1.read().split('\n')

    for i in range(len(driver_data)):
        driver_data[i] = driver_data[i].split(',')

    file1.close()

    root = tk.Tk()
    app = ArrayDisplayApp(root, driver_data)
    app.create_window()

    root.mainloop()

    print("Entered Duration:", app.result)

    # print(driver_data[app.selected_row-1])
    # print(app.result)
    details = [driver_data[app.selected_row-1][0], driver_data[app.selected_row-1][1], driver_data[app.selected_row-1][2], app.result[0], app.result[1], app.result[2]]

    message = ",".join(details)

    message = str(details)
    msg = message.encode('utf-8')

    my_functions.server(msg)

    while(True):
        
        root2 = tk.Tk()
        app2 = StringInputApp(root2)
        root2.mainloop()

        if app2.mess is not None:
            msg = app2.mess.encode('utf-8')
            my_functions.server(msg)

            if(app2.mess == "Ride Completed"):
                break
        

