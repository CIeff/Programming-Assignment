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

    print("-------------------------------------------") #partition
    print("           ABC COLLEGE INVOICE             ")
    print("Name: {} n\nYear: {} ".format(name, year), end = "") #display name,year of study
    if year == '2' or year =='3':
        print("\nCode: {}".format(code), end= " ") #display code in year 2 or 3
    print("\nFee : RM {}".format(format(fee, '.2f')))#compute and display fee
    print("-------------------------------------------") #partition

    x = input("Is there another input? (y/n) ")
    x = x.lower()
    if x == 'y':
        pass
    elif x == 'n':
        exit()
    else:
        print("Invalid input received, considered yes as default")