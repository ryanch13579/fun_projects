from tkinter import *
from test import display_word

root = Tk()
root.geometry('550x410')

#Created Main Frame
main_frame = Frame(root, highlightbackground='black',
                   highlightthickness=2)
main_frame.pack(side= LEFT)
main_frame.pack_propagate(False)
main_frame.configure(width=450, height=410)

#Create Option Frame
options_frame = Frame(root, bg="#c3c3c3")
options_frame.pack(side= LEFT, )
options_frame.pack_propagate(False)
options_frame.configure(width=100, height=410)

def start_word():
    flashcard_frame = Frame(main_frame)
    flashcard_frame.pack(pady=10)

    display_word(flashcard_frame)

#word button
word_btn = Button(options_frame, text='Words', font=('Bold',15), fg='#158aff',
                  bd=0, bg='#c3c3c3', command= start_word)
word_btn.place(x=10, y =50)


#phrase button
phrase_btn = Button(options_frame, text='Phrases', font=('Bold',15), fg='#158aff',
                  bd=0, bg='#c3c3c3')
phrase_btn.place(x=10, y =150)

root.mainloop()