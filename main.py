# Originally created by Austin G	

# Created under the MIT License

# Description
# This will use the users information that is given to try and find the best youtuber for them to watch.

#The MIT License (MIT)

# Copyright (c) <2015> <Austin Gomez | FunkyHusky Open Source Group>

#Permission is hereby granted, free of charge, to any person obtaining a copy#
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in
#all copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.

import webbrowser
import time
print "Welcome to what Youtuber should I watch? Version NON-GUI 0.0.1 Stable "

#These are the variables that will be key to compiling users score

def Main():
    # Gets the key steps for the algorithm, then compiles them in a algorithm to get the result.
    getGenre = raw_input("What genre do you prefer from the following: comedy, gaming").lower()
    if getGenre == "comedy":
	FindComedy()
    if getGenre == "gaming":
	FindGamers()

# These are the def files each will be used to find the persons favorite youtuber
def FindComedy():
     HigaScore = -10 #Initial Value for the Youtuber Nigahiga
     CHumor = 20 # Initial Value for Youtuber College Humor
     FBros = -30 # Initial Value for Youtuber Fung Bro Comedy
     BzzScore = 40
     Higaoput = "Nigahiga"
     CHumoroput = "College Humor"
     Fbrosoput = "Fung Brothers"
     Buzzoput = "BuzzFeed"

     # HigaQues is short for Nigahiga, and these will be associated with his questions
     HigaQues1 = raw_input("Would you watch a Youtuber who makes skits, and makes sometimes pointless spoofs| Please type Yes or No | ").lower()
     HigaQues2 = raw_input("Would you watch a channel that has videos titled such as How to sing like your favorite artists |Please type Yes or No | ").lower()
     HigaQues3 = raw_input("Would you watch a channel that makes a video such as Unpopular Opinion: Cyber Bullying | Please type Yes or No  ").lower()
     HigaQues4 = raw_input("Would you watch a channel that makes videos such as Ninja Feeds The Homeless |  Please type Yes or No" ).lower()
     HigaQues5 = raw_input("Woyld you watch a channel that makes videos such as Proving the Illuminati is real | Please type Yes or No ").lower()
     HigaAlgo = (HigaQues1, HigaQues2,HigaQues3, HigaQues4, HigaQues5) #Gets the results from the HigaQues

     # CHumor is short for College Humor, and these will be associated with that channels questions
     CHumorQues1 = raw_input("Do you find this video title interesting? The Six Coworkers You'll have at your job | Yes or No").lower()
     CHumorQues2 = raw_input("Would you watch a channel that was originally created for a college audience | Yes or No?").lower()
     CHumorQues3 = raw_input("Do you find this video title interestng? How to Tell If You're a Basic Bro | Yes or No?").lower()
     CHumorQues4 = raw_input("Do you find this video title interesting? If Your Girlfriend Was Actually Crazy | Yes or No?").lower()
     CHumorQues5 = raw_input("Do you find this video title interesting? Why Tipping Should Be Banned- Adam Ruins Everything | Yes or No?").lower()
     CHumorAlgo = (CHumorQues1, CHumorQues2,CHumorQues3,CHumorQues4,CHumorQues5)
     #FBros is short for Fung Bros Comedy, and this wll be associated with that channels questions

     FBrosQues1 = raw_input("Would you watch a youtube channel that is aimed at Asian-American  comedy? | Yes or No").lower()
     FBrosQues2 = raw_input("Would you watch a youtube video titled this? Things Asian Parents Do | Yes or No").lower()
     FBrosQues3 = raw_input("Would you watch a youtube video titled The next great instant noodle").lower()
     FBrosQues4 = raw_input("Would you watch a youtube video titled  Guys you meet at the club").lower()
     FBrosQues5 = raw_input("Would you watch a youtube video titled Roomate Problems! | Yes or No").lower()
     FBAlgo = (FBrosQues1,FBrosQues2,FBrosQues3,FBrosQues4,FBrosQues5)
    #BzzFeed is short for BuzzFeed, and this will be associated with that channels questions

     BzzFeedQues1 = raw_input("Would you watch a youtube video titled this? Professional Baker Reviews Cheap Doughnuts | Yes or No").lower()
     BzzFeedQues2 = raw_input("Would you watch a youtube video titled this? Things Dogs Do That'd Be Creepy If You Did Them | Yes or No").lower()
     BzzFeedQues3 = raw_input("Would you watch a youtube video titled this? Old Boyfriend Vs. New Boyfriend| Yes or No ").lower()
     BzzFeedQues4 = raw_input("Would you watch a youtube video titled this? When you Accidentally Like An Instagram Pic | Yes or No ").lower()
     BzzFeedQues5 = raw_input("Would you watch a youtube video titled this? Historically Accurate Disney princesses | Yes or No").lower()
     BzzAlgo = (BzzFeedQues1,BzzFeedQues2,BzzFeedQues3,BzzFeedQues4,BzzFeedQues5)
     calcscore(HigaAlgo,CHumorAlgo,FBAlgo,BzzAlgo,HigaScore,CHumor,FBros,BzzScore,Higaoput,CHumoroput,Fbrosoput,Buzzoput)

