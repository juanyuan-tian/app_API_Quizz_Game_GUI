from tkinter import *
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(background=THEME_COLOR, padx=20, pady=20)
        # Label
        self.score = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score.grid(row=1, column=2, padx=20, pady=20)
        # canvas
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="question",
                                                     width=280,
                                                     font=("Arial", 20, "italic"))
        self.canvas.grid(row=2, column=1, columnspan=2, pady=50)
        # botton 我的图特别小，和像素不成比例😭
        # PhotoImage("/images/true.png")用错了 少了file👈 👈 👈 👈 👈 🤙🤙🤙🤙🤙🤙
        # 其次是Button(image=PhotoImage(file="images/true.png")要分开，一起写图片找出来白板。👈 👈 🤙🤙
        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.click_true)
        self.true_button.grid(row=3, column=1)
        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.click_false)
        self.false_button.grid(row=3, column=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.score.config(text=f"score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="end of quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def click_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def click_false(self):
        is_false = self.quiz.check_answer("False")
        self.give_feedback(is_false)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

