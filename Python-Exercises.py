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

[ ]
 # Exercise 1
# On the line below, create a variable named on_mars_right_now and assign it the boolean value of False
on_mars_right_now = False

assert on_mars_right_now == False, "If you see a Name Error, be sure to create the variable and assign it a value."
print("Exercise 1 is correct.")

Exercise 1 is correct.
[ ]
 # Exercise 2
# Create a variable named fruits and assign it a list of fruits containing the following fruit names as strings: 
# mango, banana, guava, kiwi, and strawberry.
fruits = ["mango", "banana", "guava", "kiwi", "strawberry"]

assert fruits == ["mango", "banana", "guava", "kiwi", "strawberry"], "If you see an Assert Error, ensure the variable contains all the strings in the provided order"
print("Exercise 2 is correct.")

Exercise 2 is correct.
[ ]
 # Exercise 3
# Create a variable named vegetables and assign it a list of fruits containing the following vegetable names as strings: 
# eggplant, broccoli, carrot, cauliflower, and zucchini
vegetables = ["eggplant", "broccoli", "carrot", "cauliflower", "zucchini"]

assert vegetables == ["eggplant", "broccoli", "carrot", "cauliflower", "zucchini"], "Ensure the variable contains all the strings in the provided order"
print("Exercise 3 is correct.")

Exercise 3 is correct.
[ ]
 # Exercise 4
# Create a variable named numbers and assign it a list of numbers, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

assert numbers == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "Ensure the variable contains the numbers 1-10 in order."
print("Exercise 4 is correct.")

Exercise 4 is correct.
List Operations
Hint Recommend finding and using built-in Python functionality whenever possible.
[ ]
 # Exercise 5
# Given the following assigment of the list of fruits, add "tomato" to the end of the list. 
fruits.append("tomato")

assert fruits == ["mango", "banana", "guava", "kiwi", "strawberry", "tomato"], "Ensure the variable contains all the strings in the right order"
print("Exercise 5 is correct")

Exercise 5 is correct
[ ]
 # Exercise 6
# Given the following assignment of the vegetables list, add "tomato" to the end of the list.
vegetables.append("tomato")

assert vegetables == ["eggplant", "broccoli", "carrot", "cauliflower", "zucchini", "tomato"], "Ensure the variable contains all the strings in the provided order"
print("Exercise 6 is correct")

Exercise 6 is correct
[ ]
 # Exercise 7
# Given the list of numbers defined below, reverse the list of numbers that you created above. 
numbers.reverse()

assert numbers == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], "Assert Error means that the answer is incorrect." 
print("Exercise 7 is correct.")

Exercise 7 is correct.
[ ]
 # Exercise 8
# Sort the vegetables in alphabetical order
vegetables.sort()

assert vegetables == ['broccoli', 'carrot', 'cauliflower', 'eggplant', 'tomato', 'zucchini']
print("Exercise 8 is correct.")

Exercise 8 is correct.
[ ]
 # Exercise 9
# Write the code necessary to sort the fruits in reverse alphabetical order
fruits.sort(reverse=True)

assert fruits == ['tomato', 'strawberry', 'mango', 'kiwi', 'guava', 'banana']
print("Exercise 9 is correct.")

Exercise 9 is correct.
[ ]
 # Exercise 10
# Write the code necessary to produce a single list that holds all fruits then all vegetables in the order as they were sorted above.
fruits_and_veggies = [*fruits, *vegetables]


assert fruits_and_veggies == ['tomato', 'strawberry', 'mango', 'kiwi', 'guava', 'banana', 'broccoli', 'carrot', 'cauliflower', 'eggplant', 'tomato', 'zucchini']
print("Exercise 10 is correct")

Exercise 10 is correct
Basic Functions
Hint Be sure to return values from your function definitions. The assert statements will call your function(s) for you.
[ ]
 # Run this cell in order to generate some numbers to use in our functions after this.
import random
    
positive_even_number = random.randrange(2, 101, 2)
negative_even_number = random.randrange(-100, -1, 2)

positive_odd_number = random.randrange(1, 100, 2)
negative_odd_number = random.randrange(-101, 0, 2)
print("We now have some random numbers available for future exercises.")
print("The random positive even number is", positive_even_number)
print("The random positive odd nubmer is", positive_odd_number)
print("The random negative even number", negative_even_number)
print("The random negative odd number", negative_odd_number)


We now have some random numbers available for future exercises.
The random positive even number is 82
The random positive odd nubmer is 89
The random negative even number -2
The random negative odd number -3
[ ]
 # Example function defintion:
# Write a say_hello function that adds the string "Hello, " to the beginning and "!" to the end of any given input.
def say_hello(name):
    return "Hello, " + name + "!"

assert say_hello("Jane") == "Hello, Jane!", "Double check the inputs and data types"
assert say_hello("Pat") == "Hello, Pat!", "Double check the inputs and data types"
assert say_hello("Astrud") == "Hello, Astrud!", "Double check the inputs and data types"
print("The example function definition ran appropriately")

The example function definition ran appropriately
[ ]
 # Another example function definition:
# This plus_two function takes in a variable and adds 2 to it.
def plus_two(number):
    return number + 2

assert plus_two(3) == 5
assert plus_two(0) == 2
assert plus_two(-2) == 0
print("The plus_two assertions executed appropriately... The second function definition example executed appropriately.")

The plus_two assertions executed appropriately... The second function definition example executed appropriately.
[ ]
 # Exercise 11
# Write a function definition for a function named add_one that takes in a number and returns that number plus one.
def add_one(numInput):
  return numInput + 1
    
