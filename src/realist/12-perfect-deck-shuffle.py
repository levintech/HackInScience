def perfect_shuffle(deck):
    shuffled_deck = []
    length = len(deck)
    for card_index in range(int(length / 2)):
        shuffled_deck.append(deck[card_index])
        shuffled_deck.append(deck[int(length / 2) + card_index])
    
    return shuffled_deck
        