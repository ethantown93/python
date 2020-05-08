def calc_investment():
    init_balance = init_balance1 = float(input('Enter the initial balance: '))
    init_interest = float(input('Enter your annual interest (10% = .1): '))
    
    years = 0
    
    while init_balance < 2*init_balance1:
        init_balance = init_balance * ( 1 + init_interest )
        years += 1


        print('Your investment will be doubled after ' + str(years) + '.')

calc_investment()