assert add_one(2) == 3, "Ensure that the function is defined, named properly, and returns the correct value"
assert add_one(0) == 1, "Zero plus one is one."
assert add_one(positive_even_number) == positive_even_number + 1, "Ensure that the function is defined, named properly, and returns the correct value"
assert add_one(negative_odd_number) == negative_odd_number + 1, "Ensure that the function is defined, named properly, and returns the correct value"
print("Exercise 11 is correct.") 

Exercise 11 is correct.
[ ]
 # Exercise 12
# Write a function definition named is_positive that takes in a number and returns True or False if that number is positive.
def is_positive(numInput):
  if numInput > 0:
    return True
  else:
      return False

assert is_positive(positive_odd_number) == True, "Ensure that the function is defined, named properly, and returns the correct value"
assert is_positive(positive_even_number) == True, "Ensure that the function is defined, named properly, and returns the correct value"
assert is_positive(negative_odd_number) == False, "Ensure that the function is defined, named properly, and returns the correct value"
assert is_positive(negative_even_number) == False, "Ensure that the function is defined, named properly, and returns the correct value"
assert is_positive(0) == False, "Zero is not a positive number."
print("Exercise 12 is correct.")

Exercise 12 is correct.
[ ]
 # Exercise 13
# Write a function definition named is_negative that takes in a number and returns True or False if that number is negative.
def is_negative(numInput):
  if numInput < 0:
    return True
  else:
      return False

assert is_negative(positive_odd_number) == False, "Ensure that the function is defined, named properly, and returns the correct value"
assert is_negative(positive_even_number) == False, "Ensure that the function is defined, named properly, and returns the correct value"
assert is_negative(negative_odd_number) == True, "Ensure that the function is defined, named properly, and returns the correct value"
assert is_negative(negative_even_number) == True, "Ensure that the function is defined, named properly, and returns the correct value"
assert is_negative(0) == False, "Zero is not a negative number."
print("Exercise 13 is correct.")

Exercise 13 is correct.
[ ]
 # Exercise 14
# Write a function definition named is_odd that takes in a number and returns True or False if that number is odd.
def is_odd(numInput):
  if numInput %2 != 0:
    return True
  else:
    return False

assert is_odd(positive_odd_number) == True, "Ensure that the function is defined, named properly, and returns the correct value"
assert is_odd(positive_even_number) == False, "Ensure that the function is defined, named properly, and returns the correct value"
assert is_odd(negative_odd_number) == True, "Ensure that the function is defined, named properly, and returns the correct value"
assert is_odd(negative_even_number) == False, "Ensure that the function is defined, named properly, and returns the correct value"
print("Exercise 14 is correct.")

Exercise 14 is correct.
[ ]
 # Exercise 15
# Write a function definition named is_even that takes in a number and returns True or False if that number is even.
def is_even(numInput):
  if numInput %2 == 0:
    return True
  else:
    return False

assert is_even(2) == True, "Ensure that the function is defined, named properly, and returns the correct value"
assert is_even(positive_odd_number) == False, "Ensure that the function is defined, named properly, and returns the correct value"
assert is_even(positive_even_number) == True, "Ensure that the function is defined, named properly, and returns the correct value"
assert is_even(negative_odd_number) == False, "Ensure that the function is defined, named properly, and returns the correct value"
assert is_even(negative_even_number) == True, "Ensure that the function is defined, named properly, and returns the correct value"
print("Exercise 15 is correct.")

Exercise 15 is correct.
[ ]
 # Exercise 16
# Write a function definition named identity that takes in any argument and returns that argument's value. Don't overthink this one!
def identity (var):
  return var

assert identity(fruits) == fruits, "Ensure that the function is defined, named properly, and returns the correct value"
assert identity(vegetables) == vegetables, "Ensure that the function is defined, named properly, and returns the correct value"
assert identity(positive_odd_number) == positive_odd_number, "Ensure that the function is defined, named properly, and returns the correct value"
assert identity(positive_even_number) == positive_even_number, "Ensure that the function is defined, named properly, and returns the correct value"
assert identity(negative_odd_number) == negative_odd_number, "Ensure that the function is defined, named properly, and returns the correct value"
assert identity(negative_even_number) == negative_even_number, "Ensure that the function is defined, named properly, and returns the correct value"
print("Exercise 16 is correct.")

Exercise 16 is correct.
[ ]
 # Exercise 17
# Write a function definition named is_positive_odd that takes in a number and returns True or False if the value is both greater than zero and odd
def is_positive_odd(numInput):
  if numInput > 0 and numInput %2 != 0:
    return True
  else:
    return False

assert is_positive_odd(3) == True, "Double check your syntax and logic" 
assert is_positive_odd(positive_odd_number) == True, "Double check your syntax and logic"
assert is_positive_odd(positive_even_number) == False, "Double check your syntax and logic"
assert is_positive_odd(negative_odd_number) == False, "Double check your syntax and logic"
assert is_positive_odd(negative_even_number) == False, "Double check your syntax and logic"
print("Exercise 17 is correct.")

Exercise 17 is correct.
[ ]
 # Exercise 18
# Write a function definition named is_positive_even that takes in a number and returns True or False if the value is both greater than zero and even
def is_positive_even(numInput):
  if numInput > 0 and numInput %2 == 0:
    return True
  else:
    return False

assert is_positive_even(4) == True, "Double check your syntax and logic" 
assert is_positive_even(positive_odd_number) == False, "Double check your syntax and logic"
assert is_positive_even(positive_even_number) == True, "Double check your syntax and logic"
assert is_positive_even(negative_odd_number) == False, "Double check your syntax and logic"
assert is_positive_even(negative_even_number) == False, "Double check your syntax and logic"
print("Exercise 18 is correct.")

