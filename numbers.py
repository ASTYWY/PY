def f(c):
    if c == -14:
        print("Exellent, you are right. You are so smart!")
    else:
        print("Your answer is wrong, but you were so close, dear! The right answer is -14")
print("Do you want to solve the exercise? ")
answer =str(input())
if answer == "yes" :
    print("4*10-54")
    print("Take your time and solve the exercise.")
    answ = float(input("Type your answer: "))
    f(answ)
else:
    if answer == "no":
        print ("thanks, bye!")
    else:
        print ("ERROR! ERROR! ERROR!!!")
        
