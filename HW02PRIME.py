try:
    y = int(input("Enter a Number :  "))

    if y > 1:
        for x in range(2, y):
            if y % x == 0:
                print(y, " is not a prime number")
                break
        else:
            print(y, " is a prime number")

    else:
        print("Prime Number MUST be grater than 1")

except Exception as e:
    print("Invalid input, Please enter a NUMBER Greater than 1")
