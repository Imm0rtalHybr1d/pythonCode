menu: dict[str,float] = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}




def get_price() :
        total = 0
        count = 0
        while True:
            try:
                item = input('Item: ')
                for k, v in menu.items():
                    # print(k,v)
                    if item.lower() == k.lower():
                        #print('$',round(v,2))
                        total += v
                        #count += 1
                        # if count > 1:
                        #      print("Total:${:.2f}".format(total),end="\n" )
                        # break

            except(KeyboardInterrupt,EOFError):
                rouned_price = "{:.2f}".format(total)
                print('')
                print('Total: $',rouned_price)
                break    

get_price()        
