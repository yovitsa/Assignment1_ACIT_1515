# def get_menu() -> list[tuple[int, str]]:
#     """ Generate a menu for the user (4 MARKS)
#     Arguments:
#         None
#     Returns:
#         An enumerated list of strings, 1-based (i.e. the op)
#     """


#     # create a list of 5 strings: 'List Grades', 'Check Average', 'Check Status', 'Change Grade', 'Exit'
#     menu = ["List Grades","Check Average","Check Status", "Change Grade", "Exit"]
    
#     # enumerate (starting at 1) and return the list
#     return list(enumerate(menu, 1))
# print(get_menu())
import random
def validate_choice(choice: int) -> int:
    """ Validate the user's choice
    Arguments:
        choice: a string representation of a number
    Returns:
        A number (between 0 and 5)
    """
    
    # if choice is between 1 and 5, return the choice, otherwise return 0
    choice = random.randint(0,5)
    
    
    if choice in range(1,5):
        return True
    else: False
    return choice   

print(validate_choice())

