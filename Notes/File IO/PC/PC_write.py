parts_list:list[str] = ['AMD Ryzen 5 5600X, 32GB RAM, 500GB NVME SSD',
                        'AMD Ryzen 5 3600, 16GB RAM, 250GB SATA SSD',
                        'AMD Ryzen 5 3600, 16GB RAM, "250GB SATA SSD,500GB HDD"']

with open('PC.csv',mode='a') as file:
    for line in parts_list:
        file.write(f'{line}')