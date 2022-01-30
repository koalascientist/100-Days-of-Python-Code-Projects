# Quiz Game

## Description

In this game, the player is presented with a question or statement, where he/she needs to answer True or False. 

The objective of the game is to get as many correct answers as possible. The game stops once all the questions of the quiz have been asked to the player. 

## Code structure

**main.py** file contains the code for the game.  
**data.py** file contains the data (i.e. the list of questions/statements and their answers) for the game.  
**question_model.py** file contains the model for the questions used for the quiz game.  
**quiz_brain.py** file contains the model for all of the questioning and quizzing functionality of the game. It will manage the following actions: asking the questions, checking if the answer was correct and checking if the player is at the end of the quiz game.  

### Question Class
Attributes:
- **text**
   (str) The text of the question/statement  
   e.g. "The Great Wall of China is visible from the moon."  
- **answer**
   (boolean) The answer to the questions/statement.  
   e.g. False  

### QuizBrain Class  
Attributes:
- **question_number**  
(int) The question number. This attribute keeps track on which question the player is currently on. The default value is 0, as the user will always start the quiz with the first question.  
- **score**
(int) The player's score. This attribute keeps track of the score of the player. The default value is 0.  
 - **questions_list**
(list) Contains the list of all the questions used for the quiz. The attribute *question_number* is used to go through the list of questions which will be passed over to QuizBrain object when it gets initialized.  

Methods:
- **next_question()**
Extracts the item for the quiz from the *questions_list* in dependence on which current *question_number* the player is on. Then, the user is asked for an input: True or False.  
- **still_has_questions()**
Returns True if there are any questions remaining in the quiz, or False if no more questions are left.   
 - **check_answer()**
Checks if the answer given by the player is correct or not, and keeps track of the player's score.   
   
