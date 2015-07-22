import Tkinter as tk
import tkFont
from Tkinter import *
import webbrowser

class Scores(object):

	NigaHiga=0
	Smosh=0
	JennaMarbles=0
	McJuggerNuggets=0
	Pewdiepie=0

Scores = Scores() 
x=-1 #counter variable for later
TITLE_FONT = ("Helvetica", 18, "bold")

# Credits for Tkinter frame architecture switcher to JonrSharpe  http://stackoverflow.com/users/3001761/jonrsharpe
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
        for F in (Home_Page, QuizTime, UsersResults): # This is essnentially saying, for every item in the group, frame is equal to it, and its container.
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
        Welcomelabel = tk.Label(self, text="Welcome to Find Your Youtuber! Please click on the button of your choice to begin", font=50)
	Start_Game = Button(self, text="Start Quiz", command=lambda: controller.show_frame(QuizTime),width=40)
	LicenseButton = Button(self,text="Our License")
        CreditsLabel = tk.Label(self, text="Idea created by Austin Gomez & Vectrex | Distributed under The Unlicense 2015 ")
	# Below is our Grid Layout for Home_Page	
	# Padx will make it move to the left or right
	# Pady will move it move up and down
	Welcomelabel.grid(row=0, column=1)
	Start_Game.grid(row=1, column=1, padx=(0, 100), pady=(100, 0))
	LicenseButton.grid(row=2, column=1, padx=(0, 500), pady=(600,0))
	CreditsLabel.grid(row=2,column=1, padx=(300,0), pady=(600,0))

class QuizTime(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        QuizHeader =tk.Label(self,font=15,text="Welcome to the Quiz! Please press Yes or No on each question")
        self.QuestionPrompt = tk.Label(self, font=10, text="Press Yes or No to start the quiz")

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
			   "Would you watch a youtuber that has a video?",
			   "Would you watcha  youtuber that consist of two host?",
			    # Below is JennaMarbles Questions
			   "Would you watch a youtuber who is female?",
			   "Would you watch a youtuber who has a video titled? --> How to trick people into thinking you're good looking",
			   "Would you watch a youtuber that makes fun of guys?",
			   "Would you watch a youtuber who has a video titled? --> How Girl's Fall Asleep",
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
	self.YesButton = Button(self,text="Yes",height = 10, width = 30, command=self.WhenYesButton_Clicked)
	self.NoButton = Button(self, text="No",height = 10, width = 30, command=self.WhenNoButton_Clicked)
	self.ResultsNotification = tk.Label(self, text="When results are ready, the button will activate and become red")
	self.GotoResults = Button(self, text="Results are ready",command=lambda: controller.show_frame(UsersResults),height = 5, width = 20)
	# Below is the Layout, we are using Grid once again.
	QuizHeader.grid(row=0, column=1)
	self.QuestionPrompt.grid(row=1, column=1)
	self.YesButton.grid(row=3,column=1, padx=(0,100), pady=(100,0))
	self.NoButton.grid(row=4,column=1, padx=(0,100), pady=(100,0))
   	self.ResultsNotification.grid(row=5,column=1, padx=(0,100), pady=(100,0))
   	self.GotoResults.grid(row=6,column=1)
   	self.GotoResults.configure(state=DISABLED)
	
    def WhenYesButton_Clicked(self):
	global x
	x += 1
	
	if x < 4:
		Scores.NigaHiga +=1
		self.QuestionPrompt.config(text=self.ListofQuestions[x])
		
	elif x < 10:
		Scores.Smosh += 1
		self.QuestionPrompt.config(text=self.ListofQuestions[x])
		
	elif x < 15:
		Scores.JennaMarbles += 1 #Trying to always put the score increment first, in case calling the config doesn't increment score
		self.QuestionPrompt.config(text=self.ListofQuestions[x])
		
	elif x < 20:
		Scores.McJuggerNuggets += 1
		self.QuestionPrompt.config(text=self.ListofQuestions[x])
		
	else: 
		Scores.Pewdiepie += 1
		if x == 24:
			self.YesButton.configure(state=DISABLED)
			self.NoButton.configure(state=DISABLED)
			self.GotoResults.configure(state=NORMAL)
		else:
			self.QuestionPrompt.config(text=self.ListofQuestions[x])

    def WhenNoButton_Clicked(object):
	global x
	x += 1
	
	if x < 5:
		Scores.NigaHiga -=1
		self.QuestionPrompt.config(text=self.ListofQuestions[x])
		
	elif x < 10:
		Scores.Smosh -= 1
		self.QuestionPrompt.config(text=self.ListofQuestions[x])
		
	elif x < 15:
		Scores.JennaMarbles -= 1
		self.QuestionPrompt.config(text=self.ListofQuestions[x])
		
	elif x < 20:
		Scores.McJuggerNuggets -= 1
		self.QuestionPrompt.config(text=self.ListofQuestions[x])
	
	else:
		Scores.Pewdiepie -= 1
		if x == 24: #24 is the last question
			self.YesButton.configure(state=DISABLED)
			self.NoButton.configure(state=DISABLED)
			self.GotoResults.configure(state=NORMAL)
			print Scores.Pewdiepie #I assume this is a debugging statement?
		else:
			self.QuestionPrompt.config(text=self.ListofQuestions[x])

class UsersResults(tk.Frame):
	def __init__(self, parent, controller):
    		tk.Frame.__init__(self, parent)
    		test = Button(self, text=x)
    		test.grid(row=1,column=1)
       	

if __name__ == "__main__":
    app = ManagementofFrames()
    app.geometry('800x800')
    app.title("FindYourYoutuber: The quiz to find which youtuber to watch")
    app.mainloop()

