def battery_charge(percent):
    graphic = "["
    for step in range(1, 100, 10):
        if round(percent, -1) >= step:
            graphic = graphic + "❚"
        else:
            graphic = graphic + " "
    
    graphic = graphic + "]"
    
    print(graphic)
    print(str(percent) + '%')