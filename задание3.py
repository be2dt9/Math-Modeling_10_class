y=int(input(y))
if y % 4 != 0:
    print(y,"Обычный")
elif y % 100 == 0:
    if y % 400 == 0:
        print(y,"Високосный")
    else:
        print(y,"Обычный")
else:
    print(y,"Високосный")
