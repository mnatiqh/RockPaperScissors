import tkinter as tk
from PIL import Image, ImageTk
import random

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors Game")
        self.root.geometry("1500x750")
        self.root.configure(background="gray80")
        self.player_score = 0
        self.player_losses = 0
        self.create_widgets()

    def create_widgets(self):
        self.title = tk.Label(self.root , text="Rock Paper Scissors" , font=("Century Gothic" , 50) , fg="darkslategray" , bg="gray80" )
        self.title.place(x=410,y=30)

        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 16))
        self.result_label.place(x=1,y=1)

        self.user_choice_label = tk.Label(self.root, text="Your choice:", font=("Century Gothic", 14) , fg="dodgerblue4",bg="gray80")
        self.user_choice_label.place(x=1200,y=75)

        self.computer_choice_label = tk.Label(self.root, text="Computer's choice:", font=("Century Gothic", 14) , fg="dodgerblue4" , bg="gray80")
        self.computer_choice_label.place(x=1200 , y=400)

        self.rules_label = tk.Label(self.root , text="How to Play: " , bg="gray80" , width=20 , font=("Century Gothic" , 20))
        self.rules_label.place(x=610 , y=300)

        self.instructions_label = tk.Label(self.root , text="- Click one of the options\n on the left\n- Close and reopen the tab\n to reset scores" , bg="gray80" , font=("Century Gothic" , 15))
        self.instructions_label.place(x=630 , y=350)

        self.user_choice_canvas = tk.Canvas(self.root, width=170, height=170 , bg="gray80")
        self.user_choice_canvas.place(x=1200 , y=125)
        
        self.computer_choice_canvas = tk.Canvas(self.root, width=170, height=170 , bg="gray80")
        self.computer_choice_canvas.place(x=1200 , y=450)
        
        self.rock_img = Image.open("rock.png")
        self.paper_img = Image.open("paper.png")
        self.scissors_img = Image.open("scissors.png")
        
        self.rock_img = self.rock_img.resize((175, 175))
        self.paper_img = self.paper_img.resize((175, 175))
        self.scissors_img = self.scissors_img.resize((175, 175))
        
        self.rock_photo = ImageTk.PhotoImage(self.rock_img)
        self.paper_photo = ImageTk.PhotoImage(self.paper_img)
        self.scissors_photo = ImageTk.PhotoImage(self.scissors_img)
        
        self.rock_button = tk.Button(self.root, image=self.rock_photo, command=lambda: self.play("rock"), activebackground="teal", bg="gray80")
        self.rock_button.place(x=50, y=90)

        self.paper_button = tk.Button(self.root, image=self.paper_photo, command=lambda: self.play("paper"), activebackground="teal", bg="gray80")
        self.paper_button.place(x=50, y=280)

        self.scissors_button = tk.Button(self.root, image=self.scissors_photo, command=lambda: self.play("scissors"), activebackground="teal", bg="gray80")
        self.scissors_button.place(x=50, y=470)

        self.player_score_label = tk.Label(self.root, text="Player Wins: 0", font=("Century Gothic", 16), fg="darkgreen", bg="gray80")
        self.player_score_label.place(x=680, y=520)
        
        self.player_losses_label = tk.Label(self.root, text="Player Losses: 0", font=("Century Gothic", 16), fg="darkred", bg="gray80")
        self.player_losses_label.place(x=680, y=550)

    def update_score_labels(self):
        self.player_score_label.config(text=f"Player Score: {self.player_score}")
        self.player_losses_label.config(text=f"Player Losses: {self.player_losses}")

    def play(self, user_choice):
        self.result_label.config(text="")

        computer_choice = random.choice(["rock", "paper", "scissors"])
        self.update_choice_canvas(self.user_choice_canvas, user_choice)
        self.update_choice_canvas(self.computer_choice_canvas, computer_choice)
        
        self.root.update()

        if user_choice == computer_choice:
            result = "It's a tie!"
            colour = "darkorange1"
        elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
            result = "You win!"
            colour = "forest green"
            self.player_score += 1
        else:
            result = "Computer wins!"
            colour = "crimson"
            self.player_losses += 1
        
        self.update_score_labels()
        
        self.result_label.config(text=result, fg=colour, font=("Century Gothic", 40), bg="gray80", width=20)
        self.result_label.place(x=430, y=200)
        
    def update_choice_canvas(self, canvas, choice):
        canvas.delete("all")
        canvas.create_image(0, 0, anchor="nw", image=getattr(self, f"{choice}_photo"))

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissorsGame(root)
    root.mainloop()
