from tkinter import *
from tkinter.font import Font
from random import randint

def display_word(frame):

    #Read txt file
    with open('flashcards/unit1.txt','r') as file:
        lines = file.readlines()

    words =[line.strip().split(': ') for line in lines]

    #get a count of our word list
    count = len(words)


    def next():
        global hinter, hint_count
        #Clear Screen
        answer_label.config(text="")
        hint_label.config(text="")
        #Reset Hint
        hinter = ""
        hint_count = 0

        my_entry.delete(0, END)
        global random_word
        #Create random selection
        random_word = randint(0, count-1)
        #update label with malay word
        malay_word.config(text=words[random_word][0])

    def answer():
        if my_entry.get() == words[random_word][1]:
            answer_label.config(text=f"Correct! {words[random_word][0]} is {words[random_word][1]}")

        else:
            answer_label.config(text=f"Useless! {words[random_word][0]} is not {my_entry.get()}. It is {words[random_word][1]}")

    #Keep track of hints
    hinter = ""
    hint_count = 0
    def hint():
        global hint_count
        global hinter
        
        if hint_count < len(words[random_word][1]) and hint_count <=2:
            hinter = hinter + words[random_word][1][hint_count]
            hint_label.config(text=hinter)
            hint_count += 1

    malay_word = Label(frame, font=("Helvetica",36), text= "")
    malay_word.pack(pady=30)

    answer_label = Label(frame, text="")
    answer_label.pack(pady=20)

    my_entry = Entry(frame, font=('Helvetica',23))
    my_entry.pack(pady=20)

    #Create Buttons
    button_frame = Frame(frame)
    button_frame.pack(pady=20)

    answer_button = Button(button_frame, text="Answer", command=answer)
    answer_button.grid(row=0, column=0, padx=20)

    next_button = Button(button_frame, text="Next", command=next)
    next_button.grid(row=0, column=1)

    hint_button = Button(button_frame, text="Hint", command= hint)
    hint_button.grid(row=0, column=2, padx=20)

    #Create Hint Label
    hint_label = Label(frame, text="")
    hint_label.pack(padx=20)

    #Run next function when program starts
    next()