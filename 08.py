list = ("Mike" "Bernard", "Ranz", "Brent", "Charls", "Sebastian")

find = input("input the name you want to search for in the list: ")
if find in list:
    print(f' found {find}!')
else:
    print(' not found')