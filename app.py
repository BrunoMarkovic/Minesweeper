import tkinter as tk
from tkinter import messagebox
import config
import igra
import emoji
import time
class Minesweeper:

    def __init__(self):

        self.root = tk.Tk()
        self.root.title("Minesweeper")
        self.root.config(relief="raised")
        self.root.geometry(str(config.HEIGHT) + "x" + str(config.WIDTH))
        self.root.config(bg= "black")
        self.root.minsize(770,500)

        self.root.grid_rowconfigure(0, weight=1, minsize=1)
        self.root.grid_rowconfigure(1, weight=20)
        self.root.grid_columnconfigure(0, weight=1)


        self.title = tk.Label(self.root, bg = "darkgrey", padx=5, pady=5, relief="sunken", height=int(self.root.winfo_height() * config.PERCENTAGELABLE))
        self.title.grid(row = 0, column = 0, sticky = tk.E+tk.W+tk.S+tk.N)

        self.title.grid_columnconfigure(0, weight= 1)
        self.title.grid_columnconfigure(1, weight=1)
        self.title.grid_columnconfigure(2, weight=1)

        self.flagsRaised = config.BROJBOMBICA
        self.emojibox = tk.Label(self.title,text=emoji.emojize(":slightly_smiling_face:"), bg = "darkgrey", font=("Arial", 30), padx=5, pady=5, relief="raised", fg="black")
        self.emojibox.grid(row = 0, column = 1, pady = 10)
        self.minesLeftBox = tk.Label(self.title, text=str(self.flagsRaised), font=("Arial", 15), bg="darkgrey", relief="raised",padx=10, pady=10)
        self.minesLeftBox.grid(row = 0, column = 2, sticky = tk.E, padx = 7)
        self.emojibox.bind("<Button-1>", lambda event: self.emoji_clicked())


        self.menubar = tk.Menu(self.root)
        self.difficulty = tk.Menu(self.menubar, tearoff=0)
        self.difficulty.add_command(label="Beginner", command= lambda x = 0: self.difficultyChange(x))
        self.difficulty.add_command(label="Intermediate", command=lambda x=1: self.difficultyChange(x))
        self.difficulty.add_command(label="Expert", command=lambda x=2: self.difficultyChange(x))
        self.menubar.add_cascade(menu=self.difficulty, label="Difficulty")
        self.root.config(menu=self.menubar)

        #self.emojiLabel = tk.Label(self.title, text=emoji.emojize(":slightly_smiling_face:"), bg="pink")
        #elf.emojiLabel.pack(side= tk.LEFT, padx = 10)

 #       self.root.bind("<Configure>", self.resize_label)
        self.numOfRows = config.NOFROWS
        self.numOfCollumns = config.NOFCOLLUMNS
        self.noNeededToWin = self.numOfRows * self.numOfCollumns - config.BROJBOMBICA
        #print(self.noNeededToWin)

        self.root.protocol("WM_DELETE_WINDOW", self.onClosing)


        self.buttons = {}

        self.buttonFrame = tk.Frame(self.root)
        self.buttonFrame.config(relief="raised", padx=3, pady=3)
        self.buttonFrame.grid(row=1, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
        for i in range(self.numOfCollumns):
            self.buttonFrame.columnconfigure(i, weight=1, minsize = 25)

        for i in range(self.numOfRows):
            self.buttonFrame.rowconfigure(i, weight=1, minsize = 25)

        for i in range(self.numOfRows):
            for j in range(self.numOfCollumns):
                btn1 = tk.Label(self.buttonFrame, font=("Arial", 18), bd=1, padx=0, pady=0, bg="darkgrey", relief="raised")
                #btn1 = tk.Button(self.buttonFrame, font=("Arial", 18), bd=0, padx=0, pady=0, width=4, height=2, highlightbackground='darkgrey',highlightthickness=0,activebackground="lightgrey")
                btn1.grid(row=i, column=j, sticky=tk.N+tk.S+tk.E+tk.W)
                self.buttons[f'{i}button{j}'] = btn1
                btn1.bind('<Button-1>', lambda event, x=i, y=j, b=self.buttons[f'{i}button{j}']: self.buttonClicked(x, y, b))
                btn1.bind('<Button-2>', lambda event, x=i, y=j, b=self.buttons[f'{i}button{j}']: self.rightClicked(x, y, b))


        self.game = igra.Igra()
        self.startTime = time.time()

        self.root.mainloop()

    def is_valid_positionMS(self,x, y):
        return 0 <= x < config.NOFROWS and 0 <= y < config.NOFCOLLUMNS
    def emoji_clicked(self):
        self.emojibox.config(relief="sunken")
        self.root.after(100, self.reset_emoji)

    def reset_emoji(self):
        self.emojibox.config(relief="raised")
        self.restart()

    def restart(self):
        #print("restarting the game...")
        self.game = igra.Igra()
        self.startTime = time.time()
        self.noNeededToWin = self.numOfRows * self.numOfCollumns - config.BROJBOMBICA
        self.flagsRaised = config.BROJBOMBICA
        self.minesLeftBox.config(text=str(self.flagsRaised))
        self.emojibox.config(text=emoji.emojize(":slightly_smiling_face:"))
        for btntext in self.buttons:
            btn = self.buttons[btntext]
            btn.config(text = "",  bg="darkgrey", relief="raised", fg = "black", state = "normal")

    def onClosing(self):
        if messagebox.askyesnocancel(title="QUIT", message="Do you really want to quit"):
            self.root.destroy()



    def game_over_message(self):
        #messagebox.showinfo(title="GAME OVER", message="You've lost")
        self.emojibox.config(text="😵")
        for i in range(config.NOFROWS):
            for j in range(config.NOFCOLLUMNS):
                btn = self.buttons[f'{i}button{j}']
                if self.game.matrica[i,j] == -1:
                    btn.config(text="💣", bg="red")
        self.root.after(100, self.ask_Restart)


    def ask_Restart(self):
        result = messagebox.askretrycancel(title="GAME OVER", message="You've lost")
        if result:
            self.restart()
        else:
            for btntext in self.buttons:
                btn = self.buttons[btntext]
                btn.config(state="disabled")



    def you_won(self):
        self.endTime = time.time()
        self.emojibox.config(text="😎")
        messagebox.showinfo(title="CONGRATULATION", message="you have won :) \nYour time was " + str(round(self.endTime - self.startTime, 2)))
        for btntext in self.buttons:
            btn = self.buttons[btntext]
            btn.config(state="disabled")
        self.root.update_idletasks()
    def resize_label(self, event):
        label_height = int(self.root.winfo_height() * config.PERCENTAGELABLE)
        window_width = int(self.root.winfo_width())
        window_height = int(self.root.winfo_height())
        self.title.config(height=label_height)
        for i in range(self.numOfRows):
            for j in range(self.numOfCollumns):
                btn = self.buttons[f'{i}button{j}']
                btn.config(width=int(window_width / config.NOFCOLLUMNS), height=int(window_height * (1-config.PERCENTAGELABLE) / config.NOFROWS))

    def rightClicked(self, x, y, btn):
        #print("Right click on button " + str(x) + " " + str(y))
        if self.game.secondmatrix[x,y] != 0:
            pass
        else:
            if btn["text"] == "":
                btn.config(text="🚩")  # Mark the button as flagged
                self.flagsRaised -= 1
            elif btn["text"] == "🚩":
                btn.config(text="?", bg = "orange")  # Unflag the button
                self.flagsRaised += 1
            elif btn["text"] == "?":
                btn.config(text="", bg = "darkgrey")
            self.minesLeftBox.config(text=str(self.flagsRaised))

    def difficultyChange(self, dificulty):
        if dificulty == 0:
            # BEGGINER
            config.NOFROWS = 9
            config.NOFCOLLUMNS = 9
            config.BROJBOMBICA = 10
            self.root.destroy()
            self.__init__()
        elif dificulty == 1:
            #intermediate
            config.NOFROWS = 16
            config.NOFCOLLUMNS = 16
            config.BROJBOMBICA = 40
            self.root.destroy()
            self.__init__()

        elif dificulty == 2:
            #expert
            config.NOFROWS = 16
            config.NOFCOLLUMNS = 30
            config.BROJBOMBICA = 99
            self.root.destroy()
            self.__init__()
        else:
            tk.messagebox.showerror("KRIVA TEZINA")



    def buttonClicked(self, x, y, btn):
        #print("You pressed button " + str(x) + " " + str(y))
        kojiBrojAkoOtvoreno = self.game.secondmatrix[x,y]
        #print("Value is " + str(kojiBrojAkoOtvoreno))
        if kojiBrojAkoOtvoreno == 0:
            self.game.check_for_mines(x, y)
            secMat = self.game.secondmatrix[x,y]
            if secMat == -1:
                self.game_over_message()
            else:
                if self.game.openFieldsCount == self.noNeededToWin:
                    self.you_won()
                if secMat > 0 and secMat < 8:
                    btn.config(text = f'{secMat}', bg="lightgrey", relief = "sunken", fg="black")
                if secMat == 9:
                    for i in range(config.NOFROWS):
                        for j in range(config.NOFCOLLUMNS):
                            value = self.game.secondmatrix[i,j]
                            if value != 0 and value != 9:
                                self.buttons[f'{i}button{j}'].config(text=f'{value}', bg="lightgrey", relief="sunken", fg="black")
                            elif value == 9:
                                self.buttons[f'{i}button{j}'].config(state="disabled", bg="lightgrey", relief="sunken")
        else:
            #print("vec otvoreno")
            #ode moras provjerit jeli broj na secondMATRIX jednak broju zastavica
            if kojiBrojAkoOtvoreno > 0 and kojiBrojAkoOtvoreno < 9:
                # prebroji sve zastavice u krugu i usporedi s brojen
                directions = [(-1, -1), (-1, 0), (-1, 1),  # Top-left, Top, Top-right
                              (0, -1), (0, 1),  # Left, Right
                              (1, -1), (1, 0), (1, 1)]  # Bottom-left, Bottom, Bottom-right
                counter = 0
                for dx,dy in directions:
                    if self.is_valid_positionMS(x + dx, y + dy) and self.buttons[f'{dx + x}button{dy + y}']["text"] == "🚩":
                        counter += 1
                if counter == kojiBrojAkoOtvoreno:
                    for dx,dy in directions:
                        if self.is_valid_positionMS(x + dx, y + dy) and self.game.secondmatrix[x + dx, y + dy] == 0 and self.buttons[f'{dx + x}button{dy + y}']["text"] != "🚩":
                            self.game.check_for_mines(x+dx,y + dy)
                    for i in range(config.NOFROWS):
                        for j in range(config.NOFCOLLUMNS):
                            value = self.game.secondmatrix[i,j]
                            if value == -1:
                                self.game_over_message()
                            else:
                                if value != 0 and value != 9:
                                    self.buttons[f'{i}button{j}'].config(text = f'{value}', bg="lightgrey",relief="sunken", fg="black")
                                elif value == 9:
                                    self.buttons[f'{i}button{j}'].config(state="disabled", bg="lightgrey", relief="sunken")

        if self.game.openFieldsCount == self.noNeededToWin:
            self.you_won()












Minesweeper()