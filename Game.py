# root ----> main window
# new_window ------> easy level
# new_window2 -------> hard level
# entry ----> easy level

from tkinter import *
from tkinter import messagebox
from random import randint

# declaring variables
global number, counter
number = randint(1, 100)
print(number)
counter = 0
sent = "Correct Number Is  "


# creating function for showing messagebox in easy level
def messagebox2(title, text):
    root2 = Tk()
    root2.withdraw()
    messagebox.showinfo(title, text)
    root2.destroy()


# creating function for showing messagebox in easy level
def messagebox1(title, text):
    root1 = Tk()
    root1.withdraw()
    messagebox.showinfo(title, text)
    root1.destroy()


# function to clear input field in hard level
def clear2():
    entry1.delete(0, END)


# function to clear input field in easy level
def clear():
    entry.delete(0, END)


# function for generating new number
def gen():
    global number
    number = randint(1, 100)


# creating function for clue box of hard level
def clue2(b):
    global counter, bh4
    b = int(b)
    if number < b <= number + 15:
        bh3.config(text="Guessed High")
        counter = counter + 1
        bh4.config(text=counter)
        lose2()
    elif number + 15 < b:
        bh3.config(text="Guessed Too High")
        counter = counter + 1
        bh4.config(text=counter)
        lose2()
    elif number > b >= number - 15:
        bh3.config(text="Guessed Low")
        counter = counter + 1
        bh4.config(text=counter)
        lose2()
    elif b < number - 15:
        bh3.config(text="Guessed Too Low")
        counter = counter + 1
        bh4.config(text=counter)
        lose2()

    elif b == number:
        disable2()
        messagebox1("You Won!!!", "Congratulations You Won!! \nYou Guessed The Correct Number.\nThank You For Playing.")


# creating function for clue box of easy level
def clue(a):
    global counter, be4
    a = int(a)
    if number < a <= number + 15:
        be3.config(text="Guessed High")
        counter = counter + 1
        be4.config(text=counter)
        lose()
    elif number + 15 < a:
        be3.config(text="Guessed Too High")
        counter = counter + 1
        be4.config(text=counter)
        lose()
    elif number > a >= number - 15:
        be3.config(text="Guessed Low")
        counter = counter + 1
        be4.config(text=counter)
        lose()
    elif a < number - 15:
        be3.config(text="Guessed Too Low")
        counter = counter + 1
        be4.config(text=counter)
        lose()

    elif a == number:
        disable()
        messagebox1("You Won!!!", "Congratulations You Won!! \nYou Guessed The Correct Number.\nThank You For Playing.")


# creating for checking lose in easy level
def lose2():
    global counter
    if counter == 5:
        clear2()
        entry1.insert(0, sent)
        entry1.insert(19, number)
        disable2()
        messagebox2("Game Over", "You Lose!!!\nYou Ran Out Of Moves.\nCorrect Number Is Displayed In The Box.\nThank "
                                 "You For Playing.")

    # creating for checking lose in easy level


def lose():
    global counter, number
    if counter == 10:
        clear()
        entry.insert(0, sent)
        entry.insert(19, number)
        disable()
        messagebox2("Game Over!!!",
                    "You Lose!!!\nYou Ran Out Of Moves.\nCorrect Number Is Displayed In The Box.\nThank You "
                    "For Playing.")


# creating disable option for easy level
def disable():
    global be2
    be2.config(state=DISABLED)
    entry.config(state=DISABLED)


# creating disable option for hard level
def disable2():
    bh2.config(state=DISABLED)
    entry1.config(state=DISABLED)


# creating option for quit button in easy level
def back():
    global counter
    gen()
    counter = 0
    new_window.destroy()
    home()


# creating option for quit button in easy level
def back2():
    global counter
    gen()
    counter = 0
    new_window2.destroy()
    home()


def home():
    global root
    root = Tk()
    root.title("Sintrosoft's Guess Number Game")
    root.resizable(height=False, width=False)
    canvas = Canvas(height=500, width=500, bg="#CEE5D0")
    canvas.pack()
    l1 = Label(root, text="Choose Difficulty", fg="#1597E5", bg="#CEE5D0", font=('Arial', 40))
    canvas.create_window(250, 100, window=l1)
    b1 = Button(root, text="Easy Level", width="15", height="1", font=('Arial', 15), fg="#1597E5", command=easy)
    canvas.create_window(250, 200, window=b1)
    b2 = Button(root, text="Hard Level", width="15", height="1", font=('Arial', 15), fg="#1597E5", command=hard)
    canvas.create_window(250, 300, window=b2)
    root.mainloop()


