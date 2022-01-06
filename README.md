Welcome to 101 Exercises for Python Fundamentals

Solving these exercises will help make you a better programmer. Solve them in order, because each solution builds scaffolding, working code, and knowledge you can use on future problems. Read the directions carefully, and have fun!
"Learning to program takes a little bit of study and a lot of practice" - Luis Montealegre
Getting Started
Go to https://colab.research.google.com/github/ryanorsinger/101-exercises/blob/main/101-exercises.ipynb
To save your work to your Google Drive, go to File then "Save Copy in Drive".
Your own work will now appear in your Google Drive account!
If you need a fresh, blank copy of this document, go to https://colab.research.google.com/github/ryanorsinger/101-exercises/blob/main/101-exercises.ipynb and save a fresh copy in your Google Drive.
Orientation
This code notebook is composed of cells. Each cell is either text or Python code.
To run a cell of code, click the "play button" icon to the left of the cell or click on the cell and press "Shift+Enter" on your keyboard. This will execute the Python code contained in the cell. Executing a cell that defines a variable is important before executing or authoring a cell that depends on that previously created variable assignment.
Each assert line is both an example and a test that tests for the presence and functionality of the instructed exercise.
Outline
Each cell starts with a problem statement that describes the exercise to complete.
Underneath each problem statement, learners will need to write code to produce an answer.
The assert lines test to see that your code solves the problem appropriately.
Do not alter or delete the assertion tests, since those are providing automated testing.
Many exercises will rely on previous solutions to be correctly completed
The print("Exercise is complete") line will only run if your solution passes the assertion test(s)
Be sure to create programmatic solutions that will work for all inputs:
For example, calling the is_even(2) returns True, but your function should work for all even numbers, both positive and negative.
Guidance
Get Python to do the work for you. For example, if the exercise instructs you to reverse a list of numbers, your job is to find the
Save often by clicking the blue "Save" button.
If you need to clear the output or reset the notebook, go to "Run" then "Restart Session" to clear up any error messages.
Do not move or alter the lines of code that contain the assert statements. Those are what run your solution and test its actual output vs. expected outputs.
Seek to understand the problem before trying to solve it. Can you explain the problem to someone else in English? Can you explain the solution in English?
Slow down and read any error messages you encounter. Error messages provide insight into how to resolve the error. When in doubt, put your exact error into a search engine and look for results that reference an identical or similar problem.
Get Python To Do The Work For You
One of the main jobs of a programming language is to help people solve problems programatically, so we don't have to do so much by hand. For example, it's easy for a person to manually reverse the list [1, 2, 3], but imagine reversing a list of a million things or sorting a list of even a hundred things. When we write programmatic solutions in code, we are providing instructions to the computer to do a task. Computers follow the letter of the code, not the intent, and do exactly what they are told to do. In this way, Python can reverse a list of 3 numbers or 100 numbers or ten million numbers with the same instructions. Repetition is a key idea behind programming languages.
This means that your task with these exercises is to determine a sequence of steps that solve the problem and then find the Python code that will run those instructions. If you're sorting or reversing things by hand, you're not doing it right!
How To Discover How To Do Something in Python
The first step is to make sure you know what the problem is asking.
The second step is to determine, in English (or your first spoken language), what steps you need to take.
Use a search engine to look for code examples to identical or similar problems.
One of the best ways to discover how to do things in Python is to use a search engine. Go to your favorite search engine and search for "how to reverse a list in Python" or "how to sort a list in Python". That's how both learners and professionals find answers and examples all the time. Search for what you want and add "in Python" and you'll get lots of code examples. Searching for "How to sum a list of numbers in Python" is a very effective way to discover exactly how to do that task.
Learning to Program and Code

You can make a new blank cell for Python code at any time in this document.
If you want more freedom to explore learning Python in a blank notebook, go here https://colab.research.google.com/#create=true and make yourself a blank, new notebook.
Programming is an intellectual activity of designing a solution. "Coding" means turning your programmatic solution into code w/ all the right syntax and parts of the programming language.
Expect to make mistakes and adopt the attitude that the error message provides the information you need to proceed. You will put lots of error messages into search engines to learn this craft!
Because computers have zero ability to read in between the lines or "catch the drift" or know what you mean, code only does what it is told to do.
Code doesn't do what you want it to do, code does what you've told it to do.
Before writing any code, figure out how you would solve the problem in spoken language to describe the sequence of steps in the solution.
Think about your solution in English (or your natural language). It's critical to solve the problem in your natural language before trying to get a programming language to do the work.
Troubleshooting
If this entire document shows "Name Error" for many cells, it means you should read the "Getting Started" instructions above to make your own copy.
Be sure to commit your work to make save points, as you go.
If you load this page and you see your code but not the results of the code, be sure to run each cell (shift + Enter makes this quick)
"Name Error" means that you need to assign a variable or define the function as instructed.
"Assertion Error" means that your provided solution does not match the correct answer.
"Type Error" means that your data type provided is not accurate
If your kernel freezes, click on "Run" then select "Restart Session"
If you require additional troubleshooting assistance, click on "Help" and then "Docs" to access documentation for this platform.
If you have discoverd a bug or typo, please triple check your spelling then create a new issue at https://github.com/ryanorsinger/101-exercises/issues to notify the author.
What to do when you don't know what to do next
When the exercise asks you to reverse an list, the way forward is to search for "How to reverse a list in Python" in your favorite search engine.
When the exercise asks you to check if a number is even, the way forward is to search for "how to check if a number is even in Python".
When the exercise has you calculate the area of a circle, the way forward is to search for "how to calculate the area of a circle in Python" or "How to get pi in Python".
The pattern for finding what you need in JavaScript is to rely very heavily on search engine searches so you can find examples of working code and discussions about code that speak to your questions.
[ ]
# Example problem:# Uncomment the line below and run this cell.# The hashtag "#" character in a line of Python code is the comment character.  doing_python_right_now = True# The lines below will test your answer. If you see an error, then it means that your answer is incorrect or incomplete.assert doing_python_right_now == True, "If you see a NameError, it means that the variable is not created and assigned a value. An 'Assertion Error' means that the value of the variable is incorrect." print("Exercise 0 is correct") # This line will print if your solution passes the assertion above.
