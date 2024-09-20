size =int(input("Enter the size of the pattern: "))

rows = 1
while rows <= size: 
    for _ in range(size):
        print("*", end="")
    print()
    rows += 1