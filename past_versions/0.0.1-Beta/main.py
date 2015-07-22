from Tkinter import *

import webbrowser

NigaHigaScore = 0
Smosh = 0
FouseyTube = 0

class Main_Frame:
        def __init__(self, master):
            frame = Frame(master)
            frame.pack()
            # Button for Play, which is the main program

            self.playButton = Button(
            frame, text="PLAY", height=5, width=30, fg="white", bg="#003333",
            command=self.PlayLevel)

            self.welcomeLabel = Label(
            frame, font=50, fg="blue", text="FindYourYoutuber")

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



        def PlayLevel(PlyMec):
                global x
                x = -1
                # This will hold the questions that will be asked.
                ComedyQAbank =["""Would you watch a youtuber who is very satrical?""",

                """Would you watch a youtuber who comedy sometimes makes no sense""",

                """Would you watch a youtuber who has been around
                 since Youtube was created?""",

                 """Would you watch a youtuber who posts
                 atleast once a week?""",

                """Would you watch a youtuber suited
                for adult audiences?""",

                """Would ou watch a youtuber who makes fun
                 of tv shows and songs""",

                """Would you watch a youtuber who
                has a consistent series?""",

                 """Would watch a youtuber who has
                 a video titled Magic Ipad""",

                 """Would you watch a youtuber who likes to do hilarious
                 pranks on their family members, and even celebrities?""",

                 """Would you watch a youtuber who sometimes does
                 funny and serious social experiments?""",

                 """Would you watch a youtuber who can be very annoying?""",

                 """Would you watch a youtuber who does not always post?""",

                 """Your results are now ready! Please press Results"""]




                def YSButtonClicked():
                    global x
                    x += 1
                    global NigaHigaScore
                    global Smosh
                    global Fouseytube

                    #case structure
                    if x == 0:
                        QuestionPrompt.config(text=ComedyQAbank[0])

                        NigaHigaScore += 1
                    if x == 1:
                        QuestionPrompt.config(text=ComedyQAbank[1])

                        NigaHigaScore += 1
                    if x == 2:
                        QuestionPrompt.config(text = ComedyQAbank[2])

                        NigaHigaScore += 1
                    if x == 3:
                        QuestionPrompt.config(text = ComedyQAbank[3])

                        NigaHigaScore += 1
                    if x == 4:
                        QuestionPrompt.config(text = ComedyQAbank[4])

                        Smosh += 1
                    if x == 5:
                        QuestionPrompt.config(text = ComedyQAbank[5])

                        Smosh += 1
                    if x == 6:
                        QuestionPrompt.config(text = ComedyQAbank[6])

                        Smosh += 1
                    if x == 7:
                        QuestionPrompt.config(text = ComedyQAbank[7])

                        Smosh += 1
                    if x == 8:
                        QuestionPrompt.config(text = ComedyQAbank[8])

                        FouseyTube += 1
                    if x == 9:
                        QuestionPrompt.config(text = ComedyQAbank[9])

                        FouseyTube += 1
                    if x == 10:
                        QuestionPrompt.config(text = ComedyQAbank[10])

                        FouseyTube += 1
                    if x == 11:
                        QuestionPrompt.config(text=ComedyQAbank[11])
                        FouseyTube += 1
                    if x == 12:
                        QuestionPrompt.config(text=ComedyQAbank[12])
                        GotoResults.configure(state=NORMAL)

                def NoButtonClicked():
                        global x
                        x += 1
                        global NigaHigaScore
                        global Smosh
                        global Fouseytube

                        #case structure
                        if x == 0:
                            QuestionPrompt.config(text=ComedyQAbank[0])

                            NigaHigaScore -= 1
                        if x == 1:
                            QuestionPrompt.config(text=ComedyQAbank[1])

                            NigaHigaScore -= 1
                        if x == 2:
                            QuestionPrompt.config(text = ComedyQAbank[2])

                            NigaHigaScore -= 1
                        if x == 3:
                            QuestionPrompt.config(text = ComedyQAbank[3])

                            NigaHigaScore -= 1
                        if x == 4:
                            QuestionPrompt.config(text = ComedyQAbank[4])

                            Smosh -= 1
                        if x == 5:
                            QuestionPrompt.config(text = ComedyQAbank[5])

                            Smosh -= 1
                        if x == 6:
                            QuestionPrompt.config(text = ComedyQAbank[6])

                            Smosh -= 1
                        if x == 7:
                            QuestionPrompt.config(text = ComedyQAbank[7])

                            Smosh -= 1
                        if x == 8:
                            QuestionPrompt.config(text = ComedyQAbank[8])

                            FouseyTube -= 1
                        if x == 9:
                            QuestionPrompt.config(text = ComedyQAbank[9])

                            FouseyTube -= 1
                        if x == 10:
                            QuestionPrompt.config(text = ComedyQAbank[10])

                            FouseyTube -= 1
                        if x == 11:
                            QuestionPrompt.config(text=ComedyQAbank[11])
                            FouseyTube -= 1
                        if x == 12:
                            QuestionPrompt.config(text=ComedyQAbank[12])
                            GotoResults.configure(state=NORMAL)



                def Resultslevel():
                    top = Toplevel()
                    top.geometry('630x620')
                    top.maxsize(630,620)
                    top.title("Your results is ")
                    if NigaHigaScore > Smosh and NigaHigaScore > FouseyTube:
                       winner = "Nigahiga is your Youtuber!"
                    elif Smosh > FouseyTube and Smosh > FouseyTube:
                        winner = "Smosh is your youtuber!"
                    elif FouseyTube > NigaHigaScore and FouseyTube > Smosh:
                        winner = "Fouseytube is your youtuber!"

                    TestLabel = Label(top,text=winner)
                    TestLabel.pack()


                top = Toplevel()
                top.geometry('800x700')
                top.maxsize(800, 700)
                top.title("Find Your Youtuber Quiz")
                QuestionPrompt = Label(top, font=10, text="hi")
                YesButton = Button(top,text="yes", command=YSButtonClicked)
                NoButton = Button(top,text="No", command=NoButtonClicked)
                GotoResults = Button(top,text="Go To Results",
                    command=Resultslevel)
                GotoResults.configure(state=DISABLED)


            # This is the Geometry layout for PlayLevel
                QuestionPrompt.grid(row=0, column=1,  padx=(0, 50), pady=(100, 0))
                YesButton.grid(row=1, column=0,  padx=(0, 200), pady=(100, 0))
                NoButton.grid(row=2, column=0,  padx=(0, 200), pady=(100, 0))
                GotoResults.grid(row=3,column=0,  padx=(0, 200), pady=(100, 0))


if __name__ == "__main__":
    root = Tk()
    app = Main_Frame(root)
    root.title("FindYourYoutuber V0.1.3-Non-Production")
    root.geometry('630x620')  # Sets the size of the program
    root.maxsize(630, 620)  # maximum size for program
    root.mainloop()  # Essentially Starts the program
