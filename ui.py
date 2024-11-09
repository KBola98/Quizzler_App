THEME_COLOR = "#375362"
#importing the required modules
import tkinter as tk
from quiz_brain import QuizBrain

# Creating Quiz UI
class QuizInterface:

# Creating the main window  and setting the title
    def __init__(self, quiz_brain : QuizBrain):
        self.quiz = quiz_brain

        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.minsize(width=340, height=400)
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Creating the label for the score in the top right corner
        self.score_label = tk.Label(text="Score: 0", fg="white", bg=THEME_COLOR, font=("Arial", 12, "bold"))
        self.score_label.grid(row=0, column=1, columnspan = 2)

        self.canvas = tk.Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Question", fill=THEME_COLOR, font=("Arial", 10, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady = 50)

        # creating the function buttons for true and false
        true_image = tk.PhotoImage(file="images/true.png")
        false_image = tk.PhotoImage(file="images/false.png")

        self.true_button = tk.Button(image=true_image, highlightthickness=0)
        self.true_button.grid(row=2, column=0, pady = 20)

        self.false_button = tk.Button(image=false_image, highlightthickness=0)
        self.false_button.grid(row=2, column=1, pady = 20)
        print("success")

        self.get_next_question()

        # Run the main loop
        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)




