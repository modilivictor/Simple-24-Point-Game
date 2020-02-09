#   24Points
#   24Points.py
#   Modi Li
#   Victor
#   Section M001
#   mli207

from graphics import *
from random import *

"""
Read questions from the input file.

param fileName: name of the file
"""
def getQuestionsFromFile(fileName):
    questions = [] # Initialize a list of all the questions
    inputFile = open(fileName, "r") # IFL ; open input file
    for line in inputFile: # read through each line
        line = line.strip('\n')
        numbers = line.split(" ") # split the line into a list of the 4 numbers
        questions.append(numbers) # add the list of the 4 numbers to the questions list
    return questions # return the questions list back
    
"""
Class of the play view in which the user will input equations to get 24.
"""
class PlayView: # CLOD
    
    def __init__(self, question, questionTurn, totalQuestionsAmount, win):
        # set values that are imported from the constructor as the properties of the class
        self.question = question
        self.questionTurn = questionTurn
        self.totalQuestionsAmount = totalQuestionsAmount
        self.win = win
        
        # draw each object to the graph window and set the object to the class so that they can be removed afterwards
        self.questionTitle = self.drawQuestionTitle()
        self.noteText = self.drawNoteText()
        self.questionProgress = self.drawQuestionProgress(self.questionTurn, self.totalQuestionsAmount)
        self.inputBox = self.drawInputBox()
        self.equals24Text = self.drawEquals24Text()
        self.submitButton = self.drawSubmitButton()
        self.submitButtonText = self.drawSubmitButtonText()
        
        # put all objects together into a list
        # this will be used in remove()
        self.objects = [self.questionTitle, self.noteText, self.questionProgress, self.inputBox, self.equals24Text, self.submitButton, self.submitButtonText] # LOOD
       
    """
    draw the question title to the graph window and return it back
    """
    def drawQuestionTitle(self):
        titleString = "{0}  {1}  {2}  {3}".format(self.question[0],self.question[1],self.question[2],self.question[3]) # show the four numbers of the question
        questionTitle = Text(Point(5,7.5), titleString) # OTXT ; create the Text object
        questionTitle.setFill(color_rgb(19,142,242)) # set the color of the text
        questionTitle.setSize(36) # set font size of the text
        questionTitle.draw(self.win) # draw it to the win
        return questionTitle # return the questionTitle back
    
    """
    draw the note text to the graph window and return it back
    """
    def drawNoteText(self):
        noteString = "Enter numbers in the small boxes and operators in the big boxes." # string to be shown
        noteText = Text(Point(5,7), noteString) # create the Text object
        noteText.setFill(color_rgb(84,146,196)) # set the color of the text
        noteText.setSize(20) # set font size of the text
        noteText.draw(self.win) # draw it to the win
        return noteText # return the noteText back
    
    """
    draw the question progress (like ' Question 2/3') to the graph window and return it back
    param currentQuestionTurn: the current turn of the game, such as 2.
    param totalQuestionsAmount: the total amount of questions in the game
    """ 
    def drawQuestionProgress(self, currentQuestionTurn, totalQuestionsAmount):
        questionProgressString = "Question  {0}/{1}".format(currentQuestionTurn, totalQuestionsAmount) # create the string to be shown
        questionProgress = Text(Point(9,7.6), questionProgressString) # create the Text object
        questionProgress.setFill(color_rgb(19,142,242)) # set the color of the text
        questionProgress.setSize(22) # set font size of the text
        questionProgress.draw(self.win) # draw it to the win
        return questionProgress # return the questionProgress back
    
    """
    draw the input box to the graph window and return it back
    """ 
    def drawInputBox(self):
        inputBox = Entry(Point(5,6), 20) # create the Entry object
        inputBox.setFill("white") # set the color of the text
        inputBox.setSize(30) # set font size of the text
        inputBox.draw(self.win) # draw it to the win
        return inputBox # return the inputBox back
    
    """
    draw the equal 24 text to the graph window and return it back
    """
    def drawEquals24Text(self):
        equals24Text = Text(Point(8.5,6), "= 24") # create the Text object
        equals24Text.setSize(28) # set font size of the text
        equals24Text.draw(self.win) # draw it to the win
        return equals24Text # return the equals24Text back
    
    """
    draw the submit button to the graph window and return it back
    """
    def drawSubmitButton(self):
        submitButton = Rectangle(Point(4,1.6), Point(6,1)) # draw the Rectangle object
        submitButton.setOutline(color_rgb(158,158,240)) # set the color of the outline
        submitButton.setFill(color_rgb(158,158,240)) # set the color
        submitButton.draw(self.win) # draw it to the win
        return submitButton # return it back
    
    """
    draw the submit button text to the graph window and return it back
    """
    def drawSubmitButtonText(self):
        submitButtonText = Text(Point(5,1.3), "Submit") # draw the Text object
        submitButtonText.setFill("white") # set the text color
        submitButtonText.setSize(20) # set the font size
        submitButtonText.draw(self.win) # draw to the win
        return submitButtonText # return it back
    
    """
    Check if the result of input is correct
    """
    def checkResult(self):
        userInput = self.inputBox.getText() # IEB - Get user input
        
        numbersInUserInput = []
        
        for i in range(len(userInput)):
            # if there are two characters together that both are numbers, then it must be wrong.
            # also make sure that i is not the end of the list by using:     i != len(userInput)-1
            if i != len(userInput)-1 and userInput[i].isdigit() and userInput[i+1].isdigit():
                return False
            
            # add all numbers to listOfNumbersInUserInput
            if userInput[i].isdigit():
                numbersInUserInput.append(int(userInput[i]))
        
        # if there are more than 4 numbers, then it must be wrong
        if len(numbersInUserInput) != 4:
            return False
            
        # sort the question list and numbersInUserInput list and check if they are equal
        self.question.sort()
        numbersInUserInput.sort()
        # if they are not equal, then it must be wrong
        if self.question != numbersInUserInput:
            return False
        
        # String of all the characters that are allowed
        operatorsAndNumbers = "+-*/(){0}{1}{2}{3}".format(self.question[0],self.question[1],self.question[2],self.question[3])
        
        
        # Check if all characters entered are among the operatorsAndNumbers and the result is equal to 24.
        if all(c in operatorsAndNumbers for c in userInput) and eval(userInput) == 24:
            return True # return true if is correct
        
        return False # return false if is incorrect
    
    # get the userAnswer text
    def getUserAnswer(self):
        return self.inputBox.getText()
    
    # get the submit button (rectangle)
    def getSubmitButton(self):
        return self.submitButton
    
    # remove the whole view
    def remove(self):
        # undraw each object in the list
        for item in self.objects: # LOOD
            item.undraw()
    
    # show the incorrectText
    def showIncorrectText(self):
        incorrectText = Text(Point(5,4), "Incorrect. Please try Again") # create the Text object
        incorrectText.setFill("red") # set text color
        incorrectText.setSize(20) # set font size
        incorrectText.draw(self.win) # draw it to the window
        time.sleep(1) # wait for 2 seconds
        incorrectText.undraw() # remove it from the view


