a = int(input("Enter your age:- "))

if a < 18 :
    raise ValueError("You cannot vote. ")
else :
    print("You can vote. ")