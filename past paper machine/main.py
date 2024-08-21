from file_lib import * 
import random 
import matplotlib.pyplot as plt 
import numpy 
import tkinter as tk
from PIL import ImageTk
from tkinter import messagebox
currentQuestion, currentSolution, questionArr, solutionArr = [],[],None,None

def show_image(main_window, imgLabel, image):             # solution uses PIL Image object
    if image != None: 
        img = ImageTk.PhotoImage(image)
        imgLabel.configure(image=img)
        main_window.mainloop()
    else: 
        print("test finished")


def pick_random_question(questionArr, solutionArr): 
    if len(questionArr) > 0: 
        index = random.randint(0, len(questionArr)-1)
        question = questionArr[index]
        solution = solutionArr[index]
        questionArr = [i for i in questionArr if i != question]
        solutionArr = [i for i in solutionArr if i != solution]
        return question, solution, questionArr, solutionArr
    else: 
        return None, None, [], [] 
        
    
    
def gotoNextQuestion(main_window, imageLabel):
    global questionArr, solutionArr, currentQuestion, currentSolution
    currentQuestion, currentSolution, questionArr, solutionArr = pick_random_question(questionArr, solutionArr)
    show_image(main_window, imageLabel, currentQuestion)


def quiz(_questionArr, _solutionArr):
    global questionArr, solutionArr, currentQuestion, currentSolution
    questionArr = _questionArr
    solutionArr = _solutionArr
    currentQuestion, currentSolution, questionArr, solutionArr = pick_random_question(questionArr, solutionArr)

    main_window = tk.Tk()
    main_window.geometry("1000x700")

    imageFrame = tk.Frame(main_window,  width=1000, height=650)
    imageFrame.grid(row=0, column=0)

    imageLabel = tk.Label(imageFrame)
    imageLabel.grid(row=0, column=0)

    buttonFrame = tk.Frame(main_window, width=1000, height=50)
    buttonFrame.grid(row=1, column=0)

    solutionButton = tk.Button(buttonFrame, text="Display Solution", command=lambda:show_image(main_window, imageLabel, currentSolution))
    solutionButton.grid(row=0, column=0)

    questionButton = tk.Button(buttonFrame, text="Display Question", command=lambda:show_image(main_window, imageLabel, currentQuestion))
    questionButton.grid(row=0, column=1)

    nextButton = tk.Button(buttonFrame, text="Next Question", command=lambda:gotoNextQuestion(main_window, imageLabel))
    nextButton.grid(row=0, column=2)


    main_window.mainloop()

    

quiz(get_images("mat/mcq_img"), get_images("mat/mcq_solution"))