"""
Class of the view showing that the player finished a question successfully.
"""
class SuccessView:
    
    def __init__(self, win):
        self.win = win
        self.successText = self.drawSuccessText()
        self.continueButton = self.drawContinueButton()
        self.continueButtonText = self.drawContinueButtonText()
    
    # draw the successText
    def drawSuccessText(self):
        successText = Text(Point(5,7.5), "Success!") # create Text object
        successText.setFill(color_rgb(19,142,242)) # set text color
        successText.setSize(30) # set font size
        successText.draw(self.win) # draw it to the win
        return successText # return back
    
    # draw the continueButton
    def drawContinueButton(self):
        continueButton = Rectangle(Point(4,5), Point(6,4)) # create the Rectangle object
        continueButton.setOutline(color_rgb(158,158,240)) # set outline color
        continueButton.setFill(color_rgb(158,158,240)) # set fill color
        continueButton.draw(self.win) # draw it to the win
        return continueButton # return it back
    
    # draw the continueButtonText
    def drawContinueButtonText(self):
        continueButtonText = Text(Point(5,4.5), "Continue") # create the Text object with the position at the center of the continueButton
        continueButtonText.setFill("white")  # set text color
        continueButtonText.setSize(20) # set font size
        continueButtonText.draw(self.win) # draw it to the win
        return continueButtonText # return it back
    
    # get the continueButton object
    def getContinueButton(self):
        return self.continueButton
    
    # remove the whole view
    def remove(self):
        self.successText.undraw()
        self.continueButton.undraw()
        self.continueButtonText.undraw()
    
