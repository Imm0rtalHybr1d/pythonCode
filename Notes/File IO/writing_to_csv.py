# This code is essentially appending the contents of the `names_list` to the
# 'testing.csv' file.
names_list:list[str] = ['Marciano, Martin', 'Anastasia, Smith']

with open('testing.csv',mode='a') as file:
    for line in names_list:
        file.write(f'{line}\n')
        