def how_to_pay(amount, currency):
    pay_dict = {}
    
    sorted_currency = sorted(currency, key=lambda x: x, reverse=True)

    while amount > 0:
        for coin in sorted_currency:
            if amount >= coin:
                if coin in pay_dict.keys():
                    pay_dict[coin] += 1
                else:
                    pay_dict[coin] = 1
                
                amount -= coin
                break
            else:
                continue
    
    return pay_dict