import random
import tkinter as tk

class MyGui:
  def __init__ (self):

    self.difficulty = None
    self.number_to_guess = None  
    self.attempts_left = None
    self.root = tk.Tk()
    self.root.geometry('500x800')
    self.root.title('number guessing game!')

    label =tk.Label(self.root, text="Number Guessing Game!", font=("helvetica", 32))
    label.pack()

    difChoices = tk.Frame(self.root)
    difChoices.columnconfigure(0, weight=1)
    difChoices.columnconfigure(1, weight=1)
    difChoices.columnconfigure(2, weight=1)
    difChoices.columnconfigure(3, weight=1)

    ChoseText = tk.Label(difChoices, text="Choose Your Difficulty", font=("helvetica", 16))
    ChoseText.grid(row=0, columnspan=4, padx=10,pady=10)

    easy = tk.Button(difChoices, text="easy", font=("helvetica", 16) , borderwidth=2, relief="solid", command=lambda: choose_difficulty("easy"))
    easy.grid(row=1, column=0, sticky=tk.W+tk.E, padx=5, pady=5)
    medium = tk.Button(difChoices, text="medium", font=("helvetica", 16) , borderwidth=2, relief="solid", command=lambda: choose_difficulty("medium"))
    medium.grid(row=1, column=1, sticky=tk.W+tk.E, padx=5, pady=5)
    hard = tk.Button(difChoices, text="hard", font=("helvetica", 16) , borderwidth=2, relief="solid", command=lambda: choose_difficulty("hard"))
    hard.grid(row=1, column=2, sticky=tk.W+tk.E, padx=5, pady=5)
    hardest = tk.Button(difChoices, text="hardest", font=("helvetica", 16) , borderwidth=2, relief="solid", command=lambda: choose_difficulty("hardest"))
    hardest.grid(row=1, column=3, sticky=tk.W+tk.E, padx=5, pady=5)

    difChoices.pack(fill='both', padx=10,pady=10)
    
    gameState = tk.Frame(self.root)
    gameState.columnconfigure(0, weight=1)
    gameState.columnconfigure(1, weight=1)
    gameState.columnconfigure(2, weight=1)

    completeState = tk.Frame(self.root)
    completeState.columnconfigure(0, weight=1)
    completeState.columnconfigure(1, weight=1)
    completeState.columnconfigure(2, weight=1)

    gameLabel = tk.Label(gameState, text="", font=("helvetica", 16))
    gameLabel.grid(row=0, columnspan=3, padx=10,pady=10)

    chosebetween = tk.Label(gameState, text="", font=("helvetica", 16))
    chosebetween.grid(row=1, columnspan=3, padx=10,pady=10)

    guess = tk.Entry(gameState, borderwidth=2, relief="solid", font=("helvetica", 16))
    guess.grid(row=2, columnspan=3)

    guesses = tk.Label(gameState, text="", font=("helvetica", 16))
    guesses.grid(row=3, columnspan=3)

    retryText = tk.Label(gameState, text="", font=("helvetica", 16))
    retryText.grid(row=4, columnspan=3)

    btn1 = tk.Button(gameState, text="1", font=("helvetica", 18), borderwidth=2, relief="solid", command=lambda: update_guess("1", guess))
    btn1.grid(row=5, column=0, sticky=tk.W+tk.E, padx=5, pady=5)

    btn2 = tk.Button(gameState, text="2", font=("helvetica", 18), borderwidth=2, relief="solid", command=lambda: update_guess("2", guess))
    btn2.grid(row=5, column=1, sticky=tk.W+tk.E, padx=5, pady=5)

    btn3 = tk.Button(gameState, text="3", font=("helvetica", 18), borderwidth=2, relief="solid", command=lambda: update_guess("3", guess))
    btn3.grid(row=5, column=2, sticky=tk.W+tk.E, padx=5, pady=5)

    btn4 = tk.Button(gameState, text="4", font=("helvetica", 18), borderwidth=2, relief="solid", command=lambda: update_guess("4", guess))
    btn4.grid(row=6, column=0, sticky=tk.W+tk.E, padx=5, pady=5)

    btn5 = tk.Button(gameState, text="5", font=("helvetica", 18), borderwidth=2, relief="solid", command=lambda: update_guess("5", guess))
    btn5.grid(row=6, column=1, sticky=tk.W+tk.E, padx=5, pady=5)

    btn6 = tk.Button(gameState, text="6", font=("helvetica", 18), borderwidth=2, relief="solid", command=lambda: update_guess("6", guess))
    btn6.grid(row=6, column=2, sticky=tk.W+tk.E, padx=5, pady=5)

    btn7 = tk.Button(gameState, text="7", font=("helvetica", 18), borderwidth=2, relief="solid", command=lambda: update_guess("7", guess))
    btn7.grid(row=7, column=0, sticky=tk.W+tk.E, padx=5, pady=5)

    btn8 = tk.Button(gameState, text="8", font=("helvetica", 18), borderwidth=2, relief="solid", command=lambda: update_guess("8", guess))
    btn8.grid(row=7, column=1, sticky=tk.W+tk.E, padx=5, pady=5)

    btn9 = tk.Button(gameState, text="9", font=("helvetica", 18), borderwidth=2, relief="solid", command=lambda: update_guess("9", guess))
    btn9.grid(row=7, column=2, sticky=tk.W+tk.E, padx=5, pady=5)

    btn0 = tk.Button(gameState, text="0", font=("helvetica", 18), borderwidth=2, relief="solid", command=lambda: update_guess("0", guess))
    btn0.grid(row=8, column=1, sticky=tk.W+tk.E, padx=5, pady=5)

    btnb = tk.Button(gameState, text="←", font=("helvetica", 18), borderwidth=2, relief="solid", command=lambda: backspace(guess))
    btnb.grid(row=8, column=2, sticky=tk.W+tk.E, padx=5, pady=5)

    btnc = tk.Button(gameState, text="Clear", font=("helvetica", 18), borderwidth=2, relief="solid", command=lambda: clear(guess))
    btnc.grid(row=9, columnspan=3, sticky=tk.W+tk.E, padx=5, pady=5)

    btns = tk.Button(gameState, text="Submit", font=("helvetica", 18), borderwidth=2, relief="solid", command=lambda: submit(self, guess))
    btns.grid(row=10, columnspan=3, sticky=tk.W+tk.E, padx=5, pady=5)

    btnr = tk.Button(gameState, text="Reset", font=("helvetica", 18), borderwidth=2, relief="solid", command=lambda: reset_game())
    btnr.grid(row=11, columnspan=3, sticky=tk.W+tk.E, padx=5, pady=5)

    def choose_difficulty(difficulty):
      self.difficulty = difficulty
      difChoices.pack_forget()
      gameLabel.config(text=f"You have chosen {self.difficulty} difficulty")
      tell_difficulty()
      gameState.pack(fill='both', padx=10,pady=10)
      self.number_to_guess = generate_number_to_guess()

    def generate_number_to_guess():
      lower = 1
      if(self.difficulty == 'hardest'):
        upper = 1_000
        self.attempts_left = 15
      elif(self.difficulty == 'hard'):
        upper = 100
        self.attempts_left = 10
      elif(self.difficulty == 'medium'):
        upper = 50
        self.attempts_left = 5
      elif(self.difficulty == 'easy'):
        upper = 10
        self.attempts_left = 5
      return random.randint(lower, upper)

    def tell_difficulty():
      if(self.difficulty == 'hardest'):
        chosebetween.config(text="Choose any number between 1 and 1,000")
      elif(self.difficulty == 'hard'):
        chosebetween.config(text="Choose any number between 1 and 100")
      elif(self.difficulty == 'medium'):
        chosebetween.config(text="Choose any number between 1 and 50")
      elif(self.difficulty == 'easy'):
        chosebetween.config(text="Choose any number between 1 and 10")

    def update_guess(number, entry_widget):
      entry_widget.insert(tk.END, number)
    
    def clear(self):
      self.delete(0, tk.END)

    def backspace(self):
      current_text = self.get()
      new_text = current_text[:-1]  # Remove the last character
      clear(guess)  # Clear the entry field
      guess.insert(0, new_text)  # Insert the updated text back into the entry field

    def reset_game():
      self.difficulty = None
      clear(guess)
      gameState.pack_forget()
      completeState.pack_forget()
      difChoices.pack(fill='both',padx=10,pady=10)

    def submit(self, guess):
        try:
          guessed = int(guess.get())

          # Update attempts left text
          self.attempts_left -= 1  # Decrement attempts_left
          guesses.config(text=f"You have {self.attempts_left} attempts Left")
          clear(guess)

          if (guessed == self.number_to_guess):
              gameState.pack_forget()
              retryText.config(text="")
              numIs = tk.Label(completeState, text=f"Congratulations! You Guessed Correctly: {self.number_to_guess}")
              numIs.grid(row=0, columnspan=3)
              btnr2 = tk.Button(completeState, text="Reset", font=("helvetica", 18), command=lambda: reset_game())
              btnr2.grid(row=1, columnspan=3, sticky=tk.W+tk.E, padx=5, pady=5)
              completeState.pack(fill='both', padx=10, pady=10)
          elif (guessed < self.number_to_guess):
              retryText.config(text="Too Low Try Again!")
          elif (guessed > self.number_to_guess):
              retryText.config(text="Too High Try Again!")


          if ((self.attempts_left == 0) and (guessed != self.number_to_guess)):
              gameState.pack_forget()
              retryText.config(text="")
              numIs = tk.Label(completeState, text=f"Sorry, You didn't guess the number. It was: {self.number_to_guess}")
              numIs.grid(row=0, columnspan=3)
              btnr2 = tk.Button(completeState, text="Reset", font=("helvetica", 18), command=lambda: reset_game())
              btnr2.grid(row=1, columnspan=3, sticky=tk.W+tk.E, padx=5, pady=5)
              completeState.pack(fill='both', padx=10, pady=10)
        except ValueError:
          guesses.config(text="Please only enter numbers.")
    self.root.mainloop()

MyGui()