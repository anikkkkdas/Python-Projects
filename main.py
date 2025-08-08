try:
    a = int(input("Enter the First Number: "))
    b = int(input("Enter the Second Number: "))

    print("What kind of operation you want to perform. \n Press + for addition \n Press - for substraction \n Press / for division \n Press * for multiplication")

    o = input("Enter Operation: ")
    match o:
        case "+":
            print(f"The Result is {a+b}" )
        case "-":
            print(f"The Result is {a-b}" )
        case "*":
            print(f"The Result is {a*b}" )
        case "/":
            print(f"The Result is {a/b}" )
        case default:
            print("There was an Error")
except Exception as e:
    print("Enter the Valid Value of a & b")
