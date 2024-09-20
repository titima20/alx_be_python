number = int(input("Enter a number to see its multiplication table: "))
for x in range(1, 11):
    print(number, "*", x, "=", number * x)
    print(end="")