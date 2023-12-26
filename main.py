

# 1. How to use input and print functions. Also f \n to separate lines. 

print ("\n")
myName = input("Hello! What is your first name? Na min bang a tai le? \nAnswer: ")


print ("\nIt is good to meet you, " + myName +  ("    🙏🏼 🙏🏼")) # It is invalid to type full stop (.) after myName

print ("\nFun fact. The name of letters or alphabets (including spaces) in your name is: \n")

# 2. How to combine  len function and input function

print (len (myName))


# 3. How to use Python keyword def and call its function name that you have given
   

x =int(input ("\n\nEnter your birth year: "))


# 4. Dot Notation with >>>import time >>> Time = time.time() >>> x = time.ctime() >>> print (" " + x)

import time
Time = time.time()
thaliazou = time.ctime()
print("\nBy the way, 'datestamp' for today is : " + thaliazou + "\n")


y =int (input ("\nEnter current year: "))
       
print ("Your age is:" , y-x)
print ("Your year of eligibity for voting in India:", x+ 18)
print ("Your year of retirement from Govt. service:", x+ 60)
print ("Next year, your age will be: ", str(int(y-x) + 1) + "\nHappy Birthday in advance! Here is a 🌹 bouquet for you!" )



# 5. How to use Boolean function x=input(‘’)/ if x== ‘’:/ print (‘’)/ else: /print (‘’)

print ("\n")
print ("Now let us start a Quiz on the Human Body.")

print ("\n")

# 6. This function >> Score=0 is used in combination with the formula >>> Score +==1 and >>> print ("Score:", Score)

Score = 0      

bodyQuiz1 = input ("Question 1: How many times does the human heart beats 🫀 in a minute?" + "\na. 70 times per minute" + "\nb. 72 times per minute" + "\nc. 75 times per minute" + "\nd. 77 times per minute \n\nAnswer: ")
                 
if bodyQuiz1 == "B" or bodyQuiz1 == "b" or bodyQuiz1 == "72" or bodyQuiz1 == "72 times per minute" or bodyQuiz1 == "b. 72 times per minute" or bodyQuiz1 == "B. 72 times per minute":
        Score+=1     # >>> score+=1 can also be alternatively coded as: >>> score = score + 1. "Score" upper case or "score" lower case are correct as long as it is used consistently. 
        print ("\nCongragulations! You are on fire, " + myName + "!"+ " 👍")
        print ("Score:", Score)
else:
        print ("\nSorry, you are wrong.")

bodyQuiz2= input ("\n\nQuestion 2: The human skull is made up of 20 bones. \na. True \nb. False \n\nAnswer: ")
if bodyQuiz2 == bodyQuiz2 == "b" or "False" or bodyQuiz2 == "false" or bodyQuiz2 == "b. False" or bodyQuiz2 == "b. false" or bodyQuiz2 == "B. false":
        Score+=1
        print ("You are right.  👍\nThis is a false statement because the human skull is made up of 22 bones")
        print ("Score:", Score)
else:   
        print ("\nSorry. Try to do better next time.")  

bodyQuiz3= input ("\n\nQuestion 3: The human spine or backbone is made up of 33 small bones called vertibrae.  \na. True \nb. False \n\nAnswer: ")
if bodyQuiz3 == "a" or bodyQuiz3 == "True" or bodyQuiz3 == "true" or bodyQuiz3 == "a. True" or bodyQuiz3 == "a. true" or bodyQuiz3 == "A. true" :
        Score+=1
        print ("\nCongragulations! You are right.  👍\nWe have 22 skull bones and 33 vertibrae. The pattern is beautiful 22 and 33. ")
        print ("Score:", Score)
else:
        print ("\nSorry. Try to do better next time.")

bodyQuiz4= input ("\n\nQuestion 4: Fill in the blank. \n\nThe main parts of the brain are the cerebrum,_________, 🧠 and the medulla.\n\nAnswer: ")
if bodyQuiz4 == "cerebellum":
        Score+=1
        print ("\nCongragulations!   👍")
        print ("Score:", Score)
else:
        print ("\nIncorrect. The anwser is \ncerebellum.")
        

        
bodyQuiz5= input ("\n\nQuestion 5: Cardiac muscles of the heart 🫀 and lungs 🫁 are called_________ (voluntary/ involuntary) musscles as they cannot be controlled by us. \n\nAnswer: ")
if bodyQuiz5 == "involuntary":
        Score+=1
        print ("\nCongragulations! 👍   You are right. Kalai sai! ")
        print ("Score:", Score)
else:
        print ("\nSorry. Tutung dih lo na ve le. \nThe anwser is involuntary.")

print ("\n")

bodyQuiz6 = input ("Question 6: In the circulatory system, ________ connect the arteries with the veins of the human body. \na. bloods \nb. capillaries \nc. fluids \nd. nerves \n\nAnswer: ")

