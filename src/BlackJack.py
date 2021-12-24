import random
from src.PlayingCard import *
from src.ConsoleInput import ConsoleInput
from src.ConsoleOutput import ConsoleOutput

"""Constant values to be references in the functions and methods below."""
winning_score = 21
face_card_score = 10
max_ace_score = 11
min_ace_score = 1
good_number_of_cards = 5
game_input = ConsoleInput()
game_output = ConsoleOutput()

def set_game_input(new_input):
    global game_input
    game_input = new_input

def score_hand(hand):
    """Score an individual hand of playing cards. We add each card score to a total. All face cards King, Queen
 and Jack score ten. If the hand has an ace we can score at one or eleven. If the hand is less than or equal to eleven
 then ten additional score is added on (one already been added and the score for the ace is eleven)"""
    total_score = 0
    has_an_ace = False
    convert_faces_to_numbers(hand)
    for card in hand:
        if int(card[1:len(card)]) == min_ace_score:
            has_an_ace = True
        if int(card[1:len(card)])  > face_card_score: #Face cards i.e. King, Queen and Jack
            total_score += face_card_score
        else:
            total_score += int(card[1:len(card)])
    convert_numbers_to_faces(hand)
    if total_score > winning_score:
        total_score = 0
    elif has_an_ace and total_score <= max_ace_score:
        total_score += max_ace_score - min_ace_score

    return total_score

def deal_to_player(deck, hand):
    """Deal a card to a player from the deck. The score is then checked and if the have a score above 21 they
 get a score of 0. We return True if they are still below 21 or False if the score goes above i.e. when it is zero."""
    player_good = False
    hand.append(deal_a_card(deck))
    if score_hand(hand) > 0:
        player_good = True
    return player_good

def valid_deal_input():
    """Get an input of "D"eal or "S"tick from the user, validates only "D" or "S" has been entered and the
 returns the answer in upper case. A while loop is used to prompt the user till the enter a valid response"""
    """Function to get a valid user input for the deal_to_user function"""
    allowed_answers = ["D", "S"]
    answer = game_input.get_string("Please select (D)raw or (S)tick: ")
    while answer.upper() not in allowed_answers:
        answer = game_input.get_string("That is not a valid input. Please select (D)raw or (S)tick: ")
    return answer.upper()

def deal_to_user(deck, hand):
    """The user will be displayed their hand and can either request to be dealt a new card from the deck or they
 can stick so stop and move on. When you are dealt a card we determine the score, if you go over the limit 21 you loose
 and are bust. In this case we move on."""
    answer = "D"
    while answer == "D":
        game_output.display("Your hand is")
        game_output.display(hand)
        answer = valid_deal_input()
        if answer == "D":
            if not deal_to_player(deck, hand):
                answer = "F"
                game_output.display(f"Sorry you have gone over the score and are bust {hand}")


def find_winner(hands):
    """Go through each of the hands and determine the score. If the score is better than the previous score we
 replace the previous score, so we only store the highest score so far. If we have a draw both players are added to
 the to the previous player list. To determine a winner if you have the same score you win if you have five cards."""
    previous_player = []
    previous_hand = []
    previous_score = 0

    for counter in range(0, len(hands)):
        current_score = score_hand(hands[counter])
        if previous_score < current_score or (previous_score == current_score and (len(hands[counter])==good_number_of_cards and len(previous_hand) != good_number_of_cards)):
            previous_player = [counter]
            previous_hand = hands[counter]
            previous_score = current_score
        elif previous_score == current_score:
            previous_player.append(counter)


    return previous_player

def initialise_computer_risk(number_of_player):
    """The  function determines the risk for each computer player. The risk is determined by getting a random
 number. So if there risk level is nine they will stick if the have a score of twelve or above i.e. 21 minus risk
 level. If they have nine they will request an additional card."""
    computer_risk = {}
    for counter in range(1, number_of_player):
        computer_risk[counter] = random.randint(2, 9)
    return computer_risk

def deal_to_computer(deck, hands, computer_risk):
    """The computer will have a risk, the number on or above they will stick at i.e. not ask for more cards. So
 if there risk level is nine they will stick if the have a score of twelve or above. If they have nine they will request an
 additional card. One gap is the computer does not know if they have an Ace. If the have an ace it could be sensible to
 request another card, this would require a second risk level for when you have an Ace."""
    for counter in computer_risk.keys():
        score = score_hand(hands[counter])
        while score > 0 and score + computer_risk[counter] < winning_score and len(deck) >0:
            result = deal_to_player(deck, hands[counter])
            score = score_hand(hands[counter])

def black_jack(deck, hands, computer_risk):
    """The Black Jack method is passed a deck of playing cards, a starting deal of two cards each and the level
 of risk for the computer. The cards need to add up to 21 or less. If you go above 21 you are bust (loose). First the
 user has the opportunity to request more cards to be dealt, one at a time. The computer will have a risk, the number
 on or above they will stick at i.e. not ask for more cards. Once all the cards have been dealt we determine the winner
 i.e. the closest to 21."""
    deal_to_user(deck, hands[user_hand])
    deal_to_computer(deck, hands, computer_risk)
    players = find_winner(hands)
    if len(players) == 1:
        game_output.display("Player " + str(players[0]) + " is the winner")
    else:
        for player in players:
            game_output.display("Player " + str(player) + " draw")
    game_output.display(hands)

def main():
    """"Get the number of players, generate the deck of cards and work out the computer players risk."""
    number_of_players = int(game_input.get_string("Please enter the number of players, max is six"))
    deck = generate_deck()
    deck = shuffle_cards(deck)
    hands = deal_cards(deck, 2, number_of_players)
    computer_risk = initialise_computer_risk(number_of_players)
    black_jack(deck, hands, computer_risk)

# This allows the main to be called only when you run this file.
if __name__ == "__main__":
    main()