Exercise 18 is correct.
[ ]
 # Exercise 19
# Write a function definition named is_negative_odd that takes in a number and returns True or False if the value is both less than zero and odd.
def is_negative_odd(numInput):
  if numInput < 0 and numInput %2 != 0:
    return True
  else:
    return False

assert is_negative_odd(-3) == True, "Double check your syntax and logic" 
assert is_negative_odd(positive_odd_number) == False, "Double check your syntax and logic"
assert is_negative_odd(positive_even_number) == False, "Double check your syntax and logic"
assert is_negative_odd(negative_odd_number) == True, "Double check your syntax and logic"
assert is_negative_odd(negative_even_number) == False, "Double check your syntax and logic"
print("Exercise 19 is correct.")


Exercise 19 is correct.
[ ]
 # Exercise 20
# Write a function definition named is_negative_even that takes in a number and returns True or False if the value is both less than zero and even.
def is_negative_even(numInput):
  if numInput < 0 and numInput %2 == 0:
    return True
  else:
    return False

assert is_negative_even(-4) == True, "Double check your syntax and logic" 
assert is_negative_even(positive_odd_number) == False, "Double check your syntax and logic"
assert is_negative_even(positive_even_number) == False, "Double check your syntax and logic"
assert is_negative_even(negative_odd_number) == False, "Double check your syntax and logic"
assert is_negative_even(negative_even_number) == True, "Double check your syntax and logic"
print("Exercise 20 is correct.")

Exercise 20 is correct.
[ ]
 # Exercise 21
# Write a function definition named half that takes in a number and returns half the provided number.
def half(numInput):
  return numInput /2
  
assert half(4) == 2
assert half(5) == 2.5
assert half(positive_odd_number) == positive_odd_number / 2
assert half(positive_even_number) == positive_even_number / 2
assert half(negative_odd_number) == negative_odd_number / 2
assert half(negative_even_number) == negative_even_number / 2
print("Exercise 21 is correct.")

Exercise 21 is correct.
[ ]
 # Exercise 22
# Write a function definition named double that takes in a number and returns double the provided number.
def double(numInput):
  return numInput * 2

assert double(4) == 8
assert double(5) == 10
assert double(positive_odd_number) == positive_odd_number * 2
assert double(positive_even_number) == positive_even_number * 2
assert double(negative_odd_number) == negative_odd_number * 2
assert double(negative_even_number) == negative_even_number * 2
print("Exercise 22 is correct.")

Exercise 22 is correct.
[ ]
 # Exercise 23
# Write a function definition named triple that takes in a number and returns triple the provided number.
def triple(numInput):
  return numInput * 3

assert triple(4) == 12
assert triple(5) == 15
assert triple(positive_odd_number) == positive_odd_number * 3
assert triple(positive_even_number) == positive_even_number * 3
assert triple(negative_odd_number) == negative_odd_number * 3
assert triple(negative_even_number) == negative_even_number * 3
print("Exercise 23 is correct.")

Exercise 23 is correct.
[ ]
 # Exercise 24
# Write a function definition named reverse_sign that takes in a number and returns the provided number but with the sign reversed.
def reverse_sign(numInput):
  return numInput * -1

assert reverse_sign(4) == -4
assert reverse_sign(-5) == 5
assert reverse_sign(positive_odd_number) == positive_odd_number * -1
assert reverse_sign(positive_even_number) == positive_even_number * -1
assert reverse_sign(negative_odd_number) == negative_odd_number * -1
assert reverse_sign(negative_even_number) == negative_even_number * -1
print("Exercise 24 is correct.")

Exercise 24 is correct.
[ ]
 # Exercise 25
# Write a function definition named absolute_value that takes in a number and returns the absolute value of the provided number
def absolute_value(numInput):
  return abs(numInput) 

assert absolute_value(4) == 4
assert absolute_value(-5) == 5
assert absolute_value(positive_odd_number) == positive_odd_number
assert absolute_value(positive_even_number) == positive_even_number
assert absolute_value(negative_odd_number) == negative_odd_number * -1
assert absolute_value(negative_even_number) == negative_even_number * -1
print("Exercise 25 is correct.")

6
Exercise 25 is correct.
[ ]
 # Exercise 26
# Write a function definition named is_multiple_of_three that takes in a number and returns True or False if the number is evenly divisible by 3.
def is_multiple_of_three(numInput):
  if numInput % 3 == 0:
    return True
  else:
    return False

assert is_multiple_of_three(3) == True
assert is_multiple_of_three(15) == True
assert is_multiple_of_three(9) == True
assert is_multiple_of_three(4) == False
assert is_multiple_of_three(10) == False
print("Exercise 26 is correct.")

Exercise 26 is correct.
[ ]
 # Exercise 27
# Write a function definition named is_multiple_of_five that takes in a number and returns True or False if the number is evenly divisible by 5.
def is_multiple_of_five(numInput):
  if numInput % 5 == 0:
    return True
  else:
    return False

assert is_multiple_of_five(3) == False
assert is_multiple_of_five(15) == True
assert is_multiple_of_five(9) == False
assert is_multiple_of_five(4) == False
assert is_multiple_of_five(10) == True
print("Exercise 27 is correct.")

Exercise 27 is correct.
[ ]
 # Exercise 28
# Write a function definition named is_multiple_of_both_three_and_five that takes in a number and returns True or False if the number is evenly divisible by both 3 and 5.
def is_multiple_of_both_three_and_five(numInput):
  if numInput % 5 == 0 and numInput % 3 == 0:
    return True
  else:
    return False

