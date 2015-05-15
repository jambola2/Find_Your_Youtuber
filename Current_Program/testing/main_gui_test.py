from Tkinter import *


class Main_Frame:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        self.playButton = Button(
        frame, text="PLAY", height=5, width=10, fg="red")

        self.helpButton = Button(
        frame, text="HELP", height=5, width=10, fg="red")

        self.licenseButton = Button(
        frame, text="License", height=5, width=10, fg="red")

        self.welcomeLabel = Label(
            frame, font=5, text="FindYourYoutuber V0.1.2-Logo goes here")

        self.creditsLabel = Label(
            frame, font=5, text="Originally produced by Austin & Vectrex")

        # Geometry Layout Manager
        self.welcomeLabel.grid(row=0, column=1)
        self.playButton.grid(row=1, column=1, padx=(0, 300), pady=(100, 0))
        self.helpButton.grid(row=2, column=1, padx=(0, 300))
        self.licenseButton.grid(row=3, column=1, padx=(0, 300))
        self.creditsLabel.grid(row=4, column=1, padx=(0, 200), pady=(180, 0))

root = Tk()

app = Main_Frame(root)
root.title("FindYourYoutuber V0.1.2-Non-Production")
root.geometry('600x600')  # Sets the size of the program
root.maxsize(600, 600)  #maximum size for program
root.mainloop()  # Essentially Starts the program
