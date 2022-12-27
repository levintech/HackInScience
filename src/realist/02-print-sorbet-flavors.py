FLAVORS = [
    "Banana",
    "Chocolate",
    "Lemon",
    "Pistachio",
    "Raspberry",
    "Strawberry",
    "Vanilla",
]

sorbet_list = []

def isValid(firstItem, secondItem):
    if firstItem == secondItem:
        return False

    for item in sorbet_list:
        if firstItem in item and secondItem in item:
            return False
    
    return True

for firstItem in FLAVORS:
    for secondItem in FLAVORS:
        if isValid(firstItem, secondItem):
            sorbet = firstItem + ", " + secondItem
            sorbet_list.append(sorbet)
            print(sorbet)
