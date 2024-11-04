print("How many rows would you like to have for a right-angled triangle?")
rows = int(input("Enter your number of rows: "))
num = 1

'''Loop for each rows, print numbers in increasing rows'''
for i in range(1, rows + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()

print(f"\nYou have successfully created a right-angled triangle of numbers!")