assert is_multiple_of_both_three_and_five(15) == True
assert is_multiple_of_both_three_and_five(45) == True
assert is_multiple_of_both_three_and_five(3) == False
assert is_multiple_of_both_three_and_five(9) == False
assert is_multiple_of_both_three_and_five(4) == False
print("Exercise 28 is correct.")

Exercise 28 is correct.
[ ]
 # Exercise 29
# Write a function definition named square that takes in a number and returns the number times itself.
def square(numInput):
  return numInput ** 2
  
assert square(3) == 9
assert square(2) == 4
assert square(9) == 81
assert square(positive_odd_number) == positive_odd_number * positive_odd_number
print("Exercise 29 is correct.")

Exercise 29 is correct.
[ ]
 # Exercise 30
# Write a function definition named add that takes in two numbers and returns the sum.
def add(num1, num2):
  sum = num1 + num2
  return sum
  
assert add(3, 2) == 5
assert add(10, -2) == 8
assert add(5, 7) == 12
print("Exercise 30 is correct.")

Exercise 30 is correct.
[ ]
 # Exercise 31
# Write a function definition named cube that takes in a number and returns the number times itself, times itself.
def cube(numInput):
  return numInput ** 3

assert cube(3) == 27
assert cube(2) == 8
assert cube(5) == 125
assert cube(positive_odd_number) == positive_odd_number * positive_odd_number * positive_odd_number
print("Exercise 31 is correct.")

Exercise 31 is correct.
[ ]
 # Exercise 32
# Write a function definition named square_root that takes in a number and returns the square root of the provided number
import math
def square_root(numInput):
  return math.sqrt(numInput)

assert square_root(4) == 2.0
assert square_root(64) == 8.0
assert square_root(81) == 9.0
print("Exercise 32 is correct.")

Exercise 32 is correct.
[ ]
 # Exercise 33
# Write a function definition named subtract that takes in two numbers and returns the first minus the second argument.
def subtract(num1, num2):
  return num1 - num2

assert subtract(8, 6) == 2
assert subtract(27, 4) == 23
assert subtract(12, 2) == 10
print("Exercise 33 is correct.")

Exercise 33 is correct.
[ ]
 # Exercise 34
# Write a function definition named multiply that takes in two numbers and returns the first times the second argument.
def multiply(num1, num2):
  return  num1 * num2

assert multiply(2, 1) == 2
assert multiply(3, 5) == 15
assert multiply(5, 2) == 10
print("Exercise 34 is correct.")

Exercise 34 is correct.
[ ]
 # Exercise 35
# Write a function definition named divide that takes in two numbers and returns the first argument divided by the second argument.
def divide(num1, num2):
  return num1 / num2

assert divide(27, 9) == 3
assert divide(15, 3) == 5
assert divide(5, 2) == 2.5
assert divide(10, 2) == 5
print("Exercise 35 is correct.")

Exercise 35 is correct.
[ ]
 # Exercise 36
# Write a function definition named quotient that takes in two numbers and returns only the quotient from dividing the first argument by the second argument.
def quotient(num1, num2):
  return num1 // num2

assert quotient(27, 9) == 3
assert quotient(5, 2) == 2
assert quotient(10, 3) == 3
print("Exercise 36 is correct.")

Exercise 36 is correct.
[ ]
 # Exercise 37
# Write a function definition named remainder that takes in two numbers and returns the remainder of first argument divided by the second argument.
def remainder(num1, num2):
  return num1 % num2

assert remainder(3, 3) == 0
assert remainder(5, 2) == 1
assert remainder(7, 5) == 2
print("Exercise 37 is correct.")

Exercise 37 is correct.
[ ]
 # Exercise 38
# Write a function definition named sum_of_squares that takes in two numbers, squares each number, then returns the sum of both squares.
def sum_of_squares(num1, num2):
  #newNum1 = num1 ** 2
  #newNum2 = num2 ** 2
  return (num1**2) + (num2**2)

assert sum_of_squares(3, 2) == 13
assert sum_of_squares(5, 2) == 29
assert sum_of_squares(2, 4) == 20
print("Exercise 38 is correct.")

Exercise 38 is correct.
[ ]
 # Exercise 39
# Write a function definition named times_two_plus_three that takes in a number, multiplies it by two, adds 3 and returns the result.
def times_two_plus_three(num):
  return (num * 2) + 3
  
assert times_two_plus_three(0) == 3
assert times_two_plus_three(1) == 5
assert times_two_plus_three(2) == 7
assert times_two_plus_three(3) == 9
assert times_two_plus_three(5) == 13
print("Exercise 39 is correct.")

Exercise 39 is correct.
[ ]
 # Exercise 40
# Write a function definition named area_of_rectangle that takes in two numbers and returns the product.
def area_of_rectangle(num1, num2):
  return num1 * num2

assert area_of_rectangle(1, 3) == 3
assert area_of_rectangle(5, 2) == 10
assert area_of_rectangle(2, 7) == 14
assert area_of_rectangle(5.3, 10.3) == 54.59
print("Exercise 40 is correct.")

Exercise 40 is correct.
[ ]
 import math
# Exercise 41
# Write a function definition named area_of_circle that takes in a number representing a circle's radius and returns the area of the circl
def area_of_circle(r):
  area = math.pi * r * r
  return area

assert area_of_circle(3) == 28.274333882308138
assert area_of_circle(5) == 78.53981633974483
assert area_of_circle(7) == 153.93804002589985
print("Exercise 41 is correct.")

Exercise 41 is correct.
[ ]
 import math
# Exercise 42
# Write a function definition named circumference that takes in a number representing a circle's radius and returns the circumference.
def circumference(r):
  circum = math.pi * r * 2
  return circum 
  
assert circumference(3) == 18.84955592153876
assert circumference(5) == 31.41592653589793
assert circumference(7) == 43.982297150257104
print("Exercise 42 is correct.")

