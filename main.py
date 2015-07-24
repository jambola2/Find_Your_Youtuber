import Tkinter as tk
from Tkinter import *
import webbrowser


class Scores(object):
        NigaHiga = 0
        Smosh = 0
        JennaMarbles = 0
        McJuggerNuggets = 0
        Pewdiepie = 0

scores = Scores()
x = -1  # counter variable for later
TITLE_FONT = ("Helvetica", 18, "bold")


class ManagementofFrames(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (Home_Page, QuizTime):
            frame = F(container, self)
            self.frames[F] = frame
            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Home_Page)

    def show_frame(self, c):
        '''Show a frame for the given class'''
        frame = self.frames[c]
        frame.tkraise()


class Home_Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.Welcomelabel = tk.Label(self, text="Welcome to Find Your Youtuber, Please click on the button of your choice to begin", font=50)
        self.Start_Game = Button(self, text="Start Quiz",
             command=lambda: controller.show_frame(QuizTime), width=40)

        self.LicenseButton = Button(self, text="Our License",command=self.GotoLicense)
        self.CreditsLabel = tk.Label(self, text="Licensed under MIT License")
        # Padx will make it move to the left or right
        # Pady will move it move up and down
        # below will set the colors for the program
        self.Start_Game.configure(bg="#666699")
        self.LicenseButton.configure(bg="#666699")
        self.Welcomelabel.grid(row=0, column=1)
        self.Start_Game.grid(row=1, column=1, padx=(0, 100), pady=(100, 0))
        self.LicenseButton.grid(row=2, column=1, padx=(0, 500), pady=(500, 0))
        self.CreditsLabel.grid(row=2, column=1, padx=(300, 0), pady=(500, 0))

    def GotoLicense(self):
        webbrowser.open(
        "https://github.com/austinprog/Find_Your_Youtuber/blob/master/LICENSE")

