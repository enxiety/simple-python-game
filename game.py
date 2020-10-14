answer = input("Are you ready to play? yes/no: ")
print("Total score will be given in the end")
score = 0

if answer.lower() == "yes":
    answer = input("Whats 2 + 2: ")
    if answer.lower() == "4":
        print("Correct, +1 score")
        score += 1
    else:
        print("Incorrect answer")

    answer = input("Whats 50 + 50: ")
    if answer == "100":
        print("Correct, +1 score")
        score += 1
    else:
        print("incorrect")

    answer = input("Whats 250 + 250: ")
    if answer == "500":
         print("Correct, +1 score")
         score += 1
    else:
        print("incorrect")

    answer = input("Whats 495353 + 4556892: ")
    if answer == "5052245":
        print("Correct, +2 score for harder question")
        score += 2
    else:
        print("incorrect, this one was tough anyways")

    answer = input("Whats 48 * 32: ")
    if answer == "1536":
        print("Correct, +1 score")
        score += 1
    else:
        print("incorrect")

        end = input("You've completed the game, would you like to see you're total score? if you get lower then 2 you fail. yes/no: ")

        if end == "yes":
            print(score)
            if score >= 3:
                print("You won!")
            else:
                print("You lost!")

        if end == "no":
            print("Bye!")
