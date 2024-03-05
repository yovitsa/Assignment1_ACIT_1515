"""
Assignment 1: Grades Generator
------------------------------

Assignment 1 is designed to test your understanding of the skills practiced in weeks 1 through 4:
- creating variables using Python's built-in data types
- converting and checking data types 
- using built-in functions
- using conditional statements and loops
- writing custom functions

For assignment 1 you will be writing a script that generates random grades and allows you to:
    a). View your randomly generated grades
    b). Get the average of your randomly generated grades
    c). Report your pass/fail status (i.e. if the average is above 50, you are passing. If the average is below 50 you are not yet passing)
    d). Change a grade
    e). Quit

The script will consist of several functions, each of which has a placeholder below with instructions.

NOTE: all input (getting choices from the user) and output (printing to the console) MUST occur inside the if __name__ == '__main__' block. 

The functions (generate_grade, generate_grades, get_menu, validate_choice, get_average, get_status, and change_grade) *MUST NOT* contain any print() or input() statements
"""

import random
import sys

def generate_grade() -> int:
    """ Generate a grade (1 MARK)
    Arguments:
        None
    Returns:
        A random integer between 0 and 100
    """
    return random.randint(0,100)

    

def generate_grades() -> list[int]:
    """ Generate a list of grades (3 MARKS)
    Arguments:
        None
    Returns:
        A list of 7 random grades, created by calling the generate_grade() function seven times in a loop
    """
    grades = []

    for grade in range(7):
        grade = random.randint(0,100)
        grades.append(grade)
    return grades

  

def get_menu() -> list[tuple[int, str]]:
    """ Generate a menu for the user (4 MARKS)
    Arguments:
        None
    Returns:
        An enumerated list of strings, 1-based (i.e. the op)

    """
    menu = [(1, "List Grades"),(2, "Check Average"),(3, "Check Status"), (4, "Change Grade"), (5, "Exit")]


    # create a list of 5 strings: 'List Grades', 'Check Average', 'Check Status', 'Change Grade', 'Exit'
    
    
    # enumerate (starting at 1) and return the list
    return list(enumerate(menu, 1))
    
   

def validate_choice(choice: int) -> int:
    """ Validate the user's choice
    Arguments:
        choice: a string representation of a number
    Returns:
        A number (between 0 and 5)
    """

    
    # if choice is between 1 and 5, return the choice, otherwise return 0
    
    if choice >= 1 and choice <= 5:
        return choice
    
    # if choice in range(1,6):
    #     return choice 
    # else: 
    #     return 0
    

def get_average(grades: list[int]) -> int | float:
    """ Get the average of a list of grades
    Arguments:
        grades: a list of integers
    Returns:
        The mean (average) of the list
    """
    
    if not grades:
        return 0.0
    
    grades_total = sum(grades)
    
    grades_number = len(grades)

    average_grade = grades_total / grades_number

    return average_grade

    

def get_status(grades: list[int]) -> bool:
    """ Get the passing status, based on the average of grades
    Arguments:
        grades: a list of integers
    Returns:
        True if average is greater than or equal to 50, otherwise False
    """

    
    # call the get_average() function and check if average is greater than or equal to 50
    average_grade = get_average(grades)

    if average_grade >= 50:
        return True
    else:
        False

    # if so, return True, otherwise return False
    
    
    
def change_grade(grades: list[int], grade: int, new_value: int) -> list[int]:
    """ Change a grade to a new valid value
    Arguments:
        grades: a list of integers
        grade: the numeric position in the list of the grade to change
        new_value: an integer between 0 and 100
    Returns:
        The updated list of integers
    """        
    
    # if the new value is valid, silently (no print() statements) update the grade and return the list
    if  0 <= new_value <= 100:
        if 1 <= grade <= len(grades):
            grades[grade - 1] = new_value
    # if the new grade is not valid, silently return the list without updating the grade
    return grades
   
        
if __name__ == "__main__":
    # call the generate_grades() function and store the result in variable
    grades = generate_grades()  # Generate initial list of grades

    while True:
        print("\nMenu:")
        for number, option in get_menu():
            print(f"{number}. {option[1]}")  # Display menu options correctly

        user_input = input('Please choose an option from the menu: ')
        if user_input.isdigit():  # Check if input is a digit
            choice = int(user_input)
            choice = validate_choice(choice)  # Validate the user's choice
        else:
            print("Invalid input. Please enter a number.")
            continue
        
        if choice == 0:
            print('Invalid choice. Please choose a number between 1 and 5.')
            continue
        
        if choice == 1:
            print(f'Your grades are: {grades}')
        
        elif choice == 2:
            average_grade = get_average(grades)
            print(f"Your average grade is: {average_grade:.2f}")
        
        elif choice == 3:
            status = get_status(grades)
            if status:
                print("Congratulations, you are passing the course!")
            else:
                print("Unfortunately, you will have to retake this course.")
        
        elif choice == 4:
            for index, grade in enumerate(grades, 1):
                print(f"{index}. Grade: {grade}")
            grade_index_input = input("Which grade number would you like to change? ")
            new_grade_input = input("Enter the new grade (0-100): ")
            
            if grade_index_input.isdigit() and new_grade_input.isdigit():
                grade_index = int(grade_index_input)
                new_grade = int(new_grade_input)
                
                if 0 < grade_index <= len(grades) and 0 <= new_grade <= 100:
                    grades = change_grade(grades, grade_index, new_grade)
                    print("Grade updated successfully.")
                else:
                    print("Invalid grade number or new grade value.")
            else:
                print("Invalid input. Please enter valid numbers.")
        
        elif choice == 5:
            print("Exiting program.")
            break
            
