import random

play_again = "y"
points = 300


class GameRunner:
    def get_inputs():
        hi_or_lo = input("Higher or Lower? [h/l] ")   
        while hi_or_lo != "h" and hi_or_lo != "l":
            hi_or_lo = input("Input not recognized, enter h or l: ")
        return hi_or_lo
    
    def play_again():
        yn = input("Play again [y/n] ")   
        while yn != "y" and yn != "n":
            yn = input("Input not recognized, [y/n] ")
        return yn

    def print_score(points):
        print(f"Your score is: {score}")

    def win_determination(deck, score, choice):
        if deck[0] > deck[1] and choice == "h":
            print(f"Next card was {deck[1]}")
            score = score - 75
        if deck[0] < deck[1] and choice == "h":
            print(f"Next card was {deck[1]}")
            score = score + 100
        if deck[0] < deck[1] and choice == "l":
            print(f"Next card was {deck[1]}")
            score = score - 75
        if deck[0] > deck[1] and choice == "l":
            print(f"Next card was {deck[1]}")
            score = score +100
        return score

    def print_score(points):
        print(points)

class Deck:
    def new_cards():
        deck = []
        card = random.randint(1,13)
        next_card = random.randint(1,13)
        while card == next_card:
            card = random.randint(1,13)
            next_card = random.randint(1,13)
        deck.append(card)
        deck.append(next_card)
        return deck

    


while play_again == "y":
    deck = Deck.new_cards()
    print(f"Your Card is {deck[0]}")
    choice = GameRunner.get_inputs()
    score = GameRunner.win_determination(deck, points, choice)
    points = score
    GameRunner.print_score(score)
    if points <= 0:
        print(f"You lose!")
        break
    play_again = GameRunner.play_again()