Exercise 42 is correct.
Functions working with strings
If you need some guidance working with the next few problems, recommend reading through this example code
[ ]
↳ 7 cells hidden
Accessing List Elements
[ ]
↳ 10 cells hidden
Functions to describe data
[ ]
↳ 5 cells hidden
Applying functions to lists
[ ]
 # Exercise 65
# Write a function definition named get_highest_number that takes in sequence of numbers and returns the largest number.
def get_highest_number(lst):
  return max(lst)
  
assert get_highest_number([1, 2, 3]) == 3
assert get_highest_number([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]) == 5
assert get_highest_number([-5, -3, 1]) == 1
print("Exercise 65 is correct.")

Exercise 65 is correct.
[ ]
 # Exercise 66
# Write a function definition named get_smallest_number that takes in sequence of numbers and returns the smallest number.
def get_smallest_number(lst):
  return min(lst)
  
assert get_smallest_number([1, 3, 2]) == 1
assert get_smallest_number([5, -5, -4, -3, -2, -1, 1, 2, 3, 4]) == -5
assert get_smallest_number([-4, -3, 1, -10]) == -10
print("Exercise 66 is correct.")

Exercise 66 is correct.
[ ]
 # Exercise 67
# Write a function definition named only_odd_numbers that takes in sequence of numbers and returns the odd numbers in a list.
def only_odd_numbers(lst):
  return [i for i in lst if i %2 != 0]
  
assert only_odd_numbers([1, 2, 3]) == [1, 3]
assert only_odd_numbers([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]) == [-5, -3, -1, 1, 3, 5]
assert only_odd_numbers([-4, -3, 1]) == [-3, 1]
assert only_odd_numbers([2, 2, 2, 2, 2]) == []
print("Exercise 67 is correct.")

Exercise 67 is correct.
[ ]
 # Exercise 68
# Write a function definition named only_even_numbers that takes in sequence of numbers and returns the even numbers in a list.
def only_even_numbers(lst):
  return [i for i in lst if i %2 == 0]

assert only_even_numbers([1, 2, 3]) == [2]
assert only_even_numbers([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]) == [-4, -2, 2, 4]
assert only_even_numbers([-4, -3, 1]) == [-4]
assert only_even_numbers([1, 1, 1, 1, 1, 1]) == []
print("Exercise 68 is correct.")

Exercise 68 is correct.
[ ]
 # Exercise 69
# Write a function definition named only_positive_numbers that takes in sequence of numbers and returns the positive numbers in a list.
def only_positive_numbers(lst):
  return [i for i in lst if i > 0]

