
#initial state
state = 'A'
snack_1 = ['chips',2]
snack_2 = ['snoep',2]
snack_3 = ['cola',2]
total = 0

# while loop door alle states en wordt bij state G onderbroken
while True:
    if state == 'A':
        i = input("Type 'start' to start:\nType 'exit' to exit:\n\n")
        
        if i == 'start': 
            state = 'B'

        if i == 'exit':
            state = 'G'

    # state = b display alle snacks en prijs en vraag om geld
    if state == 'B':        
        print("\n{} voor €{:.2f}\n{} voor €{:.2f}\n{} voor €{:.2f}\n".format(snack_1[0], snack_1[1], snack_2[0], snack_2[1], snack_3[0], snack_3[1]))
        coin = float(input("Please insert coin: "))
        total = coin

        if coin >= 2:
            print("€{:.2f} inserted\n".format(coin))
            state = 'C'

        # vraag om meer geld
        while total < 2:
            coin = float(input("Please insert another coin: "))
            total += coin
            
            # genoeg geld, ga naar c 
            if total >= 2:
                print("€{:.2f} inserted".format(total))
                state = 'C'
                break

    # selecteer snack
    if state == 'C':
        snack_selection = input("Please select snack. \n--------\n{}\n{}\n{}\n--------\nrefund\n\n".format(snack_1[0], snack_2[0], snack_3[0]))
        if snack_selection == 'chips':
                state = 'D'

        if snack_selection == 'snoep':
                state = 'D'

        if snack_selection == 'cola':
                state = 'D'
        
        # persoon kan om refund vragen
        if snack_selection == 'refund':
            total = total - total
            print('\nMoney has been refunded. \n')
            state = 'A'

    # dispense snack
    if state == 'D':
        print('\nDispensing Snack...\n')
        change = total - 2
        state = 'E'

    # geef wisselgeld
    if state == 'E':
        if change >= 0:
            print('Returning Change of €{:.2f}\n'.format(change))
            state = 'A'

    # break out while loop en sluit machine
    if state == 'G':
        print("\nVending machine turning off...\n")
        break
