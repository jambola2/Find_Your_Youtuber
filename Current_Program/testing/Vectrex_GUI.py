from Tkinter import *

import webbrowser

class Main_Frame:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        self.playButton = Button(
        frame, text="PLAY", height=5, width=10, fg="white", bg="green")

        self.helpButton = Button(
        frame, text="HELP", height=5, width=10, fg="white", bg="green")

        self.licenseButton = Button(
        frame, text="License", height=5, width=10, fg="white", bg="green")

        self.welcomeLabel = Label(
        frame, font=5, text="FindYourYoutuber V0.1.2-Logo goes here")

        self.creditsLabel = Label(
        frame, font=5, text="Originally produced by Austin & Vectrex")

        def report():
            webbrowser.open("https://github.com/austinprog/Find_Your_Youtuber/issues")

        self.reportBug = Button(
            frame, text="Report a Bug", height=2, width=10, fg="black", bg="white", command=report)

        # Geometry Layout Manager
        self.welcomeLabel.grid(row=0, column=1)
        self.playButton.grid(row=1, column=1, padx=(0, 300), pady=(100, 0))
        self.helpButton.grid(row=2, column=1, padx=(0, 300))
        self.licenseButton.grid(row=3, column=1, padx=(0, 300))
        self.creditsLabel.grid(row=4, column=1, padx=(0, 200), pady=(180, 0))
        self.reportBug.grid(row=4, column=2, padx=(0, 0), pady=(180, 0))

root = Tk()

app = Main_Frame(root)
root.title("FindYourYoutuber V0.1.2-Non-Production")
root.geometry('630x620')  # Sets the size of the program
root.maxsize(630, 620)  #maximum size for program
root.mainloop()  # Essentially Starts the program

