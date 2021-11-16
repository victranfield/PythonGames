import copy
import random

# We want to create some constants or fixed values to help with the game
# This makes the code easier to read, and avoid spelling mistakes

# So for white and black, this will highlight an issue if you write "balck"
white = "white"
black = "black"
# Using the variable gives mean when you read the code and makes it easier to change.
# so if your code read number_of_chips less than 15 what does this mean, number_of_chips less then total_chips
total_chips = 15
middle_of_board = 13
# Again we need to find the home, start and middle for white and black, this gives more meaning when you read the code
# reading numbers is difficult to understand
home = {white:25, black:0}
start = {white:0, black:25}
middle = {white:26, black:27} # We need to record white/black chips moved off the board

# Create initial setup board
# We have a fixed number of columns that can either be white or black
# A data structure to store the board could be a list
# For each element we need to store the colour and number of chips
initial_board = [[None, 0],
                [white, 2], [None, 0], [None, 0], [None, 0], [None, 0], [black, 5],
                [None, 0], [black, 3], [None, 0], [None, 0], [None, 0], [white, 5],
                [black, 5], [None, 0], [None, 0], [None, 0], [white, 3], [None, 0],
                [white, 5], [None, 0], [None, 0], [None, 0], [None, 0], [black, 2],
                [None, 0],
                [None, 0],
                [None, 0]
               ]

def display_middle_board(board):
    print()
    print()
    if board[middle[white]][1] > 0 or board[middle[black]][1] > 0:
        print("Middle has ", board[middle[white]][1], " white chips in the middle please type", middle[white])
        print("Middle has ", board[middle[black]][1], " black chips in the middle please type", middle[black])
        print()

