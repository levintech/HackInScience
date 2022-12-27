def missing_card(cards):
    card_colors = ["S", "H", "D", "C"]
    card_values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    
    full_cards = []
    
    for color in card_colors:
        for value in card_values:
            full_cards.append(color + value)
    
    return list(set(full_cards) - set(cards.split()))[0]