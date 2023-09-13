import itertools
import time 

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

suits = ["heart", "diamond", "club", "spade"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king", "ace"]

deck = []
for rank in ranks:
    for suit in suits:
        card = Card(rank, suit)
        deck.append(card)

hands = list(itertools.combinations(deck, 5))

def check_royal_flush(hand):
    royal_flush = ["10", "jack", "queen", "king", "ace"]
    previous_card_suit = None
    suits_match = True


    m = 0
    for card in hand:
        if previous_card_suit == None:
            previous_card_suit = card.suit

        if card.rank in royal_flush:
            if card.suit == previous_card_suit:
                m += 1
            else:
                suits_match = False
                break
        else:
            break
    
    if m == 5 and suits_match:
        return True
    else:
        return False
    

total_royal_flush = 0
for hand in hands:
    if check_royal_flush(hand):
        total_royal_flush += 1

print("Total Royal Flush", total_royal_flush)