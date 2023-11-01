#Importing Necessary modules
from tkinter import *
import random
import sys

#Properties of root window
root=Tk()
root.title("Typquik")
root.geometry("920x500")
root.config(bg="light blue")
root.resizable(0,0)

#List of all words

wordList=["apple","exhibit","mobile","somewhere","laptop","offense","included","mechanic","reasonable","friend","house",
          "particular","english","faster","original","conversion","signature","positive","management","accept","level",
          "authentication","authorise","annihilate","excavator","letter","inform","office","catastrophe","strawberry",
          "retirement","television","personality","subtraction","division","understanding","vowel","rat","certificate",
          "butterfly","complex","abomination","world","demand","alternative","celebrate","clean","heart","ruthless","cat"]

random.shuffle(wordList)
#------------------Back End of theProgram----------------------------------

#----------------------Start Page Functions--------------------------------
def labelSlide():
    '''We are giving global here for these variables 
    so that their values can be changed inside the function'''
    
    global typquik_count,labelSlider
    typquik="TYPQUIK"
    if typquik_count>=len(typquik):
        typquik_count=0
        labelSlider=""
    labelSlider=labelSlider+typquik[typquik_count]
    typquik_count+=1
    typquik_label.configure(text=labelSlider)
    typquik_label.after(300,labelSlide)

#---------------------Game Page Functions---------------------------------
def start_click():
    start_page_frame.pack_forget()
    game_page_frame.pack()
    type_word_label.config(text=wordList[0])
    time_counter()
    root.bind('<Return>',on_enter)

def on_enter(event):
    try:
        global score,list_counter
        text_entered=text_field.get()
        actual_text=type_word_label.cget("text")
        text_field.delete(0,END)

        if text_entered==actual_text:
            score+=1
        else:
            score-=1

        list_counter+=1
        type_word_label.config(text=wordList[list_counter])
        score_label.config(text="Score: "+str(score))

    except IndexError:
        global time_left
        time_left=0
        time_counter()

def time_counter():
    global time_left
    if time_left>0:
        time_left-=1
        time_left_label.config(text="Time Left : "+str(time_left))
        time_left_label.after(1000,time_counter)

    else:
        game_page_frame.pack_forget()
        end_page_frame.pack()
        root.unbind('<Return>')
        final_score_label.config(text="Final Score : "+str(score))

#----------------------------Game end Page Functions--------------------------------

def restart():
    global score,time_left,list_counter
    end_page_frame.pack_forget()
    start_page_frame.pack()
    text_field.delete(0,END)
    score=0
    time_left=60
    list_counter=0
    random.shuffle(wordList)

#------------------------------Front End of the Program---------------------------------

#---------------------------------Start Page---------------------------------------
text="Rules: Time starts when you click on 'Start'. \n\nType as many words shown possible in 60 seconds and press enter "
text2="+1 Score for entering correct word , -1 Score for entering the wrong word"

start_page_frame=Frame(root,bg="light blue")
typquik_label=Label(start_page_frame,text="A",font=("courier new",40,"bold"),bg="light blue",fg="red")
rule_label_1=Label(start_page_frame,text=text,font=("helvetica",18,"bold"),bg="light blue")
rule_label_2=Label(start_page_frame,text=text2,font=("helvetica",18,"bold"),bg="light blue")
start_button=Button(start_page_frame,text="Start",font=("helvetica",15,"bold"),fg="green",bg="maroon",activebackground="orange",command=start_click)

typquik_label.pack()
rule_label_1.pack(pady=20)
rule_label_2.pack(pady=10)
start_button.pack(pady=50)
start_page_frame.pack()

typquik_count=0
labelSlider=""
labelSlide()

#--------------------------------------Game Page---------------------------------------

instruction="Type the word on the screen as fast as you can and hit Enter"
score=0
time_left=60
list_counter=0

game_page_frame=Frame(root,bg="light blue")
instruction_label=Label(game_page_frame,text=instruction,font=("helvetica",18,"bold"),bg="light blue")
score_label=Label(game_page_frame,text="Score :  "+str(score),font=("helvetica", 17 , "bold"), bg="light blue", fg="red")
time_left_label=Label(game_page_frame,text="Time Left :  "+str(time_left),font=("helvetica", 17 , "bold"), bg="light blue", fg="red")
type_word_label=Label(game_page_frame,text="",font=("courier new",30),bg="light blue")
text_field=Entry(game_page_frame,borderwidth=5,width=20,font=("helvetica", 20),justify="center")
text_field.focus_set()

instruction_label.grid(row=0,column=0,pady=40,columnspan=4,padx=20)
score_label.grid(row=1,column=0,pady=30)
time_left_label.grid(row=1,column=3)
type_word_label.grid(row=2,column=2,pady=20)
text_field.grid(row=3,column=2,pady=10)

#-----------------------------------End Page--------------------------------------

end_page_frame=Frame(root,bg="light blue")
time_up_label=Label(end_page_frame,text="Game Over !",bg="light blue",fg="red",font=("Helvetica",30))
game_over_label=Label(end_page_frame,text="Game Over !",bg="light blue",fg="red",font=("Helvetica",30))
final_score_label=Label(end_page_frame,text="",bg="light blue",fg="red",font=("Helvetica",30))
play_again_button=Button(end_page_frame,text="Play Again",font=("helvetica",15,"bold"),fg="green",bg="maroon",activebackground="orange",command=restart)
exit_button=Button(end_page_frame,text="Exit",font=("helvetica",15,"bold"),fg="green",bg="maroon",activebackground="orange",command=sys.exit)

time_up_label.pack(pady=35)
final_score_label.pack(pady=35)
play_again_button.pack(pady=35)
exit_button.pack(pady=35)

root.mainloop()