"""
check if a point is inside a rectangle; this is used for detecting a button click
param point: the point to be checked
param rectangle: the rectangle to be checked
"""
def isInside(point,rectangle):
    return rectangle.getP1().getX() < point.getX() < rectangle.getP2().getX() and rectangle.getP2().getY() < point.getY() < rectangle.getP1().getY()
    
"""
Class of the view showing that the player has finished the whole game.
"""
class FinalSuccessView:
    
    def __init__(self, win):
        self.win = win
        self.finalSuccessText = self.drawFinalSuccessText()
        self.exitButton = self.drawExitButton()
        self.exitButtonText = self.drawExitButtonText()  
    
    # draw the finalSuccessText
    def drawFinalSuccessText(self):
        finalSuccessText = Text(Point(5,7.5), "You have finished! Your answers have been saved into questions_and_player_answers.txt.") # create the Text object
        finalSuccessText.setFill(color_rgb(19,142,242)) # set text color
        fontSize = randrange(20,30) # RND ; choose random font size
        finalSuccessText.setSize(fontSize) # set font size
        finalSuccessText.draw(self.win) # draw it to the win
        
    # draw the exit button
    def drawExitButton(self):
        exitButton = Rectangle(Point(4,5), Point(6,4)) # create the rectangle object
        exitButton.setOutline(color_rgb(158,158,240)) # set the outline color
        exitButton.setFill(color_rgb(158,158,240)) # set the fill color
        exitButton.draw(self.win) # draw it to the win
        return exitButton # return it back
    
    # draw the exitButtonText
    def drawExitButtonText(self):
        exitButtonText = Text(Point(5,4.5), "Exit") # create the Text object with the position at the center of the exitButton
        exitButtonText.setFill("white") # set text color
        exitButtonText.setSize(25) # set font size
        exitButtonText.draw(self.win) # draw it to the win
    
    # get the exitButton
    def getExitButton(self):
        return self.exitButton
    

def main():
    win = GraphWin("24 Points",800,640) # GW ; create the GraphWin object
    win.setCoords(0, 0, 10, 8) # set its coordinates
    win.setBackground(color_rgb(239,239,244)) # set its background color
    
    questions = getQuestionsFromFile("questions_source.txt") # FNC ; read from the input source file
    questionsCounts = len(questions) # get the amount of questions by reading the length of the questions list
    
    userAnswers = [] # initialize a list that contains all the user's answers
    
    # iterate by the index of the range questionsCounts
    for i in range(questionsCounts):
        
        question = questions[i]
        
        # convert each element in questions to int and append to numbersList
        numbersList = [] # initialize numbersList
        for j in range(len(question)):
            numbersList.append(int(question[j]))
        
        playView = PlayView(numbersList,i+1,questionsCounts,win) # CLOD ; create a PlayView object
        win.checkMouse() # check mouse click
        
        while True:
            clickPoint = win.getMouse() # IMS ; get the point of the mouse click
            # check if the click point is inside the button
            if isInside(clickPoint, playView.getSubmitButton()): # if is inside
                # check if the result is correct
                if (playView.checkResult()): # if the result is correct
                    playView.remove() # remove the playView
                    successView = SuccessView(win) # show the successView by creating a SuccessView object
                    userAnswers.append(playView.getUserAnswer()) # append the user's answer to the userAnswers
                    break # break the while loop
                else:
                    playView.showIncorrectText() # if incorrect, then show incorrectText
                        
        
        while True:
            clickPoint = win.getMouse() # get the point of the mouse click
            # check if the click point is inside the button
            if isInside(clickPoint, successView.getContinueButton()): # if is inside
                successView.remove() # remove the successView
                break
    
    
    playerAnswersOutput = open("questions_and_player_answers.txt", "w") # open the output file
    print("Questions & Player's Answers", file=playerAnswersOutput)
    for k in range(len(questions)):
        print(', '.join(questions[k]), file=playerAnswersOutput)
        print(userAnswers[k], file=playerAnswersOutput)
    
    # showFinalSuccessView
    finalSuccessView = FinalSuccessView(win) # create a FinalSuccessView object
    clickPoint = win.getMouse() # get clickPoint
    if isInside(clickPoint, finalSuccessView.getExitButton()): # if clickPoint is inside exitButton
        win.close() # close the window
    
main()
