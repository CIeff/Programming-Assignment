while True:
    name = input("Name: ")
    year = input("Year Of Study: ")

    if year == '1':
        fee = 1200.50
    elif year == '2' or year == '3':
        code = input("Code: ")
        code = code.upper()
        if code == 'A':
            fee = 1789.00
        elif code == 'B':
            fee = 2005.00
        else:
            fee = 2200.00
    elif year == '4':
        fee = 2555.50
    else:
        print("Please try again with year 1 ~ 4")
        exit()

    print("Name: {}, Year: {}, ".format(name, year), end = "")
    if year == '2' or year =='3':
        print("Code: {}".format(code), end= ", ")
    print("Fee: RM {}".format(format(fee, '.2f')))

    x = input("Is there another input? (y/n) ")
    x = x.lower()
    if x == 'y':
        pass
    elif x == 'n':
        exit()
    else:
        print("Invalid input received, considered yes as default")