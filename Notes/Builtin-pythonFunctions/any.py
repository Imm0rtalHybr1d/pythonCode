# Works similar to all()
#but with the exception that it checks if any / atleast 1 is true , then it returns true

wifi_enabled: bool = True
has_electricity: bool = True
has_subscription: bool = True

    
#)______using any()
true_list:list[bool] = [wifi_enabled,has_electricity,has_subscription]  

if any(true_list):
    print(f'Connected to internet')
    
print(f'{isinstance(true_list,int)}')    