count = 0
limit = 2
secret_num = 7


while count <= limit:
    guess = int(input("Enter a num. It is less than 30."))
    count += 1
    if guess == secret_num:
        print("Correct. You won!")
        break

else:
    print("You failed")
