year = int(input('enter a year: '))
if (year % 4 ==0):
    if (year % 100 == 0):
        if (year % 400 == 0):
            print("leap year")
            print("a")
        else:
            print("not")
            print("b")
    else:
        print('leap year')
        print("c")
else:
    print("not")
    print("d")