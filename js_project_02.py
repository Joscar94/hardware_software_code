def conversation():
    count = 0
    while True:
        print("Hello. I will ask you a series of questions to get to know you a little better, if you don't mind. You can always end this conversation anytime by typing 'exit'.")
        print("What's your name?")
        answer = input()
        if answer.lower() == "exit" or answer.lower() == "exit " or answer.lower() == " exit":
            closing_statement(count)
            break
        else:
            count +=1
        print("Amazing! Your name is {}.".format(answer))
        print("What game consoles do you have?")
        answer = input()
        if answer.lower() == "exit" or answer.lower() == "exit " or answer.lower() == " exit":
            closing_statement(count)
            break
        else:
            count +=1
        print("That sounds spectacular!")
        print("What's your favorite video game?")
        print("That sounds fantastic!")
        print("What's your favorite series?")
        print("That sounds phenomenal!")
        print("what's your favorite cartoon?")
        print("That sounds incredible!")
        print("What's your favorite movie?")
        print("That sounds cool!")
        print("Do you read comics?")
        print("That sounds awesome!")
        print("Thank you for your time. Goodbye!")
def main():
    conversation()

if __name__ == "__main__":
    main()
