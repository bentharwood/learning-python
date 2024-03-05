import tkinter as tk
import random
import os
from pygame import mixer
from PIL import ImageTk, Image
from tkinter import messagebox
import webbrowser

class App:
  def __init__(self):
    # setting up variables for play
    global username 
    global wins
    global losses
    global ties
    ties = 0
    wins = 0
    losses = 0
    # create window
    self.root = tk.Tk()
    # make window non-resizable
    self.root.resizable(False,False)
    # set window title
    self.root.title("Rock Paper Scissors")
    # initialize mixer from pygame for music
    mixer.init()
    # boolean variable to control if music plays
    self.music_playing = False
    #topbar frame
    self.topbar = tk.Frame(self.root)
    # make top text for game
    self.top_text = tk.Label(self.topbar, text="Rock! Paper! Scissors!", font=("helvetica", 18))
    # place text in window
    self.top_text.pack(side="left",padx=10,pady=10)
    # resize musical-note.png to fit in music_button
    original_music_image = Image.open("assets/musical-note.png")
    resized_music_image = original_music_image.resize((20, 20), Image.Resampling.LANCZOS)
    self.music_icon = ImageTk.PhotoImage(resized_music_image)
    # resizes music.png to fit music_button
    original_no_music_image = Image.open("assets/music.png")
    resized_no_music_image = original_no_music_image.resize((20, 20), Image.Resampling.LANCZOS)
    self.no_music_icon = ImageTk.PhotoImage(resized_no_music_image)
    # makes the button that pauses/unpauses the music then packs it
    self.music_button = tk.Button(self.topbar, image=self.music_icon,width=20,height=20, command=self.music_toggle)
    self.music_button.pack(side="left", padx=5,pady=5)
    # resizes info.png to fit the info button
    original_info_image = Image.open("assets/info.png")
    resized_info = original_info_image.resize((20, 20), Image.Resampling.LANCZOS)
    self.info_icon = ImageTk.PhotoImage(resized_info)
    # makes the about RPS button and how to play then packs it 
    self.about_button = tk.Button(self.topbar, image=self.info_icon, width=20, height=20, command=self.info_toggle)
    self.about_button.pack(side="left", padx=5,pady=5)
    # resizes copyright.png to fit button
    original_copy_image = Image.open("assets/copyright.png")
    resized_copy = original_copy_image.resize((20, 20), Image.Resampling.LANCZOS)
    self.copy_icon = ImageTk.PhotoImage(resized_copy)
    # makes the copyright button then packs it
    self.copyright_button = tk.Button(self.topbar, image=self.copy_icon, width=20, height=20, command=self.copyright_toggle)
    self.copyright_button.pack(side="left", padx=5,pady=5)
    #displays topbar
    self.topbar.pack()
    # setting up starting menu frame
    self.startScreen = tk.Frame(self.root)
    # loads start menu music
    mixer.music.load("assets/start_screen_music.mp3")
    mixer.music.play(-1)
    self.music_playing = True
    # makes and packs username box on main menu
    self.username_box = tk.Entry(self.startScreen, borderwidth=2, relief="solid", font=("helvetica", 12))
    self.username_box.insert(tk.END, "username:")
    self.username_box.pack(padx=10,pady=10)
    self.username_box.bind("<Button-1>", lambda a:self.username_box.delete(0, tk.END))
    # makes and packs start button on main menu
    self.startButton = tk.Button(self.startScreen, borderwidth=2, relief="solid", width=12, text="Start", font=("helvetica", 32), command=self.start_game)
    self.startButton.pack(padx=10,pady=10,anchor="center")
    self.startScreen.pack(padx=10,pady=10)
    # setting up game state for play
    self.game_state = tk.Frame(self.root)
    # raw card images processing
    rock_img_raw = Image.open("assets/rock.png")
    paper_img_raw = Image.open("assets/paper.png")
    scissors_img_raw = Image.open("assets/scissors.png")
    # resized images
    rock_img_resized = rock_img_raw.resize((125, 100), Image.Resampling.LANCZOS)
    paper_img_resized = paper_img_raw.resize((125, 100), Image.Resampling.LANCZOS)
    scissors_img_resized = scissors_img_raw.resize((125, 100), Image.Resampling.LANCZOS)
    # imgs ready for cards
    self.rock_img = ImageTk.PhotoImage(rock_img_resized)
    self.paper_img = ImageTk.PhotoImage(paper_img_resized)
    self.scissors_img = ImageTk.PhotoImage(scissors_img_resized)
    # creating cards for play
    self.buttonFrame = tk.Frame(self.game_state)
    self.rock= tk.Button(self.buttonFrame, borderwidth=2, width=150, height=150, relief="solid",image=self.rock_img, command=lambda:self.play_game("R") )
    self.paper= tk.Button(self.buttonFrame, borderwidth=2, width=150, height=150, relief="solid",image=self.paper_img, command=lambda:self.play_game("P"))
    self.scissors= tk.Button(self.buttonFrame, borderwidth=2, width=150, height=150, relief="solid",image=self.scissors_img, command=lambda:self.play_game("S"))
    self.buttonFrame.pack()
    # Pack buttons side by side with vertical centering
    self.rock.pack(side="left", padx=5, pady=5, anchor="center")
    self.paper.pack(side="left", padx=5, pady=5, anchor="center")
    self.scissors.pack(side="left", padx=5, pady=5, anchor="center")
    #score counter
    self.score_frame = tk.Frame(self.game_state)
    self.score = tk.Label(self.score_frame, text=f"{wins} WINS {losses} LOSSES {ties} TIES", font=("helvetica", 18))
    self.score.grid(row=1, column=1, pady=10, sticky="nsew")
    self.score_frame.pack(expand=True)
    #results screen
    self.results_screen = tk.Frame(self.root)
    self.winner_comp = tk.Frame(self.results_screen)
    self.winner_comp.pack()
    self.user_choice_label = tk.Label(self.winner_comp, text="placeholder")
    self.comp_choice_label = tk.Label(self.winner_comp, text="placeholder")
    self.winner_comparison = tk.Label(self.winner_comp, text="/")
    self.user_choice_label.pack(side="left", padx=5, pady=5, anchor="center")
    self.winner_comparison.pack(side="left", padx=5, pady=5, anchor="center")
    self.comp_choice_label.pack(side="left", padx=5, pady=5, anchor="center")
    self.retry_frame = tk.Frame(self.results_screen)
    self.retry_frame.pack()
    self.retry_button = tk.Button(self.retry_frame,borderwidth=2,relief="solid", text="Play Again", command=lambda: self.retry())
    self.retry_button.pack(padx=10,pady=10)
    # asks if your ar sure you want to quit
    self.root.protocol("WM_DELETE_WINDOW", self.on_close)
    self.root.mainloop()
  # close game and call save function
  # TODO: make save function
  def on_close(self):
    if(messagebox.askyesno(title="quit?", message="Do you really want to quit>")):
      self.root.destroy()
  # starts game by calling game_state_frame and hiding start_menu_frame 
  def play_game(self, choice):
    global ties, wins, losses  
    player_choice = choice
    computer_choice = self.comp_choice()
    # Map choices to corresponding images
    choice_images = {"R": self.rock_img, "P": self.paper_img, "S": self.scissors_img}
    self.user_choice_label.config(image=choice_images[player_choice])
    self.comp_choice_label.config(image=choice_images[computer_choice])
    if player_choice == computer_choice:
      self.winner_comparison.config(text=" = ", font=("helvetica", 32))
      ties += 1
      self.top_text.config(text=f"ITS A TIE! would you like to play again?")
    elif (player_choice == "R" and computer_choice == "S") or \
        (player_choice == "P" and computer_choice == "R") or \
        (player_choice == "S" and computer_choice == "P"):
      self.winner_comparison.config(text=" > ", font=("helvetica", 32))
      wins += 1
      self.top_text.config(text=f"YOU WON! would you like to play again?")
    else:
      self.winner_comparison.config(text=" < ", font=("helvetica", 32))
      losses += 1
      self.top_text.config(text=f"YOU LOST! would you like to play again?")
    self.game_state.pack_forget()
    self.results_screen.pack()
    self.score.config(text=f"{wins} WINS {losses} LOSSES {ties} TIES", font=("helvetica", 18))
  # music functions
  def pause_music(self):
    self.music_playing = False
    mixer.music.pause()
    self.music_button.config(image=self.no_music_icon)

  def unpause_music(self):
    self.music_playing = True
    mixer.music.unpause()
    self.music_button.config(image=self.music_icon)

  def music_toggle(self):
    if(self.music_playing):
      self.pause_music()
    elif(self.music_playing == False):
      self.unpause_music()

  # tells the player about the game
  def info_toggle(self):
    return messagebox.showinfo("About RPS", message="Rock-Paper-Scissors is a classic hand game usually played between two people. Each player simultaneously forms one of three shapes with their hand. The possible shapes are rock, paper, and scissors. The winner is determined by the rules: Rock beats scissors, scissors beat paper, and paper beats rock. \nIn this version of the game you choose a shape by clicking its corresponding card and the computer, who is your opponent, will randomly chose one as well. \nYou can begin playing by putting in your username and clicking start. \nyou can pause the music by clicking the button with a music note and unpause it by clicking the button again.")
  # opens links to web for copyright
  def open_link(self, url):
    webbrowser.open(url)
  # copyright messagebox
  def copyright_toggle(self):
    custom_message = tk.Toplevel()
    custom_message.title("CopyRight")

    img_label = tk.Label(custom_message, text="all images were sourced from:")
    img_label.pack()

    img_hyperlink = tk.Label(custom_message, text="\nhttps://www.flaticon.com/")
    img_hyperlink.pack()
    img_hyperlink.bind("<Button-1>", lambda event: self.open_link("https://www.flaticon.com/") )

    music_label = tk.Label(custom_message, text="\nall music was sourced from:")
    music_label.pack()

    music_hyperlink = tk.Label(custom_message, text="\nMain Theme (Overture) | The Grand Score by Alexander Nakarada")
    music_hyperlink.pack()
    music_hyperlink.bind("<Button-1>", lambda event: self.open_link("https://www.chosic.com/download-audio/28030/"))

    music_hyperlink = tk.Label(custom_message, text="\nSuperepic by Alexander Nakarada")
    music_hyperlink.pack()
    music_hyperlink.bind("<Button-1>", lambda event: self.open_link("https://www.chosic.com/download-audio/25860/"))

  def start_game(self):
    global username
    username= self.username_box.get()
    if username and username != "username:":
        # If username_box is not empty, save the username and proceed
        self.username = username
        self.top_text.config(text=f"Welcome {username}, please chose a card!")
        self.startScreen.pack_forget()
        self.game_state.pack(padx=10, pady=10)
        mixer.music.unload()
        mixer.music.load("assets/game_state_music.mp3")
        mixer.music.play(-1)
        self.music_button.config(image=self.music_icon)
        self.music_playing = True
        # Call function to start the game or proceed further
    else:
        # If username_box is empty, show an error message
        messagebox.showerror("Error", "Please enter a username to start the game.")
  
  def retry(self):
    global username
    self.results_screen.pack_forget()
    self.game_state.pack(padx=10, pady=10)
    self.top_text.config(text=f"Welcome back {username}, Thank you for playing again!")
  def comp_choice(self):
      choice = random.choice([0, 1, 2])
      if choice == 0:
        return 'R'
      elif choice == 1:
        return 'P'
      else:
         return 'S'
      
App()