def display_counter_index(start_point, end_point):
    for counter in range(start_point, end_point):
        if counter == start_point + ((end_point - start_point) // 2):
            print("  ", end="")
        if counter >= 10:
            print("    " + str(counter) + "  ", end="")
        else:
            print("   " + str(counter) + "    ", end="")
    print()

# We want to keep one thing together so we display_board
# This method could do with refactoring and improving
def display_board(board):
    for counter, point in enumerate(board):

        # Create a new line if on the second half
        # We also add any chips in the middle
        if counter == middle_of_board:
            display_middle_board(board)
            display_counter_index(middle_of_board, home[white])

        # We create a divide for the mid part of the game
        # The equation is probably excessive and hardcoded values would be better,
        # but it means if the board changes it still works
        if (counter == ((middle_of_board - home[black])//2)+1) or (counter == middle_of_board + ((home[white]-middle_of_board)//2)):
            print("||", end =" ")

        if counter == 0:
            print("Black Home has", point[1])
            display_counter_index(home[black]+1, middle_of_board)
        elif counter == 25:
            print()
            print("White Home has", point[1])
            print()
        elif counter < 25:
            # To make the length of colour so the counter matches up we add a space to None
            if point[0] == None:
                colour = "None "
            else:
                colour = point[0]
            print(colour, point[1], end=" ")



def throw_a_die():
    return random.randint(1, 6)

def throw_dice():
    dice = []
    dice.append(throw_a_die())
    dice.append(throw_a_die())
    # If we roll the same dice the player gets four moves
    if dice[0] == dice[1]:
        dice.append(dice[0])
        dice.append(dice[0])

    return dice

def display_dice(dice, colour):
    print(colour + " rolled:")
    for die in dice:
        print(die)

def get_player_int(request):
    #Initialise the answer we wil get from the user to a string so we enter the while loop
    answer = " "
    #A while loop that will continue
    #not answer.isdigit() is not (is answer a digit) so while a strong like "s" is entered the while will continue
    #As soon as the player enters an integer the while loop stops
    while not (answer.isdigit() or (len(answer) > 1 and answer[0] == "-" and answer[1:].isdigit())):
        #The request string provided is prompted to the user for them to input there answer
        #We store the value entered by the player in the variable answer
        answer = input(request)

    #Return the answer after it is converted to an intger int()
    return int(answer)

def request_integer_from_player(request):
    valid = False
    while not valid:
        try:
            answer_as_string = input(request)
            answer_as_integer = int(answer_as_string)
            valid = True
        except ValueError:
            print("Please enter an integer")
    return answer_as_integer

def get_player_die_to_move(colour, dice):
    number_of_moves = request_integer_from_player("Please enter number of spaces to move for " + colour)
    # We want to check the player enters one of the die
    while number_of_moves not in dice:
        print("Please select from", dice)
        number_of_moves = request_integer_from_player("Please enter number of spaces to move for " + colour)
    return number_of_moves

def get_player_position(colour):
    point_to_move_from = request_integer_from_player("Please enter position to move for " + colour)
    while not (point_to_move_from <= middle[black]):
        print("Postion does not exist, please try again")
        point_to_move_from = request_integer_from_player("Please enter position to move for " + colour)
    return point_to_move_from

def request_player_move(colour, dice):
    number_of_moves = 0
    point_to_move_from = get_player_position(colour)
    # A negative point_to_move_from indicates the players wants to stop
    if point_to_move_from >= 0:
        number_of_moves = get_player_die_to_move(colour, dice)
    return point_to_move_from, number_of_moves

# Determine the direction of the move
# White moves forward
# Balck moves back so we subtract
def determine_new_position(colour, point_to_move_from, number_of_moves):
    # Determine the direction of the move
    # White moves forward
    # Balck moves back so we subtract
    
    #If we are in the middle we need to reset
    if point_to_move_from == middle[colour]:
        point_to_move_from = start[colour]

    # If the move is beyond, further, than home we make it home
    if colour == white:
        new_position = point_to_move_from + number_of_moves
        if new_position > home[colour]:
            new_position = home[colour]
    else: 
        new_position = point_to_move_from - number_of_moves
        if new_position < home[colour]:
            new_position = home[colour]

    return new_position

def die_exists(dice, number_of_moves):
    return number_of_moves in dice

def validate_point_to_move_from(current_board, colour, point, silent ):
    valid = True
    if not point <= middle[colour]:
        if not silent:
            print("Point is too large")
        valid = False
    elif not current_board[point][0] == colour:
        if not silent:
            print("Position to move from not your colour")
        valid = False
    elif not current_board[point][1] > 0:
        if not silent:
            print("Position to mover from does not have sufficient chips")
        valid = False
    elif current_board[middle[colour]][1]> 0 and not point == middle[colour]:
        if not silent:
            print("You have chips in the middle, please play these first")
        valid = False

    return valid

def all_in_home(current_board, colour):
    total = 0
    # We need to create a direction for the range, since home is zero for black and 25 for white
    # So for white we go backwards
    direction = 1
    if colour == white:
        direction = -1

    for counter in range(home[colour], determine_new_position(colour, home[colour], -7), direction):
        if current_board[counter][0] == colour:
            total += current_board[counter][1]
    return total == total_chips

# We need to validate the point to move to
def validate_point_to_move_to(current_board, colour, point, silent ):
    valid = True
    if current_board[point][0] != colour and current_board[point][0] != None and not current_board[point][1] == 1:
        if not silent:
            print("Position is not your colour and has more than one chip")
        valid = False
    elif not (current_board[point][0] == colour or current_board[point][0] == None or current_board[point][1] == 1):
        if not silent:
            print("Position to move to is not your colour or no colour")
        valid = False
    elif point%25 == 0 and not all_in_home(current_board, colour):
        if not silent:
            print("Not able to move off the board till all chips are home")
        valid = False
    return valid

def valid_player_instructions(current_board, colour, dice, point_to_move_from, number_of_moves, silent=False):
    # Assume it is valid
    # We can then have a number of nots to check if valid and set not with feedback
    valid = True
    if not die_exists(dice, number_of_moves):
        print("Die does not exist")
        valid = False
        
    if not validate_point_to_move_to(current_board, colour, determine_new_position(colour, point_to_move_from, number_of_moves), silent):
        valid = False
        
    if not validate_point_to_move_from(current_board, colour, point_to_move_from, silent):
        valid = False
        
    return valid

def player_can_move(current_board, colour, dice):
    can_move = False
    counter = 0
    # We use a while so we can exit once the player can move, this is faster than doing a for every move
    while counter < len(current_board):
        if current_board[counter][0] == colour:
            for die in dice:
                if valid_player_instructions(current_board, colour, dice, counter, die, True):
                    can_move = True
        counter += 1
    return can_move

def valid_player_round(current_board, colour, dice):
    valid = False
    point_to_move_from, number_of_moves = request_player_move(colour, dice)
    while point_to_move_from >= 0 and not valid and player_can_move(current_board, colour, dice):
        if valid_player_instructions(current_board, colour, dice, point_to_move_from, number_of_moves):
            valid = True
        else:
            print("Please try again")
            point_to_move_from, number_of_moves = request_player_move(colour, dice)
    
    return point_to_move_from, number_of_moves
    
def make_player_move(current_board, colour, point_to_move_from, number_of_moves):
    #Decrement chip from position to move from
    position_from_count = current_board[point_to_move_from][1]-1
    position_from_colour = colour
    if position_from_count == 0:
        position_from_colour = None
    current_board[point_to_move_from] = [position_from_colour, position_from_count]
    # Determine the direction of the move
    # White moves forward
    # Black moves back so we subtract
    new_position = determine_new_position(colour, point_to_move_from, number_of_moves)
    original_colour = current_board[new_position][0]
    if current_board[new_position][0] != None and current_board[new_position][0] != colour:
        current_board[middle[original_colour]] = [original_colour, current_board[middle[original_colour]][1] + 1]
        current_board[new_position][1] = 0
    current_board[new_position] = [colour, current_board[new_position][1]+1]
    return current_board

def player_round(current_board, colour, dice):
    point_to_move_from = 0
    # We don't know how many dice they have or if the try to exit with a negative point_to_move_from
    # So we need a conditional while to loop
    while len(dice) > 0 and point_to_move_from >= 0:
        point_to_move_from, number_of_moves = valid_player_round(current_board, colour, dice)
        current_board = make_player_move(current_board, colour, point_to_move_from, number_of_moves)
        display_board(current_board)
        if point_to_move_from >= 0:
            dice.remove(number_of_moves)
    return current_board, point_to_move_from
        
def play_game(current_board, colour):
    dice = throw_dice()
    print("New turn for", colour)
    display_board(current_board)
    display_dice(dice, colour)
    if player_can_move(current_board, colour, dice):
        current_board, points_to_move_from = player_round(current_board, colour, dice)
    else:
        print(colour + " has no moves")
        points_to_move_from = 0
    return current_board, points_to_move_from 
        
def main():
    # We need to make a deep copy or whe we change the current_board we will also change the initial_board
    # It is a memory address to the same list
    current_board = copy.deepcopy(initial_board)
    points_to_move_from = 0
    print("To exit enter a negative position to move from")
    # We need to iterate to keep till one player has all chips home or someone tries to exit with a negative point_to_move_from
    # So we need to iterate with a while since it is conditional
    while (current_board[home[white]][1] != total_chips and current_board[home[black]][1] != total_chips) and points_to_move_from >=0:
        current_board, points_to_move_from = play_game(current_board, white)
        if points_to_move_from >= 0:
            current_board, points_to_move_from = play_game(current_board, black)
        
if __name__ == "__main__":
    main()
