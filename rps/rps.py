import tkinter as tk
import random
import os
from pygame import mixer
from PIL import ImageTk, Image
from tkinter import messagebox
import webbrowser

class App:
  def __init__(self):
    global username
    global wins
    global losses
    # create window
    self.root = tk.Tk()
    # set window size
    # self.root.geometry("800x400")
    # make window non-resizable
    self.root.resizable(False,False)
    # set window title
    self.root.title("Rock Paper Scissors")
    # initialize mixer from pygame for music
    mixer.init()
    # boolean variable to control if music plays
    self.music_playing = False
    # setting up variables for play
    # make top text for game
    self.top_text = tk.Label(self.root, text="Rock! Paper! Scissors!", font=("helvetica", 18))
    # place text in window
    self.top_text.pack(padx=10,pady=10)
    # resize musical-note.png to fit in music_button
    original_music_image = Image.open("assets/musical-note.png")
    resized_music_image = original_music_image.resize((20, 20), Image.Resampling.LANCZOS)
    self.music_icon = ImageTk.PhotoImage(resized_music_image)
    # resizes music.png to fit music_button
    original_no_music_image = Image.open("assets/music.png")
    resized_no_music_image = original_no_music_image.resize((20, 20), Image.Resampling.LANCZOS)
    self.no_music_icon = ImageTk.PhotoImage(resized_no_music_image)
    # makes the button that pauses/unpauses the music then places it
    self.music_button = tk.Button(self.root, image=self.music_icon,width=20,height=20, command=self.music_toggle)
    self.music_button.pack(side="right",padx=5,pady=5)
    # resizes info.png to fit the info button
    original_info_image = Image.open("assets/info.png")
    resized_info = original_info_image.resize((20, 20), Image.Resampling.LANCZOS)
    self.info_icon = ImageTk.PhotoImage(resized_info)
    # makes the about RPS button and how to play then places it 
    self.about_button = tk.Button(self.root, image=self.info_icon, width=20, height=20, command=self.info_toggle)
    self.about_button.pack(side="right"padx=5,pady=5)
    # resizes copyright.png to fit button
    original_copy_image = Image.open("assets/copyright.png")
    resized_copy = original_copy_image.resize((20, 20), Image.Resampling.LANCZOS)
    self.copy_icon = ImageTk.PhotoImage(resized_copy)
    # makes the copyright button then places it
    self.copyright_button = tk.Button(self.root, image=self.copy_icon, width=20, height=20, command=self.copyright_toggle)
    self.copyright_button.pack(side="right", padx=5,pady=5)
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
    rock_img = ImageTk.PhotoImage(rock_img_resized)
    paper_img = ImageTk.PhotoImage(paper_img_resized)
    scissors_img = ImageTk.PhotoImage(scissors_img_resized)
    # creating cards for play
    self.rock= tk.Button(self.game_state, borderwidth=2, width=150, height=150, relief="solid",image=rock_img)
    self.paper= tk.Button(self.game_state, borderwidth=2, width=150, height=150, relief="solid",image=paper_img)
    self.scissors= tk.Button(self.game_state, borderwidth=2, width=150, height=150, relief="solid",image=scissors_img)
    # Pack buttons side by side with vertical centering
    self.rock.pack(side="left", padx=5, pady=5, anchor="center")
    self.paper.pack(side="left", padx=5, pady=5, anchor="center")
    self.scissors.pack(side="left", padx=5, pady=5, anchor="center")
    #results screen
    results_screen = tk.Frame(self.root)
    winner = tk.Label(results_screen, text="placeholder")
    loser = tk.Label(results_screen, text="placeholder")
    # asks if your ar sure you want to quit
    self.root.protocol("WM_DELETE_WINDOW", self.on_close)
    self.root.mainloop()
  # close game and call save function
  # TODO: make save function
  def on_close(self):
    if(messagebox.askyesno(title="quit?", message="Do you really want to quit>")):
      self.root.destroy()

  # starts game by calling game_state_frame and hiding start_menu_frame 
  def calls_game_state(self):
    if(self.username_box):
      pass

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
    username= self.username_box.get()
    if username and username != "username:":
        # If username_box is not empty, save the username and proceed
        self.username = username
        self.top_text.config(text=f"Welcome {username}, please chose a card!")
        self.startScreen.pack_forget()
        self.game_state.pack()
        mixer.music.unload()
        mixer.music.load("assets/game_state_music.mp3")
        mixer.music.play(-1)
        # Call function to start the game or proceed further
    else:
        # If username_box is empty, show an error message
        messagebox.showerror("Error", "Please enter a username to start the game.")
  
  def comp_choice():
      choice = random.choice([0, 1, 2])
      if choice == 0:
        return 'R'
      elif choice == 1:
        return 'P'
      else:
         return 'S'

App()