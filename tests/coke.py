total_cents = 0
price_of_coke = 0
accepted_coins = [5,10,25]
amount_due:0
change = 0

while True:
        added_cents = int(input('Insert coin: '))

        # checks if user enterd cents that accepted by the machine
        if added_cents in accepted_coins:
            total_cents += added_cents
            if total_cents < 50:
                amount_due = 50 - total_cents
                print(f'Amount Due: {amount_due}')
                continue
            elif total_cents > 50:
                change = total_cents - 50
                print(f'Change Owed: {change}')
                break
            elif total_cents == 50:
                print(f'Change Owed: {0}')
                break
        else:
            print("Amount Due: 50")
            continue