# creating functions for easy level
def easy():
    global be, be2, be3, be4, entry, new_window

    new_window = Tk()
    new_window.title("Sintrosoft's Guess Number Game--- Easy Level")
    new_window.resizable(height=False, width=False)
    root.destroy()
    canvas2 = Canvas(new_window, height=500, width=500, bg="#CEE5D0")
    canvas2.pack()

    # creating label
    label = Label(new_window, text="Easy Level", fg="#1597E5", bg="#CEE5D0", font=('Arial', 50))
    canvas2.create_window(250, 50, window=label)
    # creating a label for telling no. of chances
    label2 = Label(new_window, text="No. of chances = 10", fg="#1597E5", bg="#CEE5D0", font=('Arial', 20))
    canvas2.create_window(130, 110, window=label2)
    # creating entry
    entry = Entry(new_window, width="30")
    canvas2.create_window(400, 200, window=entry)
    # button to quit
    be = Button(new_window, text="Quit/New Game", height=2, width=15, command=back, fg="#1597E5")
    canvas2.create_window(50, 490, window=be)
    # creating button to check answer
    be2 = Button(new_window, text="Check Answer", command=lambda: clue(entry.get()), width="15", height="1",
                 font=('Arial', 15), fg="#1597E5")
    canvas2.create_window(400, 250, window=be2)
    # creating a label for clue box
    label3 = Label(new_window, text="Clue Box", fg="#1597E5", bg="#CEE5D0", font=('Arial', 20))
    canvas2.create_window(150, 200, window=label3)
    # creating clue box
    be3 = Button(new_window, text="", width="20")
    canvas2.create_window(150, 250, window=be3)
    # creating label for no. of attempts box
    label4 = Label(new_window, text="No. Of Attempts", fg="#1597E5", bg="#CEE5D0", font=('Arial', 20))
    canvas2.create_window(150, 300, window=label4)
    # creating box for showing no. of attempts used
    be4 = Button(new_window, text="", width="20")
    canvas2.create_window(150, 350, window=be4)


def hard():
    global new_window2, bh2, bh3, bh4, entry1

    new_window2 = Tk()
    new_window2.title("Sintrosoft's Guess Number Game--- Hard Level")
    new_window2.resizable(height=False, width=False)
    root.destroy()
    canvas3 = Canvas(new_window2, height=500, width=500, bg="#CEE5D0")
    canvas3.pack()
    # creating label
    label_h = Label(new_window2, text="Hard Level", fg="#1597E5", bg="#CEE5D0", font=('Arial', 50))
    canvas3.create_window(250, 50, window=label_h)
    # creating a label for telling no. of chances
    label_h2 = Label(new_window2, text="No. of chances = 5", fg="#1597E5", bg="#CEE5D0", font=('Arial', 20))
    canvas3.create_window(130, 110, window=label_h2)
    # creating entry
    entry1 = Entry(new_window2, width="30")
    canvas3.create_window(400, 200, window=entry1)
    # button to quit
    bh = Button(new_window2, text="Quit/New Game", height=2, width=15, command=back2, fg="#1597E5")
    canvas3.create_window(50, 490, window=bh)
    # creating button to check answer
    bh2 = Button(new_window2, text="Check Answer", command=lambda: clue2(entry1.get()), width="15", height="1",
                 font=('Arial', 15), fg="#1597E5")
    canvas3.create_window(400, 250, window=bh2)
    # creating a label for clue box
    label_h3 = Label(new_window2, text="Clue Box", fg="#1597E5", bg="#CEE5D0", font=('Arial', 20))
    canvas3.create_window(150, 200, window=label_h3)
    # creating clue box
    bh3 = Button(new_window2, text="", width="20")
    canvas3.create_window(150, 250, window=bh3)
    # creating label for no. of attempts box
    label_h4 = Label(new_window2, text="No. Of Attempts", fg="#1597E5", bg="#CEE5D0", font=('Arial', 20))
    canvas3.create_window(150, 300, window=label_h4)
    # creating box for showing no. of attempts used
    bh4 = Button(new_window2, text="", width="20")
    canvas3.create_window(150, 350, window=bh4)


home()