def FindGamers():
   # These are the scores for the Gamer module
   PewdScore = -2
   StampyScore = -1
   VanossScore = -3
   TobyScore = -4
   PewdOutput = "Pewdiepie"
   StampyOutput = "Stampylonghead"
   VanossOutput = "Vanoss Gaming"
   TobyOutput = "Toby Gaming"

   #Pewdiepie Questions

   PewdQues1 = raw_input("Would you watch a youtube video such as MUSCLES THE HEDGEHOG Yes or No ").lower()
   PewdQues2 = raw_input("Would you be ok with a youtuber who cusses a lot? Yes or No ").lower()
   PewdQues3 = raw_input("Would you watch a youtube video such THE SIMPSONS IN REAL LIFE? Yes or No ").lower()
   PewdQues4 = raw_input("Would a video titled this ACHOLHOLIC SIMULATOR offend you? Yes or No ").lower()
   PewdQues5 = raw_input("Would you watch a video titled this BADASS SHARK(Stranded Deep Yes or No ").lower()
   PewdAlgo = (PewdQues1,PewdQues2,PewdQues3,PewdQues4,PewdQues5)
   #Stampylonghead Questions
   StampyQues1 = raw_input("Would you watch a youtube channel that is solely based on Minecraft videos? Yes or No ").lower()
   StampyQues2 = raw_input("Would you watch a video on Youtube titled this DIsney Infinity 2.0 Edition-Spider-Man - Part 12 Yes or No ").lower()
   StampyQues3 = raw_input("Would you watch a video on Youtube titled this Terraria Xbox-Beam Sword ").lower()
   StampyQues4 = raw_input("Would you watch a video on Youtube titled this Minecraft Xbox 360 Edition-Incredible Pixel Art Yes or No  ").lower()
   StampyQues5 = raw_input("Would you watch a videon on Youtube titled this The Walking Dead-Episode 1-Part 4 Yes or No ").lower()
   StampyAlgo = (StampyQues1, StampyQues2, StampyQues3, StampyQues4, StampyQues5)
   #Vanoss Questions
   VanossQues1 = raw_input("Would a video title like this entertain you? Gmod: Toy Story 4 - The Toys Escape! Yes or No ").lower()
   VanossQues2 = raw_input("Would a video titled this entertain you? H1Z1 Adventures Yes or No  ").lower()
   VanossQues3 = raw_input("Would a video titled htis entertain you? Dying Noobs Yes or No ").lower()
   VanossQues4 = raw_input("Would a videp titled this entertain you? The Forest-Survival for the idiots Yes or No ").lower()
   VanossQues5 = raw_input("Would you watch a video titled this? GTA 5 Next Gen Funny Moments Yes or No ").lower()
   VanossAlgo = (VanossQues1,VanossQues2,VanossQues3,VanossQues4,VanossQues5)
   #TobyGames Questions
   TobyQues1 = raw_input("Would you a video titled this Longest Happy Wheels Fall Ever! Yes or No").lower()
   TobyQues2 = raw_input("Would you watch a video titled this EPIC BUTT STAB Yes or No").lower()
   TobyQues3 = raw_input("Would you watch a video titled this I AM BREAD Yes or No").lower()
   TobyQues4 = raw_input("Would you watch a video titled this Goat Simulator:DEMON GOAT KING Yes or No").lower()
   TobyQues5 = raw_input("Would you watch a video titled this IMPOSSIBLE QUIZ! Yes or No ").lower()
   TobyAlgo = (TobyQues1,TobyQues2,TobyQues3,TobyQues4,TobyQues5)
   calcscore(PewdAlgo,StampyAlgo,VanossAlgo,TobyAlgo,PewdScore,StampyScore,VanossScore,TobyScore,PewdOutput, StampyOutput, VanossOutput,TobyOutput)

# Takes in the inputs from the questions and uses little algorithm to calculate score
def calcscore(FirstAns,SndAns,ThirdAns,FourthAns,Score1,Score2,Score3,Score4,Output1,Output2,Output3,Output4):


  for ThereScore in FirstAns:
        if ThereScore == "yes":
            Score1 += 5
        if ThereScore == "no":
            Score1 -= 2
  for ThereScore in SndAns:
        if ThereScore == "yes":
            Score2 += 5
        if ThereScore == "no":
            Score2 -= 2
  for ThereScore in ThirdAns:
        if ThereScore == "yes":
            Score3 += 5
        if ThereScore == "no":
            Score3 -= 2
  for TheereScore in FourthAns:
        if ThereScore == "yes":
            Score4 += 5
        if ThereScore ==  "no":
            Score4 -= 5
  bfrscore = (Score1,Score2,Score3,Score4)
  score = sorted(bfrscore)
  DisplayScore(Score1,Score2,Score3,Score4,score,Output1,Output2,Output3,Output4)
# Displays the results to the user, and ends the program
def DisplayScore(UsersScore1,UsersScore2,UsersScore3,UsersScore4,UsrScore,FirstOput,SndOput,ThirdOput,FourthOput):
      print "You're results are in! The follow are the Youtubers we recommend for you!"
      for x in UsrScore:
          if UsersScore1 == x:
             print FirstOput
          if UsersScore2 == x:
             print SndOput
          if UsersScore3 == x:
             print ThirdOput
          if UsersScore4 == x:
              print FourthOput
      conttoend = raw_input("You havbe finish the product, please type 1 to exit")
      if conttoend == 1:
         StopProgram()

#The command the physically stops the program
def StopProgram():
    end


Main()