class QuizTime(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.QuizHeader =tk.Label(self,
        text="Welcome to the Quiz! Please press Yes or No on each question")
        self.QuestionPrompt = tk.Label(self,
            text="Press Yes or No to start the quiz")
        # Below is NigaHiga Questions
        self.ListofQuestions = ["Would you watch a youtuber who seems to be very hyper and random?",
                            "Would you watch a youtuber who makes videos that are titled this --> Are Asian Stereotypes true?",
                            "Would you watch a youtuber who tends to talk very fast which can lead to confusion?",
                            "Would you watch a youtuber who has a talk show game featuring other famous youtubers?",
                            "Would you watch a youtuber who has been around since the beginning of Youtube?",
                            # Below is Smosh Questions
                            "Would you watch a youtuber that has a video titled this --> GODS IN REAL LIFE",
                            "Would you watch a youtuber that has videos that are not approproate for young ages?",
                            "Would you watch a youtuber that has videos that are very satrical",
                            "Would you watch a youtuber that   has  a              video?",
                            "Would you watcha  youtuber that consist of two host?",
                            # Below is JennaMarbles Questions
                            "Would you watch a youtuber who is cool?",
                            "Would you watch a youtuber who has a video titled? --> How to trick people into thinking you're good looking",
                            "Would you watch a youtuber that makes                       fun of guys?",
                            "Would you watch a youtuber who has a video titled? -     -> How Tacos are made?",
                            # Below is Mcjuggernuggets Questions
                            "Would you watch a youtuber whos videos consist of him arguing with his pyschotic dad who destroys his stuff",
                            "Would you watch a youtuber who has a video titled? --> Jessee reacts to Halo Helmet Destruction",
                            "Would you watch a youtuber who fights all the time with his brother?",
                            "Would you watch a youtuber who has a survival series of him being kicked out?",
                            "Would you watch a youtuber who whines and complains alot in his videos?",
                            # Below is Pewdiepie questions
                            "Would you watch a youtuber who makes mainly gaming videos?",
                            "Would you watch a youtuber who makes very odd statements?",
                            "Would you watch a youutber who has a video titled? --> VIKING BALLS (Full Sail)",
                            "Would you watch a youtuber who makes videos with his girlfriend periodically?",
                            "Would you watch a youtuber who has a video titled? --> HOW TO BE COOL FOR SUMMER"]
        self.YesButton = Button(self, text="Yes", height=10, width=30,
            command=self.WhenYesButton_Clicked)
        self.NoButton = Button(self, text="No", height=10, width=30,
             command=self.WhenNoButton_Clicked)
        self.YesButton.configure(bg="#FFCC00")
        self.NoButton.configure(bg="#FFCC00")
        self.Rslt_Notifi = tk.Label(self,
         text="The Quiz will automatically load to the results once finished")
        # Below is the Layout, we are using Grid once again.
        self.QuizHeader.grid(row=0, column=1)
        self.QuestionPrompt.grid(row=1, column=1,pady=(100,0))
        self.YesButton.grid(row=3, column=1, padx=(0, 100), pady=(100, 0))
        self.NoButton.grid(row=4, column=1, padx=(0, 100), pady=(100, 0))
        self.Rslt_Notifi.grid(row=5, column=1, padx=(0, 100), pady=(100, 0))
        #self.GotoResults.grid(row=6,column=1)
        #self.GotoResults.configure(state=DISABLED)

    def WhenYesButton_Clicked(self):
        global x
        x += 1
        if x < 4:
            Scores.NigaHiga += 1
            self.QuestionPrompt.config(text=self.ListofQuestions[x])
        elif x < 10:
            Scores.Smosh += 1
            self.QuestionPrompt.config(text=self.ListofQuestions[x])
        elif x < 15:
            self.QuestionPrompt.config(text=self.ListofQuestions[x])
            Scores.JennaMarbles += 1
        elif x < 20:
            self.QuestionPrompt.config(text=self.ListofQuestions[x])
            Scores.McJuggerNuggets += 1
        elif x <= 23:  # 24 because it starts at 0
            self.QuestionPrompt.config(text=self.ListofQuestions[x])
            Scores.Pewdiepie += 1
        else:
            self.YesButton.grid_forget()
            self.NoButton.grid_forget()
            self.Rslt_Notifi.grid_forget()
            self.QuizHeader.grid_forget()
            self.QuestionPrompt.grid_forget()
            self.WhoWon = tk.Label(self,
            text="We have displayed the results, whoever has the most numerical points is the winner")
            self.HigaAnnounce = tk.Label(self, text="Results for NigaHiga")
            self.HigaResults = tk.Label(self, text=Scores.NigaHiga)
            self.Smosh = tk.Label(self, text="Results for Smosh")
            self.SmoshResults = tk.Label(self, text=Scores.Smosh)
            self.JennaMarbles = tk.Label(self,
                 text="Results for Jenna Marbles")
            self.JennaResults = tk.Label(self, text=Scores.JennaMarbles)
            self.Mcjuggernuggets = tk.Label(self,
                 text="Results for Mcjuggernuggets")
            self.McjuggerResults = tk.Label(self, text=Scores.McJuggerNuggets)
            self.Pewdiepie = tk.Label(self, text="Results for Pewdiepie")
            self.Pewdiescore = tk.Label(self, text=Scores.Pewdiepie)
            self.WhoWon.grid(row=1, column=1)
            self.HigaAnnounce.grid(row=2, column=1)
            self.HigaResults.grid(row=2, column=2)
            self.Smosh.grid(row=3, column=1)
            self.SmoshResults.grid(row=3, column=2)
            self.JennaMarbles.grid(row=4, column=1)
            self.JennaResults.grid(row=4, column=2)
            self.Pewdiepie.grid(row=5, column=1)
            self.Pewdiescore.grid(row=5, column=2)


    def WhenNoButton_Clicked(self):
        global x
        x += 1
        if x < 4:
            Scores.NigaHiga -= 1
            self.QuestionPrompt.config(text=self.ListofQuestions[x])
        elif x < 10:
            Scores.Smosh -= 1
            self.QuestionPrompt.config(text=self.ListofQuestions[x])
        elif x < 15:
            self.QuestionPrompt.config(text=self.ListofQuestions[x])
            Scores.JennaMarbles -= 1
        elif x < 20:
            self.QuestionPrompt.config(text=self.ListofQuestions[x])
            Scores.McJuggerNuggets -= 1
        elif x <= 23:  # 24 because it starts at 0
            self.QuestionPrompt.config(text=self.ListofQuestions[x])
            Scores.Pewdiepie -= 1
        else:
            self.YesButton.grid_forget()
            self.NoButton.grid_forget()
            self.Rslt_Notifi.grid_forget()
            self.QuizHeader.grid_forget()
            self.QuestionPrompt.grid_forget()
            self.WhoWon = tk.Label(self,
            text="We have displayed the results, whoever has the most numerical points is the winner")
            self.HigaAnnounce = tk.Label(self, text="Results for NigaHiga")
            self.HigaResults = tk.Label(self, text=Scores.NigaHiga)
            self.Smosh = tk.Label(self, text="Results for Smosh")
            self.SmoshResults = tk.Label(self, text=Scores.Smosh)
            self.JennaMarbles = tk.Label(self,
                 text="Results for Jenna Marbles")
            self.JennaResults = tk.Label(self, text=Scores.JennaMarbles)
            self.Mcjuggernuggets = tk.Label(self,
                 text="Results for Mcjuggernuggets")
            self.McjuggerResults = tk.Label(self, text=Scores.McJuggerNuggets)
            self.Pewdiepie = tk.Label(self, text="Results for Pewdiepie")
            self.Pewdiescore = tk.Label(self, text=Scores.Pewdiepie)
            self.WhoWon.grid(row=1, column=1)
            self.HigaAnnounce.grid(row=2, column=1)
            self.HigaResults.grid(row=2, column=2)
            self.Smosh.grid(row=3, column=1)
            self.SmoshResults.grid(row=3, column=2)
            self.JennaMarbles.grid(row=4, column=1)
            self.JennaResults.grid(row=4, column=2)
            self.Pewdiepie.grid(row=5, column=1)
            self.Pewdiescore.grid(row=5, column=2)

if __name__ == "__main__":
    app = ManagementofFrames()
    app.geometry('900x760')
    app.title("FindYourYoutuber:V0.0.1-Alpha")
    app.mainloop()
