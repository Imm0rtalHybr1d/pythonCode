#open csv file
#read each line
    #store data in dict as keys:values as we iterate over each line 
#display data
def read_from_csv(file_path:str) -> None:
    with open(file_path) as file:
        rows:list[str] = file.readlines() 
        data:dict[str:str] = {}
        
        
        for row in rows:
            part,amount_paid,date_paid = row.rstrip().split(',')
            
            data['Part'] = part
            data['Amount Paid'] = amount_paid
            data['Date Paid'] = date_paid
            
            print('')
            print(f'{'_':_^30}')
            print(f'Component: {data['Part']}')
            print(f'Amount Paid: {data['Amount Paid']}')
            print(f'Date Paid: {data['Date Paid']}')

        
def main():
    file_path:str = 'pc_budget.csv'
    read_from_csv(file_path)
    
    
 
if __name__ == "__main__":
    main()
       
        
    