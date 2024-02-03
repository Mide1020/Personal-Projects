import tkinter as tk
from tkinter import messagebox
import random

class QuizGame:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.current_question_index = 0

    def ask_question(self, question):
        question_text = question['question']
        options = question['options']
        correct_answer = question['correct_answer']

        root = tk.Tk()
        root.title("Quiz Game")
        root.geometry("400x300")
        root.config(bg="#F9EBB2")  # Set background color

        # Question Label
        question_label = tk.Label(root, text=question_text, font=("Helvetica", 14), bg="#F9EBB2")
        question_label.pack(pady=10)

        # Radio Buttons for Options
        selected_option = tk.StringVar()
        for i, option in enumerate(options, start=1):
            option_radio = tk.Radiobutton(root, text=f"{i}. {option}", variable=selected_option, value=str(i),
                                           font=("blue", 12), bg="skyblue", anchor=tk.W)
            option_radio.pack(anchor=tk.W)

        # Submit Button
        submit_button = tk.Button(root, text="Submit", command=lambda: self.check_answer(question, selected_option.get(), root),
                                  font=("Helvetica", 12), bg="#4CAF50", fg="white")
        submit_button.pack(pady=10)

        root.mainloop()

    def check_answer(self, question, user_answer, root):
        if user_answer.isdigit() and 1 <= int(user_answer) <= len(question['options']):
            user_answer_index = int(user_answer) - 1
            if question['options'][user_answer_index] == question['correct_answer']:
                messagebox.showinfo("Correct", "Your answer is correct!")
                self.score += 1
            else:
                messagebox.showinfo("Incorrect", f"Wrong! The correct answer is: {question['correct_answer']}")
            root.destroy()
            self.next_question()
        else:
            messagebox.showinfo("Invalid Input", "Please select a valid option.")

    def next_question(self):
        self.current_question_index += 1
        if self.current_question_index < len(self.questions):
            self.ask_question(self.questions[self.current_question_index])
        else:
            self.show_final_score()

    def show_final_score(self):
        messagebox.showinfo("Quiz Completed", f"Quiz completed! Your final score is: {self.score}/{len(self.questions)}")


if __name__ == "__main__":
    # Sample questions for the quiz
    quiz_questions = [
        {
            'question': 'What is the capital of France?',
            'options': ['Berlin', 'Paris', 'Madrid', 'Rome'],
            'correct_answer': 'Paris'
        },
        {
            'question': 'Which planet is known as the Red Planet?',
            'options': ['Mars', 'Venus', 'Jupiter', 'Saturn'],
            'correct_answer': 'Mars'
        },
        {
            'question': 'What is the largest mammal in the world?',
            'options': ['Elephant', 'Blue Whale', 'Giraffe', 'Hippopotamus'],
            'correct_answer': 'Blue Whale'
        },
        {
            'question': 'Which of this is an Italian Football Club',
            'options': ['Girona', 'Mainz', 'Lens', 'Lazio'],
            'correct_answer': 'Lazio'
        },
        {
            'question': 'What is the currency of China',
            'options' : ['Chinese Dinar', 'Chinese Franc', 'Chinese Yuan', 'Chinese CFA'],
            'correct_answer': 'Chinese Yuan'
        },
        {
            'question': 'Which European country would you find Belgrade',
            'options' : ['Serbia', 'Uzbekistan', 'Panama', 'Seychelles'],
            'correct_answer': 'Serbia' 
        },
        {
            'question': 'Which country is known as the land of the rising sun',
            'options': ['South Korea', 'Japan', 'China', 'Vietnam'],
            'correct_answer': 'Japan'
        },
        {
            'question': 'What is the capital of Austrailia',
            'options': ['Canberra', 'Vienna', 'Sydney', 'Melbourne'],
            'correct_answer': 'Canberra'
        },
        {
            'question': 'Which country can you find in Oceania',
            'options': ['New Tasmania', 'Austrailia', 'Grenada', 'Madagascar'],
            'correct_answer': 'Austrailia'
        },
        {
            'question': 'What is the second most populated black country',
            'options': ['Sudan', 'Egypt', 'Ethiopia', 'DR Congo'],
            'correct_answer': 'Ethiopia'
        }
    ]

    # Instantiate and start the quiz
    quiz = QuizGame(quiz_questions)
    quiz.ask_question(quiz.questions[0])  # Start with the first question