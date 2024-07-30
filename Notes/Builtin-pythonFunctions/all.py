wifi_enabled: bool = True
has_electricity: bool = True
has_subscription: bool = True

# ineffecient
if wifi_enabled and has_subscription and has_electricity:
    print(f'Connected to internet')
    
#)______using ALL()
true_list:list[bool] = [wifi_enabled,has_electricity,has_subscription]  

if all(true_list):
    print(f'Connected to internet')