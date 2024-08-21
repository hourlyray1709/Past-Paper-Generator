import random 
import shutil 
import os 
from PIL import Image, ImageTk
import numpy as np 


def generate_code(): 
    code = random.randint(0,100000000)                  # modify this to add different code generation system 
    question_code = "question_{}".format(code)          # generate a code to store the question and solution, very unlikely to have the same code
    solution_code = "solution_{}".format(code)
    return question_code, solution_code

def sort_questions(src, destQuestions, destSolutions):  # dont have a / at the end of the paths
    allFiles = os.listdir(src)                          # get all files in the input folder, splits them into question and solution
                                                        # puts them in the destination folder as specified
    for file_index in range(1, len(allFiles)-1, 2): 
        question_src = src + "/" + allFiles[file_index]
        solution_src = src + "/" + allFiles[file_index+1]

        print(question_src)
        print(solution_src)

        question_code, solution_code = generate_code()

        question_dest = destQuestions + "/" + question_code + ".png"
        solution_dest = destSolutions + "/" + solution_code + ".png"

        shutil.copy(question_src, question_dest)
        shutil.copy(solution_src, solution_dest)

def get_images(src):                                           # gets ALL the images in a src folder 
    imageFiles = os.listdir(src)
    imagePaths = [src+"/"+file for file in imageFiles]
    questions = [Image.open(path) for path in imagePaths]      # open the images as a PIL object, which is used with ImageTk in main to show the image 
    return questions


#sort_questions("C:/Users/Ryan/Pictures/Screenshots", "mat/mcq_img", "mat/mcq_solution")