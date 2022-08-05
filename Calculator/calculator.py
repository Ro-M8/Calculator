while True :
    print("1 Addition")
    print("2 Substraction")
    print("3 Multipication")
    print("4 Division")
    print('Enter E or e to Exit')

    choice = input ("Enter your Choice : ")

    if choice == 'e' or choice =='E':
        break

    num1 = float(input ("Enter number 1 : "))
    num2 = float(input ("Enter number 2 : "))

    if choice == "1":
        print (num1, '+', num2 ,'=', (num1+num2))

    elif choice == "2":
        print (num1, '-' ,num2 ,'=', (num1-num2))

    elif choice == "3":
        print (num1, '*' ,num2 ,'=', (num1*num2))

    elif choice == "4":
        if num2 == 0.0:
            print( "Divide by 0 Error")
    else:    
        print (num1, '/' ,num2 ,'=', (num1/num2))

else:
    print("invalid choice")
    print()