assert only_positive_numbers([1, 2, 3]) == [1, 2, 3]
assert only_positive_numbers([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
assert only_positive_numbers([-4, -3, 1]) == [1]
print("Exercise 69 is correct.")

Exercise 69 is correct.
[ ]
 # Exercise 70
# Write a function definition named only_negative_numbers that takes in sequence of numbers and returns the negative numbers in a list.
def only_negative_numbers(lst):
  return [i for i in lst if i < 0]

assert only_negative_numbers([1, 2, 3]) == []
assert only_negative_numbers([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]) == [-5, -4, -3, -2, -1]
assert only_negative_numbers([-4, -3, 1]) == [-4, -3]
print("Exercise 70 is correct.")

Exercise 70 is correct.
[ ]
 # Exercise 71
# Write a function definition named has_evens that takes in sequence of numbers and returns True if there are any even numbers in the sequence
def has_evens(lst):
  for i in lst:
    if i %2 == 0:
      return True
    i += 1
  return False
  
assert has_evens([1, 2, 3]) == True
assert has_evens([2, 5, 6]) == True
assert has_evens([3, 3, 3]) == False
assert has_evens([]) == False
print("Exercise 71 is correct.")

Exercise 71 is correct.
[ ]
 # Exercise 72
# Write a function definition named count_evens that takes in sequence of numbers and returns the number of even numbers
def count_evens(lst):
  evenCount = 0
  for i in lst:
    if i % 2 == 0:
      evenCount += 1 
  return evenCount

assert count_evens([1, 2, 3]) == 1
assert count_evens([2, 5, 6]) == 2
assert count_evens([3, 3, 3]) == 0
assert count_evens([5, 6, 7, 8] ) == 2
print("Exercise 72 is correct.")

Exercise 72 is correct.
[ ]
 # Exercise 73
# Write a function definition named has_odds that takes in sequence of numbers and returns True if there are any odd numbers in the sequence
def has_odds(lst):
  for i in lst:
    if i %2 != 0:
      return True
    i += 1
  return False

assert has_odds([1, 2, 3]) == True
assert has_odds([2, 5, 6]) == True
assert has_odds([3, 3, 3]) == True
assert has_odds([2, 4, 6]) == False
print("Exercise 73 is correct.")

Exercise 73 is correct.
[ ]
 # Exercise 74
# Write a function definition named count_odds that takes in sequence of numbers and returns True if there are any odd numbers in the sequence
def count_odds(lst):
  oddCount = 0
  for i in lst:
    if i % 2 != 0:
      oddCount += 1 
  return oddCount

assert count_odds([1, 2, 3]) == 2
assert count_odds([2, 5, 6]) == 1
assert count_odds([3, 3, 3]) == 3
assert count_odds([2, 4, 6]) == 0
print("Exercise 74 is correct.")

Exercise 74 is correct.
[ ]
 # Exercise 75
# Write a function definition named count_negatives that takes in sequence of numbers and returns a count of the number of negative numbers
def count_negatives(lst):
  negative = 0
  for i in lst:
    if i < 0:
      negative += 1 
  return negative

assert count_negatives([1, -2, 3]) == 1
assert count_negatives([2, -5, -6]) == 2
assert count_negatives([3, 3, 3]) == 0
print("Exercise 75 is correct.")

Exercise 75 is correct.
[ ]
 # Exercise 76
# Write a function definition named count_positives that takes in sequence of numbers and returns a count of the number of positive numbers
def count_positives(lst):
  positive = 0
  for i in lst:
    if i > 0:
      positive += 1 
  return positive

assert count_positives([1, -2, 3]) == 2
assert count_positives([2, -5, -6]) == 1
assert count_positives([3, 3, 3]) == 3
assert count_positives([-2, -1, -5]) == 0
print("Exercise 76 is correct.")

Exercise 76 is correct.
[ ]
 # Exercise 77
# Write a function definition named only_positive_evens that takes in sequence of numbers and returns a list containing all the positive evens from the sequence
def only_positive_evens(lst):
  return [i for i in lst if i > 0 and i % 2 == 0]

assert only_positive_evens([1, -2, 3]) == []
assert only_positive_evens([2, -5, -6]) == [2]
assert only_positive_evens([3, 3, 4, 6]) == [4, 6]
assert only_positive_evens([2, 3, 4, -1, -5]) == [2, 4]
print("Exercise 77 is correct.")

Exercise 77 is correct.
[ ]
 # Exercise 78
# Write a function definition named only_positive_odds that takes in sequence of numbers and returns a list containing all the positive odd numbers from the sequence
def only_positive_odds(lst):
  return [i for i in lst if i > 0 and i % 2 != 0]

assert only_positive_odds([1, -2, 3]) == [1, 3]
assert only_positive_odds([2, -5, -6]) == []
assert only_positive_odds([3, 3, 4, 6]) == [3, 3]
assert only_positive_odds([2, 3, 4, -1, -5]) == [3]
print("Exercise 78 is correct.")

Exercise 78 is correct.
[ ]
 # Exercise 79
# Write a function definition named only_negative_evens that takes in sequence of numbers and returns a list containing all the negative even numbers from the sequence
def only_negative_evens(lst):
  return [i for i in lst if i < 0 and i % 2 == 0]

assert only_negative_evens([1, -2, 3]) == [-2]
assert only_negative_evens([2, -5, -6]) == [-6]
assert only_negative_evens([3, 3, 4, 6]) == []
assert only_negative_evens([-2, 3, 4, -1, -4]) == [-2, -4]
print("Exercise 79 is correct.")

Exercise 79 is correct.
[ ]
 # Exercise 80
# Write a function definition named only_negative_odds that takes in sequence of numbers and returns a list containing all the negative odd numbers from the sequence
def only_negative_odds(lst):
  return [i for i in lst if i < 0 and i % 2 != 0]

assert only_negative_odds([1, -2, 3]) == []
assert only_negative_odds([2, -5, -6]) == [-5]
assert only_negative_odds([3, 3, 4, 6]) == []
assert only_negative_odds([2, -3, 4, -1, -4]) == [-3, -1]
print("Exercise 80 is correct.")

Exercise 80 is correct.
[ ]
 # Exercise 81
# Write a function definition named shortest_string that takes in a list of strings and returns the shortest string in the list.
def shortest_string(lst):
  return min(lst, key = len)
  
assert shortest_string(["kiwi", "mango", "strawberry"]) == "kiwi"
assert shortest_string(["hello", "everybody"]) == "hello"
assert shortest_string(["mary", "had", "a", "little", "lamb"]) == "a"
print("Exercise 81 is correct.")

Exercise 81 is correct.
[ ]
 # Exercise 82
# Write a function definition named longest_string that takes in sequence of strings and returns the longest string in the list.
def longest_string(lst):
  return max(lst, key = len)

assert longest_string(["kiwi", "mango", "strawberry"]) == "strawberry"
assert longest_string(["hello", "everybody"]) == "everybody"
assert longest_string(["mary", "had", "a", "little", "lamb"]) == "little"
print("Exercise 82 is correct.")

Exercise 82 is correct.
Working with sets
Hint Take a look at the set function in Python, the set data type, and built-in set methods.
[ ]
 # Example set function usage
print(set("kiwi"))
print(set([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]))

{'w', 'i', 'k'}
{1, 2, 3, 4}
[ ]
 # Exercise 83
# Write a function definition named get_unique_values that takes in a list and returns a set with only the unique values from that list.
def get_unique_values(lst):
  for i in lst:
    return set(lst)

assert get_unique_values(["ant", "ant", "mosquito", "mosquito", "ladybug"]) == {"ant", "mosquito", "ladybug"}
assert get_unique_values(["b", "a", "n", "a", "n", "a", "s"]) == {"b", "a", "n", "s"}
assert get_unique_values(["mary", "had", "a", "little", "lamb", "little", "lamb", "little", "lamb"]) == {"mary", "had", "a", "little", "lamb"}
print("Exercise 83 is correct.")

Exercise 83 is correct.
[ ]
 # Exercise 84
# Write a function definition named get_unique_values_from_two_lists that takes two lists and returns a single set with only the unique values
def get_unique_values_from_two_lists (lst1, lst2):
  return set(lst1) | set(lst2)

assert get_unique_values_from_two_lists([5, 1, 2, 3], [3, 4, 5, 5]) == {1, 2, 3, 4, 5}
assert get_unique_values_from_two_lists([1, 1], [2, 2, 3]) == {1, 2, 3}
assert get_unique_values_from_two_lists(["tomato", "mango", "kiwi"], ["eggplant", "tomato", "broccoli"]) == {"tomato", "mango", "kiwi", "eggplant", "broccoli"}
print("Exercise 84 is correct.")

Exercise 84 is correct.
[ ]
 # Exercise 85
# Write a function definition named get_values_in_common that takes two lists and returns a single set with the values that each list has in common
def get_values_in_common (lst1, lst2):
  return set(lst1) & set(lst2)

assert get_values_in_common([5, 1, 2, 3], [3, 4, 5, 5]) == {3, 5}
assert get_values_in_common([1, 2], [2, 2, 3]) == {2}
assert get_values_in_common(["tomato", "mango", "kiwi"], ["eggplant", "tomato", "broccoli"]) == {"tomato"}
print("Exercise 85 is correct.")

Exercise 85 is correct.
[ ]
 # Exercise 86
# Write a function definition named get_values_not_in_common that takes two lists and returns a single set with the values that each list does not have in common
def get_values_not_in_common (lst1, lst2):
  return set(lst1)^set(lst2)

assert get_values_not_in_common([5, 1, 2, 3], [3, 4, 5, 5]) == {1, 2, 4}
assert get_values_not_in_common([1, 1], [2, 2, 3]) == {1, 2, 3}
assert get_values_not_in_common(["tomato", "mango", "kiwi"], ["eggplant", "tomato", "broccoli"]) == {"mango", "kiwi", "eggplant", "broccoli"}
print("Exercise 86 is correct.")

Exercise 86 is correct.
Working with Dictionaries
[ ]
 # Run this cell in order to have these two dictionary variables defined.
tukey_paper = {
    "title": "The Future of Data Analysis",
    "author": "John W. Tukey",
    "link": "https://projecteuclid.org/euclid.aoms/1177704711",
    "year_published": 1962
}

thomas_paper = {
    "title": "A mathematical model of glutathione metabolism",
    "author": "Rachel Thomas",
    "link": "https://www.ncbi.nlm.nih.gov/pubmed/18442411",
    "year_published": 2008
}
[ ]
 # Exercise 87
# Write a function named get_paper_title that takes in a dictionary and returns the title property
def get_paper_title(value):
  return value['title']

assert get_paper_title(tukey_paper) == "The Future of Data Analysis"
assert get_paper_title(thomas_paper) == "A mathematical model of glutathione metabolism"
print("Exercise 87 is correct.")

Exercise 87 is correct.
[ ]
 # Exercise 88
# Write a function named get_year_published that takes in a dictionary and returns the value behind the "year_published" key.
def get_year_published(value):
  return value['year_published']

assert get_year_published(tukey_paper) == 1962
assert get_year_published(thomas_paper) == 2008
print("Exercise 88 is correct.")

Exercise 88 is correct.
[ ]
 # Run this code to create data for the next two questions
book = {
    "title": "Genetic Algorithms and Machine Learning for Programmers",
    "price": 36.99,
    "author": "Frances Buontempo"
}
[ ]
 # Exercise 89
# Write a function named get_price that takes in a dictionary and returns the price
def get_price(value):
  return value['price']
  
assert get_price(book) == 36.99
print("Exercise 89 is complete.")

Exercise 89 is complete.
[ ]
 # Exercise 90
# Write a function named get_book_author that takes in a dictionary (the above declared book variable) and returns the author's name
def get_book_author(value):
  return value['author']

assert get_book_author(book) == "Frances Buontempo"
print("Exercise 90 is complete.")

Exercise 90 is complete.
Working with Lists of Dictionaries
Hint If you need an example of lists of dictionaries, see https://gist.github.com/ryanorsinger/fce8154028a924c1073eac24c7c3f409
[ ]
 # Run this cell in order to have some setup data for the next exercises
books = [
    {
        "title": "Genetic Algorithms and Machine Learning for Programmers",
        "price": 36.99,
        "author": "Frances Buontempo"
    },
    {
        "title": "The Visual Display of Quantitative Information",
        "price": 38.00,
        "author": "Edward Tufte"
    },
    {
        "title": "Practical Object-Oriented Design",
        "author": "Sandi Metz",
        "price": 30.47
    },
    {
        "title": "Weapons of Math Destruction",
        "author": "Cathy O'Neil",
        "price": 17.44
    }
]
[ ]
 # Exercise 91
# Write a function named get_number_of_books that takes in a list of objects and returns the number of dictionaries in that list.
def get_number_of_books(lst):
  return len([i for i in lst if isinstance(i, dict)])

assert get_number_of_books(books) == 4
print("Exercise 91 is complete.")

Exercise 91 is complete.
[ ]
 # Exercise 92
# Write a function named total_of_book_prices that takes in a list of dictionaries and returns the sum total of all the book prices added together
def total_of_book_prices(lst):
  total = 0
  for i in lst:
    total += i['price']
  return total

assert total_of_book_prices(books) == 122.9
print("Exercise 92 is complete.")

122.9
Exercise 92 is complete.
[ ]
 # Exercise 93
# Write a function named get_average_book_price that takes in a list of dictionaries and returns the average book price.
def get_average_book_price(lst):
  total = 0
  for i in lst:
    total += i['price']
  return total / len(lst)

assert get_average_book_price(books) == 30.725
print("Exercise 93 is complete.")

Exercise 93 is complete.
[ ]
 # Exercise 94
# Write a function called highest_price_book that takes in the above defined list of dictionaries "books" and returns the dictionary containing the title, price, and author of the book with the highest priced book.
# Hint: Much like sometimes start functions with a variable set to zero, you may want to create a dictionary with the price set to zero to compare to each dictionary's price in the list
def highest_price_book(lst):
  book = {'title': '', 'price': 0, 'author': ''}
  for i in range(len(lst)):
    if lst[i]['price'] > book['price']:
      book['title'] = lst[i]['title']
      book['price'] = lst[i]['price']
      book['author'] = lst[i]['author']
  return book

assert highest_price_book(books) == {
    "title": "The Visual Display of Quantitative Information",
    "price": 38.00,
    "author": "Edward Tufte"
}

print("Exercise 94 is complete")

Exercise 94 is complete
[ ]
 # Exercise 95
# Write a function called lowest_priced_book that takes in the above defined list of dictionaries "books" and returns the dictionary containing the title, price, and author of the book with the lowest priced book.
# Hint: Much like sometimes start functions with a variable set to zero or float('inf'), you may want to create a dictionary with the price set to float('inf') to compare to each dictionary in the list
def lowest_price_book(lst):
  book = {'title': '', 'price': float('inf'), 'author': ''}
  for i in range(len(lst)):
    if lst[i]['price'] < book['price']:
      book['title'] = lst[i]['title']
      book['price'] = lst[i]['price']
      book['author'] = lst[i]['author']
  return book

assert lowest_price_book(books) == {
    "title": "Weapons of Math Destruction",
    "author": "Cathy O'Neil",
    "price": 17.44
}
print("Exercise 95 is complete.")

Exercise 95 is complete.
[ ]
 shopping_cart = {
    "tax": .08,
    "items": [
        {
            "title": "orange juice",
            "price": 3.99,
            "quantity": 1
        },
        {
            "title": "rice",
            "price": 1.99,
            "quantity": 3
        },
        {
            "title": "beans",
            "price": 0.99,
            "quantity": 3
        },
        {
            "title": "chili sauce",
            "price": 2.99,
            "quantity": 1
        },
        {
            "title": "chocolate",
            "price": 0.75,
            "quantity": 9
        }
    ]
}
[ ]
 # Exercise 96
# Write a function named get_tax_rate that takes in the above shopping cart as input and returns the tax rate.
# Hint: How do you access a key's value on a dictionary? The tax rate is one key of the entire shopping_cart dictionary.
def get_tax_rate(lst):
  return lst['tax']
  
assert get_tax_rate(shopping_cart) == .08
print("Exercise 96 is complete")

Exercise 96 is complete
[ ]
 # Exercise 97
# Write a function named number_of_item_types that takes in the shopping cart as input and returns the number of unique item types in the shopping cart. 
# We're not yet using the quantity of each item, but rather focusing on determining how many different types of items are in the cart.
def number_of_item_types(lst):
  return len(lst['items'])
  
assert number_of_item_types(shopping_cart) == 5
print("Exercise 97 is complete.")

Exercise 97 is complete.
[ ]
 # Exercise 98
# Write a function named total_number_of_items that takes in the shopping cart as input and returns the total number all item quantities.
# This should return the sum of all of the quantities from each item type
def total_number_of_items(lst):
  total = 0 
  for i in range(len(lst['items'])):
    total += lst['items'][i]["quantity"]
  return total
  
assert total_number_of_items(shopping_cart) == 17
print("Exercise 98 is complete.")

Exercise 98 is complete.
[ ]
 # Exercise 99
# Write a function named get_average_item_price that takes in the shopping cart as an input and returns the average of all the item prices.
# Hint - This should determine the total price divided by the number of types of items. This does not account for each item type's quantity.
def get_average_item_price(lst):
  total = 0 
  for i in range(len(lst['items'])):
    total += lst['items'][i]["price"]
  return total / len(lst['items'])

assert get_average_item_price(shopping_cart) == 2.1420000000000003
print("Exercise 99 is complete.")

Exercise 99 is complete.
[ ]
 # Exercise 100
# Write a function named get_average_spent_per_item that takes in the shopping cart and returns the average of summing each item's quanties times that item's price.
# Hint: You may need to set an initial total price and total total quantity to zero, then sum up and divide that total price by the total quantity
def get_average_spent_per_item(lst):
  totalQuantity = 0
  totalPrice = 0

  for i in range(len(lst['items'])):
    totalQuantity += lst['items'][i]["quantity"]
    
  for i in range(len(lst['items'])):
    totalPrice += lst["items"][i]["price"] * lst["items"][i]["quantity"]

  return totalPrice / totalQuantity

assert get_average_spent_per_item(shopping_cart) == 1.333529411764706
print("Exercise 100 is complete.")

Exercise 100 is complete.
[ ]
 # Exercise 101
# Write a function named most_spent_on_item that takes in the shopping cart as input and returns the dictionary associated with the item that has the highest price*quantity.
# Be sure to do this as programmatically as possible. 
# Hint: Similarly to how we sometimes begin a function with setting a variable to zero, we need a starting place:
# Hint: Consider creating a variable that is a dictionary with the keys "price" and "quantity" both set to 0. You can then compare each item's price and quantity total to the one from "most"
lst = shopping_cart

def most_spent_on_item(lst):
    item = {'title': '', 'price': 0, 'quantity': 0}
    for i in range(len(lst["items"])):
        totalPrice = lst["items"][i]["quantity"] * lst["items"][i]["price"]
        if totalPrice > item["price"]:
            item["title"] = lst["items"][i]["title"]
            item["price"] = lst["items"][i]["price"]
            item["quantity"] = lst["items"][i]["quantity"]
    return item

print (most_spent_on_item(lst))

assert most_spent_on_item(shopping_cart) == {
    "title": "chocolate",
    "price": 0.75,
    "quantity": 9
}
print("Exercise 101 is complete.")

{'title': 'chocolate', 'price': 0.75, 'quantity': 9}
Exercise 101 is complete.
Created by Ryan Orsinger
Source code on https://github.com/ryanorsinger/101-exercises
