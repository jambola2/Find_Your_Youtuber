from Tkinter import *

import webbrowser


class Main_Frame:
        def __init__(self, master):
            frame = Frame(master)
            frame.pack()

            self.playButton = Button(
            frame, text="PLAY", height=5, width=30, fg="white", bg="#003333",
            command=self.PlayLevel)

            self.welcomeLabel = Label(
            frame, font=5, text="FindYourYoutuber V0.1.2-Logo goes here")

            def gotoLicense():
                webbrowser.open(
        "https://github.com/austinprog/Find_Your_Youtuber/blob/master/LICENSE")

            self.licenseButton = Button(
            frame, text="License", height=5, width=30, fg="white", bg="orange",
            command=gotoLicense)

            self.creditsLabel = Label(
            frame, font=5, text="Originally produced by Austin & Vectrex")

            def Bugreport():
                webbrowser.open(
                "https://github.com/austinprog/Find_Your_Youtuber/issues")

            self.reportBug = Button(
            frame, text="Report a Bug", height=2, width=10, fg="black",
            bg="white", command=Bugreport)
             # Geometry Layout Manager
            self.welcomeLabel.grid(row=0, column=1)
            self.playButton.grid(row=1, column=1, padx=(0, 300), pady=(100, 0))
            self.licenseButton.grid(row=3, column=1, padx=(0, 300))
            self.creditsLabel.grid(row=3, column=1, padx=(0, 200), pady=(360,
             0))
            self.reportBug.grid(row=3, column=2, padx=(0, 0), pady=(360, 0))

        def PlayLevel(self):
            top = Toplevel()
            top.geometry('500x500')
            top.title("Find Your Youtuber Quiz")
            quizHeader = Label(top, font=10, text="Find Your Youtuber Quiz!")
            quizInfo = Label(top, font=10, text="""To play, you will be given
            a question, and a yes or no button box, press the yes button if
            you agree with the question, and press the no button if you
            disagree. Afterwards we will crunch up your score and tell you
            which youtuber you should watch.""")

            # This is the Geometry layout for PlayLevel
            quizHeader.grid(row=0, column=1)
            quizInfo.grid(row=1, column=1)

if __name__ == "__main__":
    root = Tk()
    app = Main_Frame(root)
    root.title("FindYourYoutuber V0.1.2-Non-Production")
    root.geometry('630x620')  # Sets the size of the program
    root.maxsize(630, 620)  # maximum size for program
    root.mainloop()  # Essentially Starts the program
    root.bg = "redd"