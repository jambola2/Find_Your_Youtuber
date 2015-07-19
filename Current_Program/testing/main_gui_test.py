import Tkinter as tk
import tkFont
from Tkinter import *
import webbrowser

NigaHiga=0
Smosh=0
JennaMarbles=0
McJuggerNuggets=0 
Pewdiepie=0
x=-1
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
        for F in (Home_Page, QuizTime, PageTwo): # This is essnentially saying, for every item in the group, frame is equal to it, and its container.
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
                           "Would you watch a youtuber who has a survival series of him being kicked out?"
			   "Would you watch a youtuber who whines and complains alot in his videos?",
			    # Below is Pewdiepie questions
			   "Would you watch a youtuber who makes mainly gaming videos?",
			   "Would you watch a youtuber who makes very odd statements?",
			   "Would you watch a youutber who has a video titled? --> VIKING BALLS (Full Sail)",
                           "Would you watch a youtuber who makes videos with his girlfriend periodically?",
			   "Would you watch a youtuber who has a video titled? --> HOW TO BE COOL FOR SUMMER"]
	YesButton = Button(self,text="Yes", command=self.WhenYesButton_Clicked)
	NoButton = Button(self, text="No", command=self.WhenNoButton_Clicked)
	# Below is the Layout, we are using Grid once again.
	QuizHeader.grid(row=0, column=1)
	self.QuestionPrompt.grid(row=1, column=1,  padx=(0, 150), pady=(400, 0))
	YesButton.grid(row=1,column=1, padx=(0,150), pady=(100,0))
	NoButton.grid(row=2,column=1, padx=(0,200), pady=(200,0))

	
    def WhenYesButton_Clicked(self):
	global x
	x += 1
	global NigaHiga
	global Smosh
	global JennaMarbles
	global McJuggerNuggets 
	global Pewdiepie
	if x == 0:
		
		self.QuestionPrompt.config(text=self.ListofQuestions[0])
		NigaHiga += 1 
	if x == 1:
		self.QuestionPrompt.config(text=self.ListofQuestions[1])
		NigaHiga += 1 
		
	if x == 2:
		self.QuestionPrompt.config(text=self.ListofQuestions[2])
		NigaHiga += 1 
	if x == 3:
		self.QuestionPrompt.config(text=self.ListofQuestions[3])
		NigaHiga += 1
	if x ==4:
		self.QuestionPrompt.config(text=self.ListofQuestions[4])
		NigaHiga += 1
        if x ==5: 
		self.QuestionPrompt.config(text=self.ListofQuestions[5])
		Smosh += 1 
	if x == 6:
		self.QuestionPrompt.config(text=self.ListofQuestions[6])
		Smosh += 1 
	if x == 7:
		self.QuestionPrompt.config(text=self.ListofQuestions[7])
		Smosh += 1 
	if x == 8:
		self.QuestionPrompt.config(text=self.ListofQuestions[8])
		Smosh += 1 
	if x == 9:
		self.QuestionPrompt.config(text=self.ListofQuestions[9])
		Smosh += 1 
	if x == 10:
		self.QuestionPrompt.config(text=self.ListofQuestions[10])
		JennaMarbles += 1 
	if x == 11:
		self.QuestionPrompt.config(text=self.ListofQuestions[11])
		JennaMarbles += 1 
	if x == 12:
		self.QuestionPrompt.config(text=self.ListofQuestions[12])
		JennaMarbles += 1 
	if x == 13:
		self.QuestionPrompt.config(text=self.ListofQuestions[13])
		JennaMarbles += 1 
	if x == 14: 
		self.QuestionPrompt.config(text=self.ListofQuestions[14])
		JennaMarbles += 1
	if x == 15:
		self.QuestionPrompt.config(text=self.ListofQuestions[15])
		McJuggerNuggets += 1 
	if x == 16: 
		self.QuestionPrompt.config(text=self.ListofQuestions[16])
		McJuggerNuggets += 1 
	if x == 17:
		self.QuestionPrompt.config(text=self.ListofQuestions[17])
		McJuggerNuggets += 1 
	if x == 18:
		self.QuestionPrompt.config(text=self.ListofQuestions[18])
		McJuggerNuggets += 1 
	if x == 19:
		self.QuestionPrompt.config(text=self.ListofQuestions[19])
		McJuggerNuggets += 1 
	if x == 20:
		self.QuestionPrompt.config(text=self.ListofQuestions[20])
		Pewdiepie += 1
	if x == 21:
		self.QuestionPrompt.config(text=self.ListofQuestions[21])
		Pewdiepie += 1 
	if x == 22:
		self.QuestionPrompt.config(text=self.ListofQuestions[22])
		Pewdiepie += 1 
	if x == 23:
		self.QuestionPrompt.config(text=self.ListofQuestions[23])
		Pewdiepie += 1 
	if x == 24:
		self.QuestionPrompt.config(text=self.ListofQuestions[24])
		Pewdiepie += 1 
    
    def WhenNoButton_Clicked(self):
	global x
	x += 1
	global NigaHiga
	global Smosh
	global JennaMarbles
	global McJuggerNuggets 
	global Pewdiepie
	if x == 0:
		
		self.QuestionPrompt.config(text=self.ListofQuestions[0])
		NigaHiga -= 1 
	if x == 1:
		self.QuestionPrompt.config(text=self.ListofQuestions[1])
		NigaHiga -= 1 
		
	if x == 2:
		self.QuestionPrompt.config(text=self.ListofQuestions[2])
		NigaHiga -= 1 
	if x == 3:
		self.QuestionPrompt.config(text=self.ListofQuestions[3])
		NigaHiga -= 1
	if x ==4:
		self.QuestionPrompt.config(text=self.ListofQuestions[4])
		NigaHiga -= 1
        if x ==5: 
		self.QuestionPrompt.config(text=self.ListofQuestions[5])
		Smosh -= 1 
	if x == 6:
		self.QuestionPrompt.config(text=self.ListofQuestions[6])
		Smosh -= 1 
	if x == 7:
		self.QuestionPrompt.config(text=self.ListofQuestions[7])
		Smosh -= 1 
	if x == 8:
		self.QuestionPrompt.config(text=self.ListofQuestions[8])
		Smosh -= 1 
	if x == 9:
		self.QuestionPrompt.config(text=self.ListofQuestions[9])
		Smosh -= 1 
	if x == 10:
		self.QuestionPrompt.config(text=self.ListofQuestions[10])
		JennaMarbles -= 1 
	if x == 11:
		self.QuestionPrompt.config(text=self.ListofQuestions[11])
		JennaMarbles -= 1 
	if x == 12:
		self.QuestionPrompt.config(text=self.ListofQuestions[12])
		JennaMarbles -= 1 
	if x == 13:
		self.QuestionPrompt.config(text=self.ListofQuestions[13])
		JennaMarbles -= 1 
	if x == 14: 
		self.QuestionPrompt.config(text=self.ListofQuestions[14])
		JennaMarbles -= 1
	if x == 15:
		self.QuestionPrompt.config(text=self.ListofQuestions[15])
		McJuggerNuggets -= 1 
	if x == 16: 
		self.QuestionPrompt.config(text=self.ListofQuestions[16])
		McJuggerNuggets -= 1 
	if x == 17:
		self.QuestionPrompt.config(text=self.ListofQuestions[17])
		McJuggerNuggets -= 1 
	if x == 18:
		self.QuestionPrompt.config(text=self.ListofQuestions[18])
		McJuggerNuggets -= 1 
	if x == 19:
		self.QuestionPrompt.config(text=self.ListofQuestions[19])
		McJuggerNuggets -= 1 
	if x == 20:
		self.QuestionPrompt.config(text=self.ListofQuestions[20])
		Pewdiepie -= 1
	if x == 21:
		self.QuestionPrompt.config(text=self.ListofQuestions[21])
		Pewdiepie -= 1 
	if x == 22:
		self.QuestionPrompt.config(text=self.ListofQuestions[22])
		Pewdiepie -= 1 
	if x == 23:
		self.QuestionPrompt.config(text=self.ListofQuestions[23])
		Pewdiepie -= 1 
	if x == 24:
		self.QuestionPrompt.config(text=self.ListofQuestions[24])
		Pewdiepie -= 1 
								
		
class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="This is page 2", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame(StartPage))
        button.pack()


if __name__ == "__main__":
    app = ManagementofFrames()
    app.geometry('800x800')
    app.title("FindYourYoutuber: The quiz to find which youtuber to watch")
    app.mainloop()

