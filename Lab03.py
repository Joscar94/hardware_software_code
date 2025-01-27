

def conversation():
    print("Hello what's your name")
    Name = input()
    print("What's your high school")
    High_school = input()
    print("What's your college")
    College = input()
    print("Which institution is more fun")
    Choice = input()
    print("I learned that you went to {}".format(High_school))
    print("You're currently attending {}".format(College))
def main():
    conversation()
if __name__ == "__main__":
 main()
