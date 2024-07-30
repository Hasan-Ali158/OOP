import tkinter as tk

class App(tk.Tk):
    def __init__(self, wtitle):
        super().__init__()

        self.title(wtitle)

        self.frm = tk.Frame(self)
        self.frm.pack()

        first_label = tk.Label(self.frm, text="Just an output")
        first_label.grid(row=0, column=0, padx=60, pady=30)
        
        self.entrybox = tk.Entry(self.frm)
        self.entrybox.grid(row= 0, column=1, padx=60, pady=30)

        # Create the application variable.
        self.contents = tk.StringVar()
        # Set it to some value.
        self.contents.set("~a StringVar~")

        # Tell the entry widget to watch this variable.
        self.entrybox["textvariable"] = self.contents

        self.entrybox2 = tk.Entry(self.frm)
        self.entrybox2.grid(row= 1, column=1, padx=60, pady=30)

        # Create the application variable.
        self.contents2 = tk.StringVar()
        # Set it to some value.
        self.contents2.set("~a StringVar2~")

        # Tell the entry widget to watch this variable.
        self.entrybox2["textvariable"] = self.contents2

        # Define a button to do some action.
        self.buttonX = tk.Button(self.frm, text="Do this")
        self.buttonX.grid(row= 3, column=1, padx=60, pady=30)

        # Define a callback for when the user hits return.
        # It prints the current value of the variable.
        self.entrybox.bind('<Key-Return>',
                             self.print_contents)
        
        # Define callbacks for when the user enter or leave mouse in the entry.
        self.entrybox.bind("<Enter>", self.turn_red)
        self.entrybox.bind("<Leave>", self.turn_blue)
        self.entrybox.bind("<Button-1>", self.sayDone)

        # Define action of the button.
        self.buttonX.bind('<Button-1>',
                             self.turn_red)
    
    def turn_red(self, event):
        event.widget["foreground"] = "red"        
    def turn_blue(self, event):
        event.widget["foreground"] = "blue"        
    def sayDone(self, event):
        self.contents.set("Done")        
        
    def print_contents(self, event):
        print("Hi. The current entry content is:",
              self.contents.get(), self.entrybox.get(), event.widget.get())
def main():
    App("My Do-Nothing Application").mainloop()
    
main()