if bodyQuiz6 == "b" or bodyQuiz6 == "capillaries" or bodyQuiz6 == "b. capillaries":
        Score+=1           
        print ("Correct   👍")
        print ("Score:", Score)
        print ("\n")
else:
        print ("Incorrect! The answer is capillaries")
        print ("Score:", Score)
        print ("\n")
        

bodyQuiz7 = input ("Question 7: The medulla oblongata is  ___________: \na. the spinal cord.  \nb. windpipe \nc. brainstem \nd. rib cage \n\nAnswer: ")

if bodyQuiz7 == "c" or bodyQuiz7 == "C" or bodyQuiz7 == "brainstem" or bodyQuiz7 == "c. brainstem" or bodyQuiz7 == "C. brainstem":
        Score+=1
        print ("Correct   👍")
        print ("Score:", Score)
        print ("\n")
else:
        print ("Incorrect! The answer is brainstem")
        print ("Score:", Score)
        print ("\n")

bodyQuiz8 = input ("Question 8: Strong fibres called TENDONS attached our muscles to bones, and the actions of the muscles 💪 are controlled by ____________. \na. cerebellum \nb. cerebra \nc. frontal lobe \nd. occipital lobe \n\nAnswer: ")

if bodyQuiz8 == "a" or bodyQuiz8 == "A" or bodyQuiz8 == "cerebellum" or bodyQuiz8 == "a. cerebellum" or bodyQuiz8 == "A. cerebellum":
        Score+=1
        print ("Correct   👍")
        print ("Score:", Score)
        print ("\n")
else:
        print ("Incorrect! The answer is cerebellum")
        print ("Score:", Score)
        print ("\n")

bodyQuiz9 = input ("Question 9: In the human digestive system, digested food turns into a paste that travels to the walls of the _________intestines, where our blood absorbs the nutrients. \na. specialized \nb. stomach \nc. large \nd. small \n\nAnswer: ")

if bodyQuiz9 == "d" or bodyQuiz9 == "small" or bodyQuiz9 == "d. small":
        Score+=1
        print ("Correct   👍")
        print ("Score:", Score)
        print ("\n")
else:
        print ("Incorrect! The answer is 'small intestines' ")
        print ("Score:", Score)
        print ("\n")

bodyQuiz10 = input ("Question 10: Final question. Undigested food in the human body travels to the ____________ intestines, from where it is thrown out of the body as faeces or poop. \na. small \nb. tiny \nc. large \nd. very small \n\nAnswer: ")

if bodyQuiz10 == "c" or bodyQuiz10 == "large" or bodyQuiz10 == "c. large":
        Score+=1
        print ("Correct   👍")
        print ("Score:", Score)
        print ("\n")
else:
        print ("Incorrect! The answer is 'large intestines' ")
        print ("Score:", Score)
        print ("\n")

# 7. How to use boolean >> elif >= and elif <= and float together >>> x = float (input (" ")) 


if Score == 10:
    print ("Congratulations! You got a perfect score. 10/10   👍👍👏 🌷")
elif Score >= 7 and Score <=9 :
    print ("Your score is: Excellent!   👍👍")
elif Score >= 5 and Score <=7:
    print ("Your score is: Good   👍")
elif Score >= 3 and Score <=4:
    print ("Your score is: Average")
else:
    print ("Your score is: Bad  ☹️")

print ("\n")
                
   
yourRating = input ("Do you enjoy this conversation?  \nType 'Yes' if you do.\n\nAnswer: ")

if yourRating == "Yes" or yourRating == "yes": 
    
        print ("\nWe shall continue this game soon. \nBye bye for now. \nMangpha!  💛 ✋🏽")
    
else:
        print ("\nSorry to hear that. Dahuai na e!\nI promise to make it more entertaining next time. ✋🏽 ")



print ("\n")
print ("I\'ll treat you with a magic show of Stars. Be prepared!")

        
print ("\n")
print ("[ © 2022 DAVID VUMLALLIAN ZOU & THALIA MANNEIHOI ZOU (§§§   8 May 2022   §§§)\nEducational quiz developed on Python 3. Difficulty level = class V ]")

time.sleep (7)

import turtle

turtle.bgcolor ("black")
naunu= turtle.Turtle ()

naunu.penup ()
naunu.setposition (8,250)
naunu.pendown ()
naunu.color ("white")

naunu.write ("Thangvan Zilsol Ahsi nelkai. \nCreated by Thalia & David. 🌷 🌸", font=("Times",16), align="center")
naunu.goto (0, 10)
naunu.hideturtle ()

naunu.begin_fill ()
for i in range (7):
    
    naunu.forward (200)
    naunu.left (135)
    naunu.color ("yellow")
naunu.end_fill ()
turtle.done ()

    



