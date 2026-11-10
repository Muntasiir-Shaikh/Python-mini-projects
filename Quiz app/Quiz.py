
print("Welcome to Python Quiz!")

score = 0

print("\n1. Which language are we learning?")
print("a. Java")
print("b. Python")
print("c. C++")

answer = input("Your answer: ")

if answer.lower() == "b":
    print("Correct answer!")
    score = score + 1
else:
    print("Wrong answer!")

print("\n2. Which function is used to display output in Python?")
print("a. print()")
print("b. input()")
print("c. type()")

answer = input("Your answer: ")

if answer.lower() == "a":
    print("Correct answer!")
    score = score + 1
else:
    print("Wrong answer!")

print("\nYour final score is:", score, "/